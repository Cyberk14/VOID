from pyht import Client
from pyht.client import TTSOptions
import os

client = Client(
    user_id="Didb3xzYmNUM5QH4nZyxzoSIlio2",
    api_key="82cbdc7000a848739a86affc988171cb",
)
 
import pygame
from io import BytesIO

# Assuming you have already imported necessary libraries and defined the TTS client
options = TTSOptions(voice="s3://voice-cloning-zero-shot/d9ff78ba-d016-47f6-b0ef-dd630f59414e/female-cs/manifest.json")

# Assuming client is an instance of your TTS client class
audio_chunks = []
for chunk in client.tts("Can you tell me your account email or, ah your phone number?", options):
    audio_chunks.append(chunk)

# Concatenate audio chunks into a single byte stream
audio_data = b"".join(audio_chunks)

# Play the audio data using pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(BytesIO(audio_data))
pygame.mixer.music.play()

# Wait until the audio finishes playing
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Adjust the tick rate as needed

# Clean up pygame resources
pygame.mixer.quit()
pygame.quit()
