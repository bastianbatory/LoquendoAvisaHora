import pygame
import os
import sys


args = sys.argv
date = args[1]

dir = os.path.dirname(os.path.abspath(__file__))
#D:\AlarmasBot

sonido = (dir + '\\audio\\' + date +'.wav')
pygame.mixer.init()
pygame.mixer.music.load(sonido)

pygame.mixer.music.set_volume(0.25)  
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)