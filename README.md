# Timestamper

**Timestamper** is a Python tool for working with audio transcription and subtitle files. It enables you to generate timestamped templates for text, transcribe audio into subtitles with word-level timestamps, and convert `.srt` subtitle files into `.docx` documents.

## Features

- **Add Timestamps to Text Files:** Automatically generate `.srt`-style timestamp templates for `.txt` files.
- **Audio Transcription:** Transcribe audio files (`.mp3`, `.wav`, `.m4a`, `.aac`, `.webm`) into `.srt` subtitle files using the `faster-whisper` library.
- **Word-Level Timestamps:** Generate subtitles with precise word-level timestamps.
- **SRT to DOCX Conversion:** Convert `.srt` subtitle files into `.docx` documents with timestamps and text.
- **Custom Whisper Model Selection:** Choose from various Whisper model sizes (`tiny`, `base`, `small`, `medium`, `large`) for transcription.
- **Multi-Language Support:** Specify the language for audio transcription.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/leopalladium/timestamper.git
    cd timestamper
    ```
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Transcribing Audio Files

1. Run `main.py`.
2. Select the root directory containing your audio files.
3. Choose the Whisper model size.
4. Enter the language code (e.g., `en`, `ru`).
5. Select which audio files to process or type `all` to process all found files.
6. The script generates `.srt` files with word-level timestamps in the same directory as the audio files.

### Adding Timestamp Templates to Text Files

1. Place your `.txt` file in the script directory.
2. Use the `add_timestamps_to_sentences` function to generate a timestamped template.

### Converting SRT to DOCX

1. Use the `convert_srt_to_docx` function to convert an `.srt` file to a `.docx` document.

## Roadmap

- [ ] Add speaker diarization
- [ ] Optimize and debug code
- [ ] Develop as a subtitle editing tool
- [ ] API for server deployment
- [ ] Add audio track from video text recognition
- [ ] Make executable more lightweight
- [ ] Add signature for executable

## License

This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for details.

## Author

- [Klimentsi Katsko (@leopalladium)](https://github.com/leopalladium)