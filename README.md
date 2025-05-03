# Timestamper

**Timestamper** is a lightweight tool designed to add timestamps to every sentence in `.txt` files. It's especially useful for preparing transcribed text data for training AI Speech-to-Text (STT) models.

---

## ✨ Features
- **Timestamp Integration**: Automatically adds a timestamp template to each sentence in `.txt` files.
- **Preserves Formatting**: Retains original paragraphs and formatting.
- **Flexible Output Options**:
  - Updates existing `.docx` files if they share the same name as the `.txt` file.
  - Creates new `.docx` files if none exist.

---

## 🚀 How to Use
1. **Setup**:
   - Place the script in the same folder as your `.txt` files.
2. **Run the Script**:
   - Execute the script via the terminal or command line.
3. **File Selection**:
   - A list of available `.txt` files will appear in the console.
   - Select the files you wish to process by entering their numbers (comma-separated).
4. **Processing**:
   - The script will:
     - Generate new `.txt` files with timestamps.
     - Optionally create or update `.docx` files based on your choice.
5. **Output**:
   - Processed files are saved in the same directory as the script.

---

## 📋 Requirements
To use **Timestamper**, ensure the following are installed:

- **Python**: Version 3.x
- **Dependencies**: Install the required Python package with:
  ```bash
  pip install python-docx
