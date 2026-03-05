# Text to Audio Converter (Sarvam.ai)

This project converts text from any file into an audio file (`audio.mp3`) using the Sarvam.ai Text-to-Speech (TTS) API. It now features **automatic language detection** and **multi-speaker support**.

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

### Advanced Usage

You can now specify a different speaker or a different text file:
```bash
python main.py --speaker ritu --file my_story.txt
```
*Available speakers: `shubh`, `ritu`, `priya`, `aditya`, etc.*

## Audio Preview

Click the button below to listen to the audio on the live player:

<div align="center">

[![Live Audio Player](https://img.shields.io/badge/LIVE_PLAYER-Click_to_Listen-brightgreen?style=for-the-badge&logo=google-play&logoColor=white)](https://ppavankumar19.github.io/text-to-audio/)

*(Hosted via GitHub Pages)*

</div>

## Advanced Features

- **Auto Language Detection**: Automatically detects if the text is in Telugu, Hindi, English, etc., and sets the correct API parameters.
- **Smart Chunking**: Automatically splits long text files to stay within API limits.
- **Multi-Speaker Support**: Choose from various Sarvam AI voices via command-line arguments.
- **Web Player**: Includes a dedicated web player for easy sharing and listening.
