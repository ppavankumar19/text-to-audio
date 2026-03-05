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

Click the button below to listen to the audio on the live player:

<div align="center">

[![Live Audio Player](https://img.shields.io/badge/LIVE_PLAYER-Click_to_Listen-brightgreen?style=for-the-badge&logo=google-play&logoColor=white)](https://ppavankumar19.github.io/text-to-audio/)

*(Hosted via GitHub Pages)*

</div>

## Features

- Supports Indian English (`en-IN`), Telugu (`te-IN`), and other Indian languages.
- **Smart Chunking:** Automatically splits long text files to stay within API limits.
- **Web Player:** Includes a dedicated web player for easy sharing and listening.
