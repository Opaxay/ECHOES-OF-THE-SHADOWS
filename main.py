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

spritesheet = pg.image.load('textures/Zelda/Zelda_animation.png').convert_alpha()
sols_textures = pg.image.load('textures/ground/ground_texture.png').convert_alpha()
sols_textures = pg.transform.scale(sols_textures, (40, 40))  # Remplacez (40, 40) par la taille de votre rectangle
pont_texture = pg.image.load('textures/ground/bridge_texture.png').convert_alpha()
pont_texture = pg.transform.scale(pont_texture, (40, 40))  # Remplacez (40, 40) par la taille de votre rectangle
water_texture = pg.image.load('textures/ground/water.png').convert_alpha()
water_texture = pg.transform.scale(water_texture, (40, 40))  # Remplacez (40, 40) par la taille de votre rectangle
arbre1 = pg.image.load('textures/Tree/Tree-1-4.png')  # Load the decoration texture
arbre1 = pg.transform.scale(arbre1, (60, 80))  # Resize the decoration texture
arbre2 = pg.image.load('textures/Tree/Tree-1-2.png')  # Load the decoration texture
arbre2 = pg.transform.scale(arbre2, (30, 40))  # Resize the decoration texture
arbre3 = pg.image.load('textures/Tree/Tree-3-4.png')  # Load the decoration texture
arbre3 = pg.transform.scale(arbre3, (60, 80))  # Resize the decoration texture
#Variables

perso = pg.Rect(100, 320, 40, 40)  # le perso, ou plutôt sa "hitbox"
sol_afficher_bool = False
carte = cartes[0] #création de la carte avec la liste "cartes"
portail = [] #création de la liste (vide) pour les portails
eaux = [] #création de la liste (vide) pour l'eau
murs =[] #création de la liste (vide) pour les murs
decorations = [] #création de la liste (vide) pour les décorations
vitesse = 3.5
i_anim = 0 

# Initialize a storage for the chosen textures for each tile
chosen_textures = [[None for _ in range(20)] for _ in range(13)]

# Initialize texture storage
textures = {
    1: [pg.transform.rotate(water_texture, angle) for angle in [-90, 90, 180]],
    4: [pg.transform.rotate(pont_texture, angle) for angle in [90]],
    'sols': [pg.transform.rotate(sols_textures, angle) for angle in [-90, 90, 180]]
}

# Populate the lists based on the map and store the chosen textures
for y in range(0, 13):
    for x in range(0, 20):
        if carte[y][x] == 1:
            eaux.append(pg.Rect(x * 40, y * 40, 40, 40))
            chosen_textures[y][x] = random.choice(textures[1])
        elif carte[y][x] == 2:
            murs.append(pg.Rect(x * 40, y * 40, 40, 40))
        elif carte[y][x] == 3:
            portail.append(pg.Rect(x * 40, y * 40, 40, 40))
        elif carte[y][x] == 4:
            chosen_textures[y][x] = textures[4][0]
        else:
            chosen_textures[y][x] = random.choice(textures['sols'])

# Add decorations to the list with their positions
decorations.append((arbre1, (100, 100)))  # Example decoration
decorations.append((arbre2, (100, 200)))  # Example decoration
decorations.append((arbre3, (100, 300)))  # Example decoration
decorations.append((arbre1, (200, 100)))  # Example decoration

# Initialize vertical offset for water animation
water_offset = 0

def affichage_sol():
    global water_offset
    # Clear the screen by filling it with a background color (e.g., black)
    fenetre.fill((0, 0, 0))
    
    # Update the vertical offset for water animation
    water_offset = (water_offset + 1) % 40  # Adjust the speed of the flow by changing the increment value
    
    # Draw the water elements first
    for y in range(0, 13):
        for x in range(0, 20):
            if carte[y][x] == 1:
                texture = chosen_textures[y][x]
                fenetre.blit(texture, (x * 40, y * 40 + water_offset - 40))  # Apply the vertical offset

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
                texture = chosen_textures[y][x]
                fenetre.blit(texture, (x * 40, y * 40))

    # Draw the decorations
    for decoration in decorations:
        texture, position = decoration
        fenetre.blit(texture, position)



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


    affichage_sol()


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
