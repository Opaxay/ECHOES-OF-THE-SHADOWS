import pygame as pg #pour simplifier l'écriture = pg -long que pygame
from pygame.locals import * #pour les constantes comme QUIT ou K_LEFT

from liste_cartes import cartes #pour appeller toutes les cartes on créé notre propre bibliothèque

# on lance pygame
pg.init()

#Réglages

LARGEUR, HAUTEUR = 800, 480 #Dimensions
fenetre = pg.display.set_mode((LARGEUR, HAUTEUR))#, FULLSCREEN) # fenêtre d'affichage de dimension LARGEUR, HAUTEUR
pg.display.set_caption("Zelda Théo Nicolas")#nom de la fenetre
horloge = pg.time.Clock() #pour simplifier plus tard pour la commande des images par seconde
# images
spritesheet = pg.image.load('Zelda_animation.png').convert_alpha()
#texturesheet = pg.image.load('tp_textures_1200.jpg').convert()

#Variables
perso = pg.Rect(100, 320, 40, 40)  # le perso, ou plutôt sa "hitbox"

carte = cartes[0] #création de la carte avec la liste "cartes"
#Théo
portail = [] #création de la liste (vide) pour les portails
eaux = [] #création de la liste (vide) pour l'eau
murs =[] #création de la liste (vide) pour les murs

for y in range(0, 8): # on parcourt les ligne de liste
    for x in range(0, 10): # on parcourt les element des ligne dans la liste
        if carte[y][x] == 1: #on parcourt la liste pour chaque 1 qui correspond a de l'eau
            eaux.append(pg.Rect(x * 40, y * 40, 40, 40))# on rajoute dans la liste "eaux" des rectangle de taille 40*40
        elif carte[y][x] == 2:  #on parcourt la liste pour chaque 2 qui correspond aux murs
            murs.append(pg.Rect(x * 40, y * 40, 40, 40))# on rajoute dans la liste "murs" des rectangle de taille 40*40
        elif carte[y][x] == 3:  #on parcourt la liste pour chaque 3 qui correspond aux portails
            portail.append(pg.Rect(x * 40, y * 40, 40, 40))# on rajoute dans la liste "portail" des rectangle de taille 40*40
            
def affichage():
    # on dessine
    for y in range(0, 8):
        for x in range(0, 10):
            if carte[y][x] == 1: 
                pg.draw.rect(fenetre, (0, 255, 255), (x * 40, y * 40, 40, 40), 0) #on dessine un rectangle bleu de taille 40*40
            elif carte[y][x] == 2:
                pg.draw.rect(fenetre, (255, 0, 0), (x * 40, y * 40, 40, 40), 0) #on dessine un rectangle rouge de taille 40*40
            elif carte[y][x] == 3:
                pg.draw.rect(fenetre, (255, 0, 255), (x * 40, y * 40, 40, 40), 0)#on dessine un rectangle violet de taille 40*40
            else:
                pg.draw.rect(fenetre, (0, 128, 0), (x * 40, y * 40, 40, 40), 0)#on dessine un rectangle vert de taille 40*40
    # perso
    #pg.draw.rect(fenetre, (255, 255, 0), perso, 0)


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
    
vitesse = 10 #vitesse du perso initialisé a 10
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

#Boucle perpétuelle
continuer = True

while continuer:
    # 42 images par seconde
    horloge.tick(42)


    fenetre.blit(image, perso)# affiche l'image et le perso sur la fenetre
    pg.display.flip()
    # on bascule l'affichage, une seule fois
    # par passage dans la boucle perpétuelle
    affichage()

    #collision avec l'eau?
    if collision_eau():
        vitesse = 2 #on change la vitesse pour que le perso soit ralenti
    else:
        vitesse = 10
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

    if touches[K_RIGHT]:
        perso.x += vitesse #le pero avance 
        if perso.left >= LARGEUR: # on dépasse les limites de la carte?
            perso.right = 0 #on revient a gauche
        for mur in murs : 
            if perso.colliderect(mur):#collision avec les murs?
                perso.x -= vitesse # effet de surplace en revenant en arriere de la meme vitesse que celle avancée
        # animation
        i_anim += 1 # on passe a l'image de l'animation suivante
        if i_anim >= len(droite):
            i_anim = 0 #si on dépasse toute les animation on revient à la première
        image = droite[i_anim] # affiche l'image de l'animation de droite
        
    if touches[K_LEFT]:
        perso.x -= vitesse #le pero avance
        if perso.right <= 0: # on dépasse les limites de la carte?
            perso.left = LARGEUR #on revient a droite
        for mur in murs :
            if perso.colliderect(mur): #collision avec les murs?
                perso.x += vitesse # effet de surplace en revenant en arriere de la meme vitesse que celle avancée
        # animation
        i4_anim += 1 # on passe a l'image de l'animation suivante
        if i4_anim >= len(gauche):
            i4_anim = 0 #si on dépasse toute les animation on revient à la première
        image = gauche[i4_anim] # affiche l'image de l'animation de gauche

    if touches[K_UP]:
        perso.y -= vitesse #le pero avance
        if perso.bottom <= 0: # on dépasse les limites de la carte?
            perso.top = HAUTEUR #on revient en bas
        for mur in murs :
            if perso.colliderect(mur): #collision avec les murs?
                perso.y += vitesse # effet de surplace en revenant en arriere de la meme vitesse que celle avancée
        # animation
        i2_anim += 1 # on passe a l'image de l'animation suivante
        if i2_anim >= len(haut):
            i2_anim = 0  #si on dépasse toute les animation on revient à la première
        image = haut[i2_anim] # affiche l'image de l'animation du haut
        
    if touches[K_DOWN]:
        perso.y += vitesse #le pero avance
        if perso.top >= HAUTEUR: # on dépasse les limites de la carte?
            perso.bottom = 0 #on revient en haut
        for mur in murs : 
            if perso.colliderect(mur):#collision avec les murs?
                perso.y -= vitesse # effet de surplace en revenant en arriere de la meme vitesse que celle avancée
        # animation
        i3_anim += 1 # on passe a l'image de l'animation suivante
        if i3_anim >= len(bas):
            i3_anim = 0 #si on dépasse toute les animation on revient à la première
        image = bas[i3_anim]# affiche l'image de l'animation du bas

# on stoppe pygame
pg.quit()
