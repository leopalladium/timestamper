import os
import re
from datetime import datetime


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


def main():
    # Get the directory where the script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Current directory: {current_dir}")

    # Change the working directory to the script's directory
    os.chdir(current_dir)

    # List all .txt files in the current directory
    txt_files = [f for f in os.listdir(current_dir) if f.endswith('.txt')]
    if not txt_files:
        print("No .txt files found in the current directory.")
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
        return

    # Process each selected file
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    template = f"[HH:MM:SS,MS --> HH:MM:SS,MS]"

    for file in selected_files:
        timestamp_file = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f"{os.path.splitext(file)[0]}_output_{timestamp_file}.txt"
        add_template_to_sentences(file, output_file, template)
        print(f"Processed {file} -> {output_file}")


if __name__ == "__main__":
    main()
