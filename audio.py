
import pygame
def TTS_mem():
    
    pygame.mixer.init()
    # 
    # audio_stream.seek(0)  # Make sure the stream is at the beginning
    pygame.mixer.music.load("D:\\New folder\\VOID\\Pia.wav", "wav")

    pygame.mixer.music.play()

    # Use a ticker to prevent high CPU usage
    clock = pygame.time.Clock()

    while pygame.mixer.music.get_busy():
        clock.tick(1)  # Adjust the tick rate as needed

        print('---------------------')
        

    print("done")
    pygame.mixer.quit()
    pygame.quit()

print("starting")
with open("D:\\New folder\\VOID\\output.mp3", 'w') as file:
    file.write('hello')
TTS_mem()
print("ended....")

for i in range(3):
    print("fuck youuuu")
