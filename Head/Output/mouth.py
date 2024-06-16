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

def speak(text: str):
    # Get the audio stream
    audio_stream = text_to_speech_stream(text=text)

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

speak("hello i came to save the world..")
