import pygame as pg
from textures import *
from pygame.locals import * #pour les constantes comme QUIT ou K_LEFT
import random

#importer les cartes
from cartes.carte1 import *
from cartes.carte2 import *
from cartes.carte3 import *
from cartes.carte4 import *

cartes = [carte1, carte2, carte3, carte4]

def affichage_sol(fenetre, carte, chosen_textures):
    # Clear the screen by filling it with a background color (e.g., black)
    fenetre.fill((0, 0, 0))
    
    # Update the vertical offset for water animation
    # Draw the water elements first
    for y in range(0, 13):
        for x in range(0, 20):
            if carte[y][x] == 1:
                texture = chosen_textures[y][x]
                fenetre.blit(texture, (x * 40, y * 40 ))  # Apply the vertical offset

    # Draw the other elements on top of the water
    for y in range(0, 13):
        for x in range(0, 20):
            if carte[y][x] == 2:
                pg.draw.rect(fenetre, (255, 0, 0), (x * 40, y * 40, 40, 40), 0)
            elif carte[y][x] == 3:
                pg.draw.rect(fenetre, (255, 0, 255), (x * 40, y * 40, 40, 40), 0)
            elif carte[y][x] == 4:
                texture = chosen_textures[y][x]
                fenetre.blit(texture, (x * 40, y * 40))
            elif carte[y][x] == 0:
                #choice between 4 textures
                random_texture = random.choice(ground)
                texture = chosen_textures[y][x]
                fenetre.blit(texture, (x * 40, y * 40))

    # Draw the decorations
    if carte == cartes[0]:
        for decoration in decorations1:
            texture, position = decoration
            fenetre.blit(texture, position)

    if carte == cartes[1]:
        for decoration in decorations2:
            texture, position = decoration
            fenetre.blit(texture, position)

    if carte == cartes[2]:
        for decoration in decorations3:
            texture, position = decoration
            fenetre.blit(texture, position)
        
    if carte == cartes[3]:
        for decoration in decorations4:
            texture, position = decoration
            fenetre.blit(texture, position)

def loading_screen(fenetre, loading_image):
    loading_image = pg.transform.scale(loading_image, (656, 102))
    fenetre.blit(loading_image, (72, 120))
    fenetre.blit(credits_button, (10, 10))
    alpha = 0

    while alpha < 255:
        fenetre.fill((0, 0, 0))  # Clear the screen with a black background
        loading_image.set_alpha(alpha)
        credits_button.set_alpha(alpha)
        fenetre.blit(credits_button, (10, 10))
        fenetre.blit(loading_image, (72, 120))
        pg.display.flip()
        alpha += 1.5  # Increase the alpha value to create the fade-in effect
        pg.time.delay(30)  # Adjust the delay to control the speed of the fade-in   
    pg.time.wait(1000)  # Display the loading screen for 2 seconds

def home_page(fenetre, start_button, credits_button):
    start_button = pg.transform.scale(start_button, (614, 82))
    fenetre.blit(start_button, (93, 249))

    #lancer le jeu quand on clique sur le bouton de la manette
    while True:
        pg.display.flip()
        for event in pg.event.get():
            if event.type == QUIT:
                return 'quit'
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if credits_button.get_rect(topleft=(10, 10)).collidepoint(mouse_pos):
                    print("\n\n Chef de projet: Tom \n Developer :  Tom, Théo \n Music: Thomas Brunet \n Textures: Itch.io")
            elif event.type == JOYBUTTONDOWN:
                return 'start'
            
        pg.time.Clock().tick(30)

black_surface = pg.Surface((800, 400))
black_surface.fill((0, 0, 0))

def fade_out(fenetre, fade_out_duration):
    for alpha in range(0, 256, int(255 / (fade_out_duration / 10))):
        black_surface.set_alpha(alpha)
        fenetre.blit(black_surface, (0, 0))
        pg.display.flip()
        pg.time.delay(10)


def fade_in(fenetre, fade_in_duration):
    for alpha in range(255, -1, -int(255 / (fade_in_duration / 10))):
        black_surface.set_alpha(alpha)
        fenetre.blit(black_surface, (0, 0))
        pg.display.flip()
        pg.time.delay(10)