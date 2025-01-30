import os
import pygame as pg
from textures import bas

os.environ['SDL_VIDEO_CENTERED'] = '1'
LARGEUR, HAUTEUR = 800, 480
fenetre = pg.display.set_mode((LARGEUR, HAUTEUR))
horloge = pg.time.Clock() 

icone = pg.image.load('textures/objects/locked_chest.png')
pg.display.set_icon(icone)
pg.display.set_caption("ECHOES OF THE SHADOWS")

perso = pg.Rect(50, 250, 40, 40)  # le perso, ou plutôt sa "hitbox"
vitesse = 2.5
i_anim = 0 
portail = [] #création de la liste (vide) pour les portails
murs =[] #création de la liste (vide) pour les murs
image = bas[0]
