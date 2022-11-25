#titlescreen animation

from genderSelection import *
from animation import animate
import pygame
from pygame import mixer

pygame.mixer.init()

mixer.music.load(r'sfx\titlescreen.mp3')
mixer.music.set_volume(0.5)

sfx = pygame.mixer.Sound(r'sfx\select.mp3')



for x in range(0,7):
    animate(f"titlescreen/loading/{x}.txt")
mixer.music.play()

anyKey = input("Press any key to continue...")
sfx.play()
mixer.music.stop()

genderSelect()