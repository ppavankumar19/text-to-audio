# Text to Audio Converter (Sarvam.ai)

This project converts text from a `story.txt` file into an audio file (`audio.mp3`) using the Sarvam.ai Text-to-Speech (TTS) API.

## Prerequisites

- Python 3.8+
- Sarvam.ai API Key

## How to get Sarvam.ai API Key

1.  **Sign Up**: Go to [dashboard.sarvam.ai](https://dashboard.sarvam.ai/) and create an account.
2.  **API Keys**: Navigate to the **"API Keys"** section in the sidebar.
3.  **Generate**: Click **"Create New API Key"**, give it a name, and copy the key immediately.
4.  **Credits**: Check the **"Billing"** or **"Usage"** tab to ensure you have active free credits (usually provided to new accounts).

## Setup (Recommended: Virtual Environment)

Since modern Linux distributions protect the system Python environment, use a virtual environment:

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

Listen to the generated audio directly here:

https://github.com/ppavankumar19/text-to-audio/raw/main/audio.mp3

> **Note:** If the player above doesn't appear, you can also [click here to play/download the file](https://github.com/ppavankumar19/text-to-audio/raw/main/audio.mp3).

## Features

- Supports Indian English (`en-IN`), Telugu (`te-IN`), and other Indian languages.
- **Smart Chunking:** Automatically splits long text files to stay within API limits.
- **GitHub Playback:** The generated `audio.mp3` can be played directly within the GitHub web interface.
