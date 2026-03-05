import os
import base64
import requests
import argparse
from dotenv import load_dotenv
from langdetect import detect

# Configuration
MAX_CHARS_PER_CHUNK = 2000

# Language Mapping (Auto-detect → Sarvam Code)
LANG_MAP = {
    'te': 'te-IN', # Telugu
    'hi': 'hi-IN', # Hindi
    'en': 'en-IN', # English
    'kn': 'kn-IN', # Kannada
    'ml': 'ml-IN', # Malayalam
    'ta': 'ta-IN', # Tamil
    'mr': 'mr-IN', # Marathi
    'bn': 'bn-IN', # Bengali
}

def detect_language(text):
    """
    Automatically detects the language of the input text.
    """
    try:
        lang_code = detect(text)
        return LANG_MAP.get(lang_code, 'en-IN') # Default to en-IN if not found
    except Exception:
        return 'en-IN'

def get_audio_from_api(text, language_code, speaker="shubh"):
    """
    Calls Sarvam.ai's TTS API for a single chunk of text.
    """
    api_key = os.getenv("SARVAM_API_KEY")
    if not api_key:
        print("Error: SARVAM_API_KEY not found in environment.")
        return None

    url = "https://api.sarvam.ai/text-to-speech"
    payload = {
        "text": text,
        "target_language_code": language_code,
        "speaker": speaker,
        "model": "bulbul:v3"
    }
    headers = {
        "api-subscription-key": api_key,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        if "audios" in data and len(data["audios"]) > 0:
            return base64.b64decode(data["audios"][0])
    except Exception as e:
        print(f"Error calling API: {e}")
        if hasattr(e, 'response') and e.response:
            print("Response:", e.response.text)
    return None

def chunk_text(text, max_len=MAX_CHARS_PER_CHUNK):
    """
    Splits text into chunks of roughly max_len, trying not to break sentences.
    """
    chunks = []
    while len(text) > max_len:
        split_at = text.rfind('.', 0, max_len)
        if split_at == -1: split_at = max_len
        chunks.append(text[:split_at + 1].strip())
        text = text[split_at + 1:].strip()
    if text:
        chunks.append(text)
    return chunks

def main():
    parser = argparse.ArgumentParser(description="Sarvam AI Text-to-Audio Converter")
    parser.add_argument("--speaker", default="shubh", help="Select speaker: shubh, ritu, priya, etc.")
    parser.add_argument("--file", default="story.txt", help="Path to your story file.")
    args = parser.parse_args()

    load_dotenv()
    
    if not os.path.exists(args.file):
        print(f"Error: {args.file} not found.")
        return

    try:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read().strip()
    except Exception as e:
        print(f"Failed to read file: {e}")
        return

    if not text:
        print("Error: Input file is empty.")
        return

    # Auto-detect language
    target_lang = detect_language(text)
    print(f"Detected language: {target_lang}")
    print(f"Using speaker: {args.speaker}")

    chunks = chunk_text(text)
    print(f"Processing {len(chunks)} chunk(s)...")

    all_audio_data = []
    for i, chunk in enumerate(chunks):
        print(f"Converting chunk {i+1}/{len(chunks)}...")
        audio_data = get_audio_from_api(chunk, target_lang, args.speaker)
        if audio_data:
            all_audio_data.append(audio_data)
        else:
            print(f"Failed to convert chunk {i+1}. Stopping.")
            return

    # Combine all chunks into one file
    output_file = "audio.mp3"
    with open(output_file, "wb") as f:
        for chunk_data in all_audio_data:
            f.write(chunk_data)
    
    print(f"Success! Combined audio saved as: {output_file}")

if __name__ == "__main__":
    main()
