import pygame

def speak():
    pygame.init()
    pygame.mixer.init()
    # audio_stream.seek(0)  # Make sure the stream is at the beginning
    pygame.mixer.music.load("D:\\New folder\\VOID\\agent_voice.mp3", "mp3")

    pygame.mixer.music.play()

    # Use a ticker to prevent high CPU usage
    clock = pygame.time.Clock()

    while pygame.mixer.music.get_busy():
        clock.tick(1)  # Adjust the tick rate as needed

    pygame.mixer.quit()
    pygame.quit()


