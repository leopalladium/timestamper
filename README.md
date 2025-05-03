# timestamper

This project helps you to timestamp every sentence in `.txt` files. It is useful for preparing data for AI Speech-to-Text (STT) models training from already transcribed text.

## Features
- Adds a timestamp template to each sentence in `.txt` files.
- Preserves paragraphs and formatting from the original text.
- Creates or modifies `.docx` files based on the source `.txt` files:
  - If a `.docx` file with the same name exists, it will be updated.
  - If no `.docx` file exists, a new one will be created.

## How to Use
1. Place the script in the folder containing your `.txt` files.
2. Run the script. The console will display a list of available `.txt` files.
3. Select the files you want to process by entering their numbers (comma-separated).
4. The script will:
   - Generate new `.txt` files with timestamps.
   - Optionally create or modify `.docx` files if you choose to do so.
5. The processed files will be saved in the same directory as the script.

## Requirements
- Python 3.x
- `python-docx` package (install with `pip install python-docx`)

## Author
Klimentsi Katsko (@leopalladium)
