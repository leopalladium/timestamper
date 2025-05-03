import os
import re
from datetime import datetime

def add_template_to_sentences(input_file, output_file, template):
    # Read the content of the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split the text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', content)
    
    # Add the template after each sentence
    updated_content = ''
    for sentence in sentences:
        if sentence.strip():  # Ignore empty lines
            updated_content += f"{sentence} {template}\n"
    
    # Write the updated text to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(updated_content)

def main():
    # Path to the input file
    input_file = 'input.txt'  # Ensure the file exists in the same directory
    # Generate the output file name with a timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = f'output_{timestamp}.txt'
    
    # Template to be added
    template = '[TIMESTAMP]'
    
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"The file {input_file} was not found.")
        return
    
    # Process the file
    add_template_to_sentences(input_file, output_file, template)
    print(f"The processed file has been saved as {output_file}")

if __name__ == "__main__":
    main()
