import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('Musica.wav')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()
pygame.event.wait()