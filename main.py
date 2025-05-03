import os
import re
import sys
import traceback
from datetime import datetime
from docx import Document  # Requires `python-docx` package
from faster_whisper import WhisperModel  # Requires `faster-whisper` package


def add_template_to_sentences(input_file, output_file, template):
    """
    Добавляет шаблон перед каждым предложением в тексте.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Разделение текста на абзацы
    paragraphs = content.split('\n')

    updated_content = ''
    for paragraph in paragraphs:
        if paragraph.strip():  # Игнорируем пустые абзацы
            # Разделение абзаца на предложения
            sentences = re.split(r'(?<=[.!?])(?<!\b\w\.\w)(?<!\b\w\.)\s+', paragraph)
            for sentence in sentences:
                if sentence.strip():  # Игнорируем пустые предложения
                    updated_content += f"{template}\n{sentence}\n"
            updated_content += '\n'  # Сохраняем разрывы между абзацами
        else:
            updated_content += '\n'

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(updated_content)


def add_timestamps_to_sentences(input_file, output_file):
    """
    Add timestamps in SRT format to each sentence in the input file.
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', content)

    # Generate timestamps for each sentence
    timestamped_content = ""
    start_time = 0.0  # Start time in seconds
    duration = 2.0  # Assume each sentence takes 2 seconds (adjust as needed)

    for idx, sentence in enumerate(sentences, start=1):
        if sentence.strip():
            end_time = start_time + duration
            start_timestamp = format_timestamp(start_time)
            end_timestamp = format_timestamp(end_time)
            timestamped_content += f"{idx}\n{start_timestamp} --> {end_timestamp}\n{sentence.strip()}\n\n"
            start_time = end_time

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(timestamped_content)

    print(f"Timestamps added to {output_file}")


def process_docx(input_file, template):
    # Generate the name of the .docx file
    docx_file = f"{os.path.splitext(input_file)[0]}.docx"

    # Read the content of the input .txt file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the text into paragraphs
    paragraphs = content.split('\n')

    # Create or modify the .docx file
    if os.path.exists(docx_file):
        print(f"Updating existing .docx file: {docx_file}")
        doc = Document(docx_file)
    else:
        print(f"Creating new .docx file: {docx_file}")
        doc = Document()

    # Add content to the .docx file
    for paragraph in paragraphs:
        if paragraph.strip():  # Ignore empty paragraphs
            sentences = re.split(r'(?<=[.!?])\s+', paragraph)
            for sentence in sentences:
                if sentence.strip():  # Ignore empty sentences
                    doc.add_paragraph(template)  # Add the template on a separate line
                    doc.add_paragraph(sentence)  # Add the sentence on the next line
            doc.add_paragraph("")  # Preserve paragraph breaks
        else:
            doc.add_paragraph("")  # Preserve empty lines

    # Save the .docx file
    doc.save(docx_file)
    print(f"Processed .docx file: {docx_file}")


def generate_srt_from_audio(audio_file, language, model):
    """
    Generate .txt and .srt files from an audio file using the faster-whisper library.

    :param audio_file: Path to the audio file.
    :param language: Language code for transcription (e.g., "en", "ru").
    :param model: WhisperModel instance.
    """
    print(f"Transcribing {audio_file}...")
    segments_gen, _ = model.transcribe(audio_file, language=language)
    segments = list(segments_gen)  # Сохраняем все сегменты в список

    # Generate the .txt file
    txt_file = f"{os.path.splitext(audio_file)[0]}.txt"
    with open(txt_file, 'w', encoding='utf-8') as file:
        for segment in segments:
            text = segment.text.strip()
            file.write(f"{text}\n")
    print(f"Text file created: {txt_file}")

    # Generate the .srt file
    srt_file = f"{os.path.splitext(audio_file)[0]}.srt"
    with open(srt_file, 'w', encoding='utf-8') as file:
        for idx, segment in enumerate(segments, start=1):
            start_time = format_timestamp(segment.start)
            end_time = format_timestamp(segment.end)
            text = segment.text.strip()
            file.write(f"{idx}\n")
            file.write(f"{start_time} --> {end_time}\n")
            file.write(f"{text}\n\n")
    print(f"SRT file created: {srt_file}")

    return txt_file


def format_timestamp(seconds):
    """
    Форматирует секунды в строку SRT (HH:MM:SS,MS).
    """
    total_milliseconds = int(round(seconds * 1000))
    hours, remainder = divmod(total_milliseconds, 3600 * 1000)
    minutes, remainder = divmod(remainder, 60 * 1000)
    secs, milliseconds = divmod(remainder, 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{milliseconds:03}"


def log_error(error_message):
    """
    Log errors to a file named 'error_log.txt' in the current directory.

    :param error_message: The error message to log.
    """
    log_file = "error_log.txt"
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {error_message}\n")
    print(f"An error occurred. Details have been logged to {log_file}.")


def main():
    try:
        # Display author information
        print("Author: Klimentsi Katsko (@leopalladium)")
        print("Welcome to the Time Stamper script!")

        # Get the directory where the script is located
        if getattr(sys, 'frozen', False):  # Check if the script is running as a bundled executable
            current_dir = os.path.dirname(sys.executable)
        else:
            current_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"Current directory: {current_dir}")

        # Explicitly set the working directory to the script's directory
        os.chdir(current_dir)

        # List all .txt and audio files in the current directory
        txt_files = [f for f in os.listdir(current_dir) if f.endswith('.txt')]
        audio_files = [f for f in os.listdir(current_dir) if f.endswith(('.mp3', '.wav', '.m4a'))]

        if not txt_files and not audio_files:
            print("No .txt or audio files found in the current directory.")
            input("Press Enter to exit...")
            return

        # Ask the user how to handle timestamps
        print("Choose how to handle timestamps:")
        print("1: Add timestamp templates only (manual editing)")
        print("2: Automatically generate timestamps using AI for audio files")
        timestamp_option = input("Enter your choice (1 or 2): ").strip()

        # Ask the user to select the Whisper model
        print("Select the Whisper model to use:")
        print("1: tiny")
        print("2: base")
        print("3: small")
        print("4: medium")
        print("5: large")
        model_choice = input("Enter your choice (1-5): ").strip()

        model_map = {
            "1": "tiny",
            "2": "base",
            "3": "small",
            "4": "medium",
            "5": "large"
        }
        model_name = model_map.get(model_choice, "base")  # Default to "base" if invalid choice
        print(f"Selected model: {model_name}")

        if timestamp_option == "1":
            # Process .txt files with templates and timestamps
            if not txt_files:
                print("No .txt files found for manual processing.")
            else:
                print("Available .txt files:")
                for idx, file in enumerate(txt_files, start=1):
                    print(f"{idx}: {file}")

                selected_files = input("Enter the numbers of the files to process (comma-separated): ")
                try:
                    selected_indices = [int(i.strip()) - 1 for i in selected_files.split(',')]
                    selected_files = [txt_files[i] for i in selected_indices if 0 <= i < len(txt_files)]
                except (ValueError, IndexError):
                    print("Invalid selection. Exiting.")
                    input("Press Enter to exit...")
                    return

                for file in selected_files:
                    timestamp_file = datetime.now().strftime('%Y%m%d_%H%M%S')
                    output_file = f"{os.path.splitext(file)[0]}_timestamped_{timestamp_file}.srt"
                    add_timestamps_to_sentences(file, output_file)
                    print(f"Processed {file} -> {output_file}")

        elif timestamp_option == "2":
            # Process audio files with AI
            if not audio_files:
                print("No audio files found for AI processing.")
            else:
                print("Available audio files:")
                for idx, file in enumerate(audio_files, start=1):
                    print(f"{idx}: {file}")

                selected_files = input("Enter the numbers of the audio files to process (comma-separated): ")
                try:
                    selected_indices = [int(i.strip()) - 1 for i in selected_files.split(',')]
                    selected_files = [audio_files[i] for i in selected_indices if 0 <= i < len(audio_files)]
                except (ValueError, IndexError):
                    print("Invalid selection. Exiting.")
                    input("Press Enter to exit...")
                    return

                # Ask the user to select the language
                language = input("Enter the language code for transcription (e.g., 'en' for English, 'ru' for Russian): ").strip()

                print(f"Loading Whisper model: {model_name}...")
                model = WhisperModel(model_name, device="cuda")

                for file in selected_files:
                    txt_file = generate_srt_from_audio(file, language, model)

                    # Ask if the user wants to generate a .docx file
                    generate_docx = input(f"Do you want to generate a .docx file for {file}? (yes/no): ").strip().lower()
                    if generate_docx == "yes":
                        process_docx(txt_file, f"HH:MM:SS,MS --> HH:MM:SS,MS")

        else:
            print("Invalid choice. Exiting.")
            input("Press Enter to exit...")
            return

    except Exception as e:
        error_message = traceback.format_exc()
        log_error(error_message)
        print("An unexpected error occurred. Please check the error log for details.")
        input("Press Enter to exit...")

    # Prevent the console from closing immediately
    input("Task completed. Press Enter to exit...")


if __name__ == "__main__":
    main()

