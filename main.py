import pygame as pg #pour simplifier l'écriture = pg -long que pygame
from pygame.locals import * #pour les constantes comme QUIT ou K_LEFT
import random
from textures import *
from cartes import cartes #pour appeller toutes les cartes on créé notre propre bibliothèque
from affichage import *
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

pg.init()
pg.mixer.init()
pg.joystick.init()

# Vérifier si des manettes sont connectées
if pg.joystick.get_count() > 0:
    joystick = pg.joystick.Joystick(0)  # Utiliser la première manette détectée
    joystick.init()
    print(f"Manette connectée : {joystick.get_name()}")
else:
    print("Aucune manette détectée.")

# Parametres de la fenetre

LARGEUR, HAUTEUR = 800, 480 #Dimensions
fenetre = pg.display.set_mode((LARGEUR, HAUTEUR)) # fenêtre d'affichage de dimension LARGEUR, HAUTEUR
pg.display.set_caption("Zelda")#nom de la fenetre
horloge = pg.time.Clock() #pour simplifier plus tard pour la commande des images par seconde


# Parametres du jeu

perso = pg.Rect(100, 320, 40, 40)  # le perso, ou plutôt sa "hitbox"
carte = cartes[0] #création de la carte avec la liste "cartes"
portail = [] #création de la liste (vide) pour les portails
eaux = [] #création de la liste (vide) pour l'eau
murs =[] #création de la liste (vide) pour les murs
vitesse = 3.5 
i_anim = 0 

# Chargements des carrés de textures pour la carte
for y in range(0, 13):
    for x in range(0, 20):
        if carte[y][x] == 1:
            eaux.append(pg.Rect(x * 40, y * 40, 40, 40))
            texture_choisi[y][x] = random.choice(textures[1])
        elif carte[y][x] == 2:
            murs.append(pg.Rect(x * 40, y * 40, 40, 40))
        elif carte[y][x] == 3:
            portail.append(pg.Rect(x * 40, y * 40, 40, 40))
        elif carte[y][x] == 4:
            texture_choisi[y][x] = textures[4][0]
        else:
            texture_choisi[y][x] = random.choice(ground)

# Chargement des musiques
pg.mixer.music.load('music/menu.mp3') 
game_music = 'music/in_game.mp3' 
pg.mixer.music.play(-1) 

# Affichage de l'écran de chargement
loading_screen(fenetre, loading_image)
# Affichage de l'écran d'accueil
action = home_page(fenetre, start_button, credits_button)

# Gérer les actions de l'écran d'accueil
if action == 'quit':
    pg.quit()
    exit()

elif action == 'start':
    pg.mixer.music.fadeout(3000)  # Fade out the current music over 2 seconds
    
    pg.mixer.music.load(game_music)  # Load the game music
    pg.mixer.music.play(-1)  # Play the game music in a loop

    fade_out(fenetre, 2000)



# POUR L'ANIMATION DU PERSO

droite = [] # création d'une liste (vide) pour l'animation de droite
for x in range(0, 900, 90):#on parcour l'image de 90 en 90
    image = spritesheet.subsurface(x, 678, 90, 90)# création de la variable image pour qu'elle soit un surface modifiable
    image = pg.transform.scale(image, (40, 40))# transforme l'image pour que sur la fenetre elle soit en 40*40 
    droite.append(image) #on ajoute les succession d'image dans une liste
i_anim = 0 

haut = [] # création d'une liste (vide) pour l'animation du haut
for x in range(0, 900, 90):#on parcour l'image de 90 en 90
    image = spritesheet.subsurface(x, 573, 90, 90)# création de la variable image pour qu'elle soit un surface modifiable
    image = pg.transform.scale(image, (40, 40))# transforme l'image pour que sur la fenetre elle soit en 40*40 
    haut.append(image)#on ajoute les succession d'image dans une liste
i2_anim = 0

bas = [] # création d'une liste (vide) pour l'animation du bas
for x in range(0, 900, 90):#on parcour l'image de 90 en 90
    image = spritesheet.subsurface(x, 388, 90, 90)# création de la variable image pour qu'elle soit un surface modifiable
    image = pg.transform.scale(image, (40, 40))# transforme l'image pour que sur la fenetre elle soit en 40*40 
    bas.append(image)#on ajoute les succession d'image dans une liste
i3_anim = 0


gauche = [] # création d'une liste (vide) pour l'animation de gauche
for x in range(0, 900, 90):#on parcour l'image de 90 en 90
    image = spritesheet.subsurface(x, 478, 90, 90)# création de la variable image pour qu'elle soit un surface modifiable
    image = pg.transform.scale(image, (40, 40))# transforme l'image pour que sur la fenetre elle soit en 40*40 
    gauche.append(image)#on ajoute les succession d'image dans une liste
i4_anim = 0
    

#Gérer les Collisions

#collision eau?
def collision_eau():#création de la fonction de collision pour l'eau
    for eau in eaux:
        if perso.colliderect(eau):#si il y a collision renvoie un booléen
            return True 
    return False
#collision portail?
def collision_portail(): #création de la fonction de collision pour les portails
    for port in portail:
        if perso.colliderect(port): #si il y a collision renvoie un booléen
            return True 
    return False


#Boucle du jeu 
continuer = True

while continuer:
    horloge.tick(60)
    

    # Dessine le personnage
    fenetre.blit(image, perso)

    # Met à jour l'affichage
    pg.display.flip()


    fenetre.blit(image, perso)# affiche l'image et le perso sur la fenetre
    pg.display.flip()
    # on bascule l'affichage, une seule fois
    # par passage dans la boucle perpétuelle


    affichage_sol(fenetre, carte, texture_choisi) #on appelle la fonction affichage_sol pour afficher la carte

    #collision avec les portails?
    if collision_portail():
        carte = cartes[1] #on change de carte

    #Je parcours tous les événements
    for e in pg.event.get():
        if e.type == QUIT: #quitter le jeu
            continuer = False
    # liste des touches
    touches = pg.key.get_pressed()
    if touches[K_ESCAPE]:
        print("touche Escape, on sort") #quitter le jeu
        continuer = False

        # Gestion des entrées clavier, souris et manette
    if joystick:  # Vérifier si une manette est connectée
        # Lire les axes de la manette (valeurs entre -1.0 et 1.0)
        x_axis = joystick.get_axis(0)  # Axe horizontal (gauche-droite)
        y_axis = joystick.get_axis(1)  # Axe vertical (haut-bas)

        # Seuil pour éviter les petites variations (zone morte)
        dead_zone = 0.1
        if abs(x_axis) < dead_zone:
            x_axis = 0
        if abs(y_axis) < dead_zone:
            y_axis = 0

        # Convertir les axes en déplacement
        joystick_dx = int(x_axis * vitesse)
        joystick_dy = int(y_axis * vitesse)
    else:
        joystick_dx = joystick_dy = 0  # Pas de manette

    # Lire les entrées clavier
    dx = dy = 0  # Déplacement clavier par défaut
    if touches[K_d]:
        dx += vitesse 
    if touches[K_q]:
        dx -= vitesse 
    if touches[K_z]:
        dy -= vitesse 
    if touches[K_s]:
        dy += vitesse 

    # Combiner les entrées de la manette et du clavier
    final_dx = dx + joystick_dx
    final_dy = dy + joystick_dy

    # Appliquer les déplacements horizontaux
    if final_dx != 0:
        perso.x += final_dx
        if perso.left >= LARGEUR:  # Dépasse les limites de la carte ?
            perso.right = 0  # Revenir à gauche
        elif perso.right <= 0:  # Dépasse par la gauche ?
            perso.left = LARGEUR  # Revenir à droite
        for eau in eaux:
            if perso.colliderect(eau):  # Collision avec un mur
                perso.x -= final_dx  # Annuler le déplacement

        # Animation en fonction de la direction
        if final_dx > 0:  # Droite
            i_anim += 1
            if i_anim >= len(droite):
                i_anim = 0
            image = droite[i_anim]
        elif final_dx < 0:  # Gauche
            i4_anim += 1
            if i4_anim >= len(gauche):
                i4_anim = 0
            image = gauche[i4_anim]

    # Appliquer les déplacements verticaux
    if final_dy != 0:
        perso.y += final_dy
        if perso.top >= HAUTEUR:  # Dépasse les limites de la carte ?
            perso.bottom = 0  # Revenir en haut
        elif perso.bottom <= 0:  # Dépasse par le haut ?
            perso.top = HAUTEUR  # Revenir en bas
        for eau in eaux:
            if perso.colliderect(eau):  # Collision avec un mur
                perso.y -= final_dy  # Annuler le déplacement

        # Animation en fonction de la direction
        if final_dy < 0:  # Haut
            i2_anim += 1
            if i2_anim >= len(haut):
                i2_anim = 0
            image = haut[i2_anim]
        elif final_dy > 0:  # Bas
            i3_anim += 1
            if i3_anim >= len(bas):
                i3_anim = 0
            image = bas[i3_anim]


# on stoppe pygame
pg.quit()
