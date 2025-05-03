import os
import re
import sys
from datetime import datetime
from docx import Document  # Requires `python-docx` package


def add_template_to_sentences(input_file, output_file, template):
    # Read the content of the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the text into paragraphs
    paragraphs = content.split('\n')

    # Process each paragraph
    updated_content = ''
    for paragraph in paragraphs:
        if paragraph.strip():  # Ignore empty paragraphs
            # Split the paragraph into sentences
            sentences = re.split(r'(?<=[.!?])\s+', paragraph)
            for sentence in sentences:
                if sentence.strip():  # Ignore empty sentences
                    # Add the template before each sentence
                    updated_content += f"{template}\n{sentence}\n"
            updated_content += '\n'  # Preserve paragraph breaks
        else:
            updated_content += '\n'  # Preserve empty lines

    # Write the updated text to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(updated_content)


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
                    doc.add_paragraph(f"{template} {sentence}")
            doc.add_paragraph("")  # Preserve paragraph breaks
        else:
            doc.add_paragraph("")  # Preserve empty lines

    # Save the .docx file
    doc.save(docx_file)
    print(f"Processed .docx file: {docx_file}")


def main():
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

    # List all .txt files in the current directory
    txt_files = [f for f in os.listdir(current_dir) if f.endswith('.txt')]
    if not txt_files:
        print("No .txt files found in the current directory.")
        input("Press Enter to exit...")
        return

    # Display the list of .txt files
    print("Available .txt files:")
    for idx, file in enumerate(txt_files, start=1):
        print(f"{idx}: {file}")

    # Ask the user to select files
    selected_files = input("Enter the numbers of the files to process (comma-separated): ")
    try:
        selected_indices = [int(i.strip()) - 1 for i in selected_files.split(',')]
        selected_files = [txt_files[i] for i in selected_indices if 0 <= i < len(txt_files)]
    except (ValueError, IndexError):
        print("Invalid selection. Exiting.")
        input("Press Enter to exit...")
        return

    # Process each selected file
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    template = f"[HH:MM:SS,MS --> HH:MM:SS,MS]"

    for file in selected_files:
        timestamp_file = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f"{os.path.splitext(file)[0]}_output_{timestamp_file}.txt"
        add_template_to_sentences(file, output_file, template)
        print(f"Processed {file} -> {output_file}")

    # Ask the user if they want to process .docx files
    process_docx_option = input("Do you want to create/modify .docx files? (yes/no): ").strip().lower()
    if process_docx_option == 'yes':
        for file in selected_files:
            process_docx(file, template)

    # Prevent the console from closing immediately
    input("Task completed. Press Enter to exit...")


if __name__ == "__main__":
    main()

