import pygame as pg #pour simplifier l'écriture = pg -long que pygame
from pygame.locals import * #pour les constantes comme QUIT ou K_LEFT
import random

from cartes import cartes #pour appeller toutes les cartes on créé notre propre bibliothèque

# on lance pygame
pg.init()

# Module pour manettes
pg.joystick.init()

# Vérifier si des manettes sont connectées
if pg.joystick.get_count() > 0:
    joystick = pg.joystick.Joystick(0)  # Utiliser la première manette détectée
    joystick.init()
    print(f"Manette connectée : {joystick.get_name()}")
else:
    print("Aucune manette détectée.")




#Réglages

LARGEUR, HAUTEUR = 800, 480 #Dimensions
fenetre = pg.display.set_mode((LARGEUR, HAUTEUR))#, FULLSCREEN) # fenêtre d'affichage de dimension LARGEUR, HAUTEUR
pg.display.set_caption("Zelda")#nom de la fenetre
horloge = pg.time.Clock() #pour simplifier plus tard pour la commande des images par seconde


# Charger les Textures

spritesheet = pg.image.load('Zelda_animation.png').convert_alpha()
sols_textures = pg.image.load('ground_texture.png').convert_alpha()
sols_textures = pg.transform.scale(sols_textures, (40, 40))  # Remplacez (40, 40) par la taille de votre rectangle
pont_texture = pg.image.load('bridge_texture.png').convert_alpha()
pont_texture = pg.transform.scale(pont_texture, (40, 40))  # Remplacez (40, 40) par la taille de votre rectangle
water_texture = pg.image.load('water.png').convert_alpha()
water_texture = pg.transform.scale(water_texture, (40, 40))  # Remplacez (40, 40) par la taille de votre rectangle


#Variables

perso = pg.Rect(100, 320, 40, 40)  # le perso, ou plutôt sa "hitbox"
sol_afficher_bool = False
carte = cartes[0] #création de la carte avec la liste "cartes"
portail = [] #création de la liste (vide) pour les portails
eaux = [] #création de la liste (vide) pour l'eau
murs =[] #création de la liste (vide) pour les murs
vitesse = 3.5


for y in range(0, 13): # on parcourt les ligne de liste
    for x in range(0, 20): # on parcourt les element des ligne dans la liste
        if carte[y][x] == 1: #on parcourt la liste pour chaque 1 qui correspond a de l'eau
            eaux.append(pg.Rect(x * 40, y * 40, 40, 40))# on rajoute dans la liste "eaux" des rectangle de taille 40*40
        elif carte[y][x] == 2:  #on parcourt la liste pour chaque 2 qui correspond aux murs
            murs.append(pg.Rect(x * 40, y * 40, 40, 40))# on rajoute dans la liste "murs" des rectangle de taille 40*40
        elif carte[y][x] == 3:  #on parcourt la liste pour chaque 3 qui correspond aux portails
            portail.append(pg.Rect(x * 40, y * 40, 40, 40))# on rajoute dans la liste "portail" des rectangle de taille 40*40


i_anim = 0 
def affichage_sol():
    # on dessine
    for y in range(0, 13):
        for x in range(0, 20):
            if carte[y][x] == 1: 
                angle_rotation = random.choice([-90, 90, 180])
                texture = pg.transform.rotate(water_texture, angle_rotation)
                fenetre.blit(texture, (x * 40, y * 40))
            elif carte[y][x] == 2:
                pg.draw.rect(fenetre, (255, 0, 0), (x * 40, y * 40, 40, 40), 0) #on dessine un rectangle rouge de taille 40*40
            elif carte[y][x] == 3:
                pg.draw.rect(fenetre, (255, 0, 255), (x * 40, y * 40, 40, 40), 0)#on dessine un rectangle violet de taille 40*40
            elif carte[y][x] == 4:
                texture = pg.transform.rotate(pont_texture, 0)
                fenetre.blit(pont_texture, (x * 40, y * 40))

            else:
                angle_rotation = random.choice([-90, 90, 180])
                texture = pg.transform.rotate(sols_textures, angle_rotation)
                fenetre.blit(texture, (x * 40, y * 40))



# POUR L'ANIMATION DU PERSO

droite = [] # création d'une liste (vide) pour l'animation de droite
for x in range(0, 900, 90):#on parcour l'image de 90 en 90
    image = spritesheet.subsurface(x, 690, 90, 90)# création de la variable image pour qu'elle soit un surface modifiable
    image = pg.transform.scale(image, (40, 40))# transforme l'image pour que sur la fenetre elle soit en 40*40 
    droite.append(image) #on ajoute les succession d'image dans une liste
i_anim = 0 

haut = [] # création d'une liste (vide) pour l'animation du haut
for x in range(0, 900, 90):#on parcour l'image de 90 en 90
    image = spritesheet.subsurface(x, 585, 90, 90)# création de la variable image pour qu'elle soit un surface modifiable
    image = pg.transform.scale(image, (40, 40))# transforme l'image pour que sur la fenetre elle soit en 40*40 
    haut.append(image)#on ajoute les succession d'image dans une liste
i2_anim = 0

bas = [] # création d'une liste (vide) pour l'animation du bas
for x in range(0, 900, 90):#on parcour l'image de 90 en 90
    image = spritesheet.subsurface(x, 400, 90, 90)# création de la variable image pour qu'elle soit un surface modifiable
    image = pg.transform.scale(image, (40, 40))# transforme l'image pour que sur la fenetre elle soit en 40*40 
    bas.append(image)#on ajoute les succession d'image dans une liste
i3_anim = 0


gauche = [] # création d'une liste (vide) pour l'animation de gauche
for x in range(0, 900, 90):#on parcour l'image de 90 en 90
    image = spritesheet.subsurface(x, 490, 90, 90)# création de la variable image pour qu'elle soit un surface modifiable
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

    if sol_afficher_bool is not True:
        affichage_sol()
        print('prout')
        sol_afficher_bool = True

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
        for mur in murs:
            if perso.colliderect(mur):  # Collision avec un mur
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
        for mur in murs:
            if perso.colliderect(mur):  # Collision avec un mur
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
