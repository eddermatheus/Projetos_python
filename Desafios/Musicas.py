import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("Desafios/Musica.mp3")  # ou "Desafios\\Musica.mp3"
pygame.mixer.music.play()

while True : 
 tecla = input("Digite 'P' para parar a música: ")
 if tecla.lower() == "p":
    pygame.mixer.music.stop()
    print("Música parada!")
    break

pygame.quit()
