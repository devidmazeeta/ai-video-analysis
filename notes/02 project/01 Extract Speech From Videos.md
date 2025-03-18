### **Explanation of the Python Program**
This Python script automates the process of:
1. **Extracting audio** from video files.
2. **Converting speech** from the extracted audio into text using **Google Cloud Speech-to-Text API**.
3. **Saving transcripts** as text files.

The program follows these steps:

---

## **1. Importing Required Libraries**
```python
import os
import moviepy.editor as mp
import speech_recognition as sr
from google.cloud import speech
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
```
- `os`: Handles file and directory operations.
- `moviepy.editor`: Extracts audio from video files.
- `speech_recognition`: Unused in this script but usually helps with local speech-to-text conversion.
- `google.cloud.speech`: Allows interaction with Google Cloud's Speech-to-Text API.
- `google_auth_oauthlib.flow` and `google.oauth2.credentials`: Handle OAuth authentication for Google Cloud API access.

---

## **2. Setting Up Directory Paths**
```python
VIDEO_DIR = "../input/videos/"
AUDIO_DIR = "../output/audios/"
TEXT_DIR = "../output/transcripts/"

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(TEXT_DIR, exist_ok=True)
```
- Specifies the paths where **videos**, **extracted audio files**, and **transcripts** will be stored.
- Ensures that directories exist (if they don't, they are created).

---

## **3. OAuth 2.0 Authentication for Google Cloud API**
```python
OAUTH_JSON_PATH = "../client_secret.json"
TOKEN_PATH = "../token.json"
SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]
```
- `OAUTH_JSON_PATH`: Path to the OAuth 2.0 credentials file (replace it with the actual path).
- `TOKEN_PATH`: Stores authenticated credentials for future use.
- `SCOPES`: Specifies the access level needed (full access to the Google Cloud platform).

#### **Authenticate the user with Google Cloud API**
```python
def authenticate_with_oauth():
    """Authenticates with Google Cloud using OAuth 2.0"""
    creds = None

    # Check if already authenticated
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    # If not authenticated, request credentials
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(OAUTH_JSON_PATH, SCOPES)
        creds = flow.run_local_server(port=8080)  # Opens a local web server for authentication

        # Save credentials
        with open(TOKEN_PATH, "w") as token_file:
            token_file.write(creds.to_json())

    return speech.SpeechClient(credentials=creds)
```
- If a valid `token.json` file exists, it loads the stored credentials.
- Otherwise, it prompts the user for authentication using OAuth 2.0 and saves the credentials.

---

## **4. Extracting Audio from Videos**
```python
def extract_audio_from_videos(video_dir, audio_dir):
    """Extracts audio from videos and saves them as WAV files."""
    for filename in os.listdir(video_dir):
        if filename.endswith(('.mp4', '.avi', '.mov', '.mkv', '.flv')):
            video_path = os.path.join(video_dir, filename)
            audio_filename = os.path.splitext(filename)[0] + ".wav"
            audio_path = os.path.join(audio_dir, audio_filename)

            print(f"Extracting audio from {filename}...")
            video = mp.VideoFileClip(video_path)
            video.audio.write_audiofile(audio_path, codec='pcm_s16le')
```
- Loops through all video files in `video_dir`.
- Converts video formats (`.mp4`, `.avi`, `.mov`, `.mkv`, `.flv`) to **audio WAV** files.
- Saves the extracted audio as WAV format (`pcm_s16le` codec for high-quality speech processing).

---

## **5. Converting Audio to Text Using Google Cloud Speech-to-Text**
```python
def convert_audio_to_text(audio_dir, text_dir, client):
    """Converts audio speech to text using Google Cloud Speech-to-Text API."""
    for filename in os.listdir(audio_dir):
        if filename.endswith(".wav"):
            audio_path = os.path.join(audio_dir, filename)
            text_filename = os.path.splitext(filename)[0] + ".txt"
            text_path = os.path.join(text_dir, text_filename)

            print(f"Converting {filename} to transcript using Google Cloud API...")

            with open(audio_path, "rb") as audio_file:
                content = audio_file.read()

            # Prepare Google Cloud Speech API request
            audio = speech.RecognitionAudio(content=content)
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=16000,
                language_code="en-US",
                enable_automatic_punctuation=True,  # Enables punctuation in transcripts
            )

            try:
                response = client.recognize(config=config, audio=audio)
                transcript = "\n".join([result.alternatives[0].transcript for result in response.results])

                # Save the transcript
                with open(text_path, "w", encoding="utf-8") as text_file:
                    text_file.write(transcript)
                print(f"Saved transcript: {text_path}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")
```
### **Steps:**
1. Loops through **all WAV files** in the `audio_dir`.
2. Reads the audio file and sends it to **Google Cloud Speech-to-Text API**.
3. Configures:
   - `encoding="LINEAR16"`: Required for WAV files.
   - `sample_rate_hertz=16000`: Recommended sample rate.
   - `language_code="en-US"`: Specifies English (US) as the transcription language.
   - `enable_automatic_punctuation=True`: Adds punctuation to improve readability.
4. **Processes API response** and extracts text from recognized speech.
5. **Saves transcript** in the `text_dir`.

---

## **6. Running the Program**
```python
if __name__ == "__main__":
    client = authenticate_with_oauth()
    extract_audio_from_videos(VIDEO_DIR, AUDIO_DIR)
    convert_audio_to_text(AUDIO_DIR, TEXT_DIR, client)
    print("Processing completed!")
```
### **Execution Flow:**
1. Authenticates with **Google Cloud API**.
2. Extracts **audio** from all videos.
3. Converts **audio to text** using Google Cloud Speech-to-Text.
4. **Saves the transcript** as a `.txt` file.

---

## **Summary**
This program is useful for **automated transcription of videos**:
- **OAuth authentication** ensures secure access to Google Cloud API.
- **MoviePy extracts audio** from videos.
- **Google Cloud Speech-to-Text API converts speech** to text.
- **Automatic punctuation** makes transcripts more readable.

---
