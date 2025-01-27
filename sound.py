import pygame as pg

pg.mixer.music.load('sounds/music/menu.mp3') 
game_music = 'sounds/music/in_game.mp3' 
pg.mixer.music.play(-1) 
footstep_sounds = [
    pg.mixer.Sound('sounds\effects\grasswalk\GRASS - Walk 1.wav'),
    pg.mixer.Sound('sounds\effects\grasswalk\GRASS - Walk 2.wav'),
    pg.mixer.Sound('sounds\effects\grasswalk\GRASS - Walk 3.wav'),
    pg.mixer.Sound('sounds\effects\grasswalk\GRASS - Walk 4.wav'),
    pg.mixer.Sound('sounds\effects\grasswalk\GRASS - Walk 5.wav'),
    pg.mixer.Sound('sounds\effects\grasswalk\GRASS - Walk 6.wav'),
    pg.mixer.Sound('sounds\effects\grasswalk\GRASS - Walk 7.wav'),
    pg.mixer.Sound('sounds\effects\grasswalk\GRASS - Walk 8.wav'),
]

for sound in footstep_sounds:
    sound.set_volume(0.15)