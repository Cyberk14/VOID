# import requests
# from playsound import playsound

# CHUNK_SIZE = 1024
# url = "https://api.elevenlabs.io/v1/text-to-speech/<voice-id>"

# headers = {
#   "Accept": "audio/mpeg",
#   "Content-Type": "application/json",
#   "xi-api-key": "b1c950b3f3aea69e6f35e70c4578cd52"
# }

# data = {
#   "text": """Born and raised in the charming south, 
#   I can add a touch of sweet southern hospitality 
#   to your audiobooks and podcasts""",
#   "model_id": "eleven_monolingual_v1",
#   "voice_settings": {
#     "stability": 0.5,
#     "similarity_boost": 0.5
#   }
# }

# response = requests.post(url, json=data, headers=headers)
# with open('output.mp3', 'wb') as f:
#     for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
#         if chunk:
#             f.write(chunk)

# # playsound('output.mp3')



import os
from io import BytesIO
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
import pygame

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

def text_to_speech_stream(text: str) -> BytesIO:
    # Perform the text-to-speech conversion
    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB",  # Adam pre-made voice
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Create a BytesIO object to hold the audio data in memory
    audio_stream = BytesIO()

    # Write each chunk of audio data to the stream
    for chunk in response:
        if chunk:
            audio_stream.write(chunk)

    # Reset stream position to the beginning
    audio_stream.seek(0)

    # Return the stream for further use
    return audio_stream

# Get the audio stream
audio_stream = text_to_speech_stream("This is James hello i can help yo with writing anything")

# Initialize pygame mixer
pygame.mixer.init()

# Load the audio from the BytesIO stream
audio_stream.seek(0)  # Make sure the stream is at the beginning
pygame.mixer.music.load(audio_stream, "mp3")

# Play the audio
pygame.mixer.music.play()

# Wait until the audio finishes playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(1)  # Adjust the tick rate as needed

# Quit the pygame mixer
pygame.mixer.quit()
