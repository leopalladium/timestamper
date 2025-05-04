
# Timestamper

**Timestamper** provides tools for working with audio transcription and subtitle files. It allows you to generate timestamps for text files, transcribe audio files into subtitles, and convert .srt subtitle files into .docx documents.


## Features

- **Add Timestamps to Text Files:** Automatically generate timestamp templates for .txt files.
- **Audio Transcription:** Transcribe audio files (.mp3, .wav, .m4a, .aac, .webm) into .srt subtitle files using the faster-whisper library.
- **Word-Level Timestamps:** Generate subtitles with precise word-level timestamps.
- **SRT to DOCX Conversion:** Convert .srt subtitle files into .docx documents with timestamps and text.
- **Custom Whisper Model Selection:** Choose from various Whisper model sizes (tiny, base, small, medium, large) for transcription.
- **Multi-Language Support:** Specify the language for audio transcription.


## Installation

1. Clone the repository:
```
git clone https://github.com/leopalladium/time-stamper.git
cd time-stamper
```
2. Install dependencies:
```
pip install -r requirements.txt
```
## Usage/Examples

I've created this script to simplify my $10 contract from Upwork (some enterprise clients say that this is easy task, but you must proofread and timestamp hours of shitty recorded audio), so this is simple STT application which can recognize and timestamp audio to simplify such monkey job to just proofreading as it was declared.

### Transcribing an Audio File
    1. Place your audio file in the same directory as the script.
    2. Run the script and select the transcription option.
    3. Choose the audio file and Whisper model
    4. The script generates an .srt file with word-level timestamps
    5. Choose if you want to generate .docx or not
    6. Find generated files in the directory

### Placing timestamp templates before each sentence (v1.0.0.0)
    1. Place .txt with the text in the same directory as the script
    2. Choose your file
    3. Get the .txt divided on the sentences with .srt-like timestamp templates before each sentence
    
     

## License

This project is licensed under the MIT License. See the LICENSE file for details.


## Authors

- [Klimentsi Katsko (@leopalladium)](https://www.github.com/leopalladium)

