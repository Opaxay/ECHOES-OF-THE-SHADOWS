import pygame as pg 
from pygame.locals import * #pour les constantes comme QUIT ou K_LEFT
import random
from textures import *
from affichage import *
import os
import sys
from settings import * 
from sound import * 
#importer les 4 cartes
from cartes.carte1 import carte1, texture_choisi_carte1, eaux1
from cartes.carte2 import carte2, texture_choisi_carte2, eaux2
from cartes.carte3 import carte3, texture_choisi_carte3, eaux3
from cartes.carte4 import carte4, texture_choisi_carte4, eaux4
import time

PLAYER_MODE = True #Desactivé il enleve toute l'animation au debut pour pouvoir relacer le jeu plus rapidement quand on est entrain de developper 

en_jeu = False

eaux = [eaux1, eaux2, eaux3, eaux4]

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

tick = 60

police = pg.font.Font(None, 36)  

cartes = [carte1, carte2, carte3, carte4]

def relancer_jeu():
    global carte, perso, CLE_TROUVER, LIMIT_CARTE, timer, cle, coffre1, fences
    carte = cartes[0]
    perso = pg.Rect(170, 220, 40, 40)
    CLE_TROUVER = False
    LIMIT_CARTE = 155
    timer = tick * 60

    cle = []
    coffre1 = []
    fences = []

    cle.append({'texture': cle_tex, "rect": pg.Rect(300, 300, 20, 12), "cle": False})
    coffre1.append({'texture': coffre_ferme, "rect": pg.Rect(600, 300, 40, 40), "ouvert": False})
    fences.append({'texture': fence_tex, "rect": pg.Rect(100, 120, 21, 66)})
    fences.append({'texture': fence_tex, "rect": pg.Rect(100, 186, 21, 66)})
    fences.append({'texture': fence_tex, "rect": pg.Rect(100, 252, 21, 66)})
    fences.append({'texture': fence_tex, "rect": pg.Rect(100, 318, 21, 66)})
    fences.append({'texture': fence_tex, "rect": pg.Rect(100, 384, 21, 66)})

    if PLAYER_MODE:
        # Affichage de l'écran de chargement
        loading_screen(fenetre, loading_image)
        # Affichage de l'écran d'accueil
        action = home_page(fenetre, start_button, credits_button)
        
        # Gérer les actions de l'écran d'accueil
        if action == 'quit':
            pg.quit()
            exit()

        elif action == 'start':
            start_button.fill((0, 0, 0, 0))
            pg.mixer.music.fadeout(3000)
            fade_out(fenetre, 1)
            
            
            pg.mixer.music.load(game_music)  # Load the game music
            pg.mixer.music.play(-1)  # Play the game music in a loop

       


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

    if not en_jeu:
        relancer_jeu()
        en_jeu = True

    #lancer le jeu


    horloge.tick(tick)
    
    
    # Dessine le personnage
    fenetre.blit(image, perso)

    # Met à jour l'affichage
    pg.display.flip()
    if carte == cartes[0]: # Si on est sur la carte 1
        affichage_sol(fenetre, carte, texture_choisi_carte1) #on appelle la fonction affichage_sol pour afficher la carte
    elif carte == cartes[1]: # Si on est sur la carte 2
        affichage_sol(fenetre, carte, texture_choisi_carte2) #on appelle la fonction affichage_sol pour afficher la carte
    elif carte == cartes[2]: # Si on est sur la carte 3
        affichage_sol(fenetre, carte, texture_choisi_carte3) #on appelle la fonction affichage_sol pour afficher la carte
    elif carte == cartes[3]: # Si on est sur la carte 4
        affichage_sol(fenetre, carte, texture_choisi_carte4) #on appelle la fonction affichage_sol pour afficher la carte

    timer -= 1
    texte = police.render(f"00:{timer // 60}", True, (255,255,255))
    texte_rect = texte.get_rect(center=(LARGEUR - 35, 20))
    fenetre.blit(texte, texte_rect)
    
    #avoir les coordonné quand je click avec la souris
    if pg.mouse.get_pressed()[0]:
        print(pg.mouse.get_pos())

    #collision avec les portails?
    if collision_portail():
        pass

    #Je parcours tous les événements
    for e in pg.event.get():
        if e.type == QUIT: #quitter le jeu
            continuer = False
    # liste des touches
    touches = pg.key.get_pressed()
    if touches[K_ESCAPE]:
        print("touche Escape, on sort") #quitter le jeu
        continuer = False
    try:
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
    except:
        pass

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
    try: 
        final_dx = dx + joystick_dx
        final_dy = dy + joystick_dy
    except:
        final_dx = dx
        final_dy = dy


    # Appliquer les déplacements horizontaux
    if final_dx != 0:
        perso.x += final_dx
        if perso.left >= LARGEUR:  # Dépasse a droite ? (teleportation)
            if carte == cartes[0]: # Si on est sur la carte 1
                carte = cartes[1]
                perso.right = 0
            elif carte == cartes[2]: # Si on est sur la carte 3
                carte = cartes[3]
                perso.right = 0
        
        elif perso.left >= LARGEUR - 40: # Dépasse par la droite ? (collision)
            if carte == cartes[1]: # Si on est sur la carte 2
                perso.x -= final_dx
            elif carte == cartes[3]: # Si on est sur la carte 4
                perso.x -= final_dx
        

        elif perso.right <= 0:  # Dépasse par la gauche ? (teleportation)
            if carte == cartes[1]: # Si on est sur la carte 2
                carte = cartes[0]
                perso.left = LARGEUR
            elif carte == cartes[3]: # Si on est sur la carte 4
                carte = cartes[2]
                perso.left = LARGEUR
        
        elif perso.right <= 40:  # Dépasse par la gauche ? (collision)
            if carte == cartes[2]: # Si on est sur la carte 3
                perso.x -= final_dx

        elif perso.right <= LIMIT_CARTE:  # Dépasse par la gauche ? (collision)
            if carte == cartes[0]: # Si on est sur la carte 1
                perso.x -= final_dx

        try:
            if carte[perso.y // 40][perso.x // 40] == 0:
                random.choice(footstep_sounds).play()
        except IndexError:
            'Coordonnées erronées'
        
        for eau in eaux[cartes.index(carte)]:
            if perso.colliderect(eau):  # Collision avec l'eau
                perso.x -= final_dx
                
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
        if perso.top >= HAUTEUR:  # Dépasse par le bas ? (teleportation)
            if carte == cartes[2]: # Si on est sur la carte 3
                carte = cartes[0]
                perso.bottom = 0
            elif carte == cartes[3]: # Si on est sur la carte 4
                carte = cartes[1]
                perso.bottom = 0

        elif perso.top >= HAUTEUR - 40:  # Dépasse par le bas ?
            if carte == cartes[0]: # Si on est sur la carte 1
                perso.y -= final_dy
            elif carte == cartes[1]: # Si on est sur la carte 2
                perso.y -= final_dy
            
            
        elif perso.bottom <= 0:  # Dépasse par le haut ?
            if carte == cartes[0]: # Si on est sur la carte 1
                carte = cartes[2]
                perso.bottom = HAUTEUR
            elif carte == cartes[1]: # Si on est sur la carte 2
                carte = cartes[3]
                perso.bottom = HAUTEUR

        elif perso.bottom <= 40:  # Dépasse par bas ?
            if carte == cartes[2]: # Si on est sur la carte 3
                perso.y -= final_dy
            elif carte == cartes[3]: # Si on est sur la carte 4
                perso.y -= final_dy

        try:
            if carte[perso.y // 40][perso.x // 40] == 0:
                random.choice(footstep_sounds).play()
        except IndexError:
            'Coordonnées erronées'

        #changer la liste d'eaux en fonction de la carte
        
        for eau in eaux[cartes.index(carte)]:
            if perso.colliderect(eau):  # Collision avec l'eau
                perso.y -= final_dy

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

    for cles in cle:
        if not cles['cle'] and perso.colliderect(cles['rect']):
            CLE_TROUVER = True
            cles['cle'] = True
            cle.remove(cles)
        elif carte == cartes[3]:
            fenetre.blit(cle[0]['texture'], cle[0]['rect'].topleft)
            
    for coffre in coffre1:
        
        if CLE_TROUVER:
            if not coffre['ouvert'] and perso.colliderect(coffre1[0]['rect']):
                coffre1[0]['texture'] = coffre_ouvert
                coffre1[0]['ouvert'] = True
                LIMIT_CARTE = 0
                fences.pop(2)
        if carte == cartes[0]:
            fenetre.blit(coffre1[0]['texture'], coffre1[0]['rect'].topleft)
            for fence in fences:
                fenetre.blit(fence['texture'], fence['rect'].topleft)

        if carte == cartes[0]:
            #blit every fences
            for fence in fences:
                fenetre.blit(fence['texture'], fence['rect'].topleft)

    affichage_decorations(fenetre, carte)

    if timer == 0:
        en_jeu = False
    
# on stoppe pygame
pg.quit()
