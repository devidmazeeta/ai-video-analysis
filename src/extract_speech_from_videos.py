import os
import moviepy.editor as mp
import speech_recognition as sr
from google.cloud import speech
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

# Directory paths
VIDEO_DIR = "../input/videos/"
AUDIO_DIR = "../output/audios/"
TEXT_DIR = "../output/transcripts/"

# Ensure directories exist
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(TEXT_DIR, exist_ok=True)

# Path to OAuth Client JSON file (Replace with actual path)
OAUTH_JSON_PATH = "../client_secret.json"
TOKEN_PATH = "../token.json"

# OAuth 2.0 Scope for Google Cloud API Access
SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]

def authenticate_with_oauth():
    """Authenticates with Google Cloud using OAuth 2.0"""
    creds = None

    # Check if the user has already authenticated (token.json)
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    # If there are no valid credentials, authenticate the user
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(OAUTH_JSON_PATH, SCOPES)
        creds = flow.run_local_server(port=8080)  # Ensure this matches Google Cloud redirect URI

        # Save credentials for future use
        with open(TOKEN_PATH, "w") as token_file:
            token_file.write(creds.to_json())

    return speech.SpeechClient(credentials=creds)

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

if __name__ == "__main__":
    client = authenticate_with_oauth()
    extract_audio_from_videos(VIDEO_DIR, AUDIO_DIR)
    convert_audio_to_text(AUDIO_DIR, TEXT_DIR, client)
    print("Processing completed!")
