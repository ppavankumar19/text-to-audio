# Text to Audio Converter (Sarvam.ai)

This project converts text from a `story.txt` file into an audio file (`audio.mp3`) using the Sarvam.ai Text-to-Speech (TTS) API.

## Prerequisites

- Python 3.8+
- Sarvam.ai API Key

## Setup (Recommended: Virtual Environment)

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

2. **Activate the environment:**
   ```bash
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your text in `story.txt`.
2. Ensure your virtual environment is active (`source venv/bin/activate`).
3. Run the script:
   ```bash
   python main.py
   ```
4. The output will be saved as `audio.mp3`.

## Audio Preview

*(To activate the inline player: Edit this README on GitHub and drag & drop your `audio.mp3` file here!)*
[audio.mp3](https://github.com/user-attachments/files/25763237/audio.mp3)

## Features

- Supports Indian English (`en-IN`), Telugu (`te-IN`), and other Indian languages.
- **Smart Chunking:** Automatically splits long text files to stay within API limits.
- **Native Experience:** Uses GitHub's secure, built-in player for the best audio quality.
