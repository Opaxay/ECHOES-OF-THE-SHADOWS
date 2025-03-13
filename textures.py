import pygame as pg

pg.init()

pg.display.set_mode((1, 1))

spritesheet_haut = pg.image.load('textures/Zelda/Zelda_animation_haut.png').convert_alpha()
spritesheet_bas = pg.image.load('textures/Zelda/Zelda_animation_bas.png').convert_alpha()
spritesheet_droite = pg.image.load('textures/Zelda/Zelda_animation_droite.png').convert_alpha()
spritesheet_gauche = pg.image.load('textures/Zelda/Zelda_animation_gauche.png').convert_alpha()

ground = []
ground1 = pg.image.load('textures/ground/ground1.png').convert_alpha()
ground2 = pg.image.load('textures/ground/ground2.png').convert_alpha()
ground3 = pg.image.load('textures/ground/ground3.png').convert_alpha()
ground4 = pg.image.load('textures/ground/ground4.png').convert_alpha()

for i in range(1, 5):
    ground.append(pg.image.load(f'textures/ground/ground{i}.png').convert_alpha())
    ground[i - 1] = pg.transform.scale(ground[i - 1], (40, 40))  # Remplacez (40, 40) par la taille de votre rectangle
    


water_texture = pg.image.load('textures/ground/water.png').convert_alpha()
water_texture = pg.transform.scale(water_texture, (40, 40))  # Remplacez (40, 40) par la taille de votre rectangle
g_water_texture = pg.image.load('textures/ground/bordure_gauche.png').convert_alpha()
d_water_texture = pg.image.load('textures/ground/bordure_droite.png').convert_alpha()
g_water_texture = pg.transform.scale(g_water_texture, (40, 40))  # Remplacez (40, 40) par la taille de votre rectangle
d_water_texture = pg.transform.scale(d_water_texture, (40, 40))
edge_top = pg.image.load('textures/ground/bordure_haut.png')
edge_bottom = pg.image.load('textures/ground/bordure_bas.png')
edge_top = pg.transform.scale(edge_top, (40, 40))  
edge_bottom = pg.transform.scale(edge_bottom, (40, 40)) 
corner1 = pg.image.load('textures/ground/corner1.png').convert_alpha()
corner1 = pg.transform.scale(corner1, (40, 40))
corner2 = pg.image.load('textures/ground/corner2.png').convert_alpha()
corner2 = pg.transform.scale(corner2, (40, 40))
corner3 = pg.image.load('textures/ground/corner3.png').convert_alpha()
corner3 = pg.transform.scale(corner3, (40, 40))
corner4 = pg.image.load('textures/ground/corner4.png').convert_alpha()
corner4 = pg.transform.scale(corner4, (40, 40))
reversec1 = pg.image.load('textures/ground/reversec1.png').convert_alpha()
reversec1 = pg.transform.scale(reversec1, (40, 40))
reversec2 = pg.image.load('textures/ground/reversec2.png').convert_alpha()
reversec2 = pg.transform.scale(reversec2, (40, 40))
reversec3 = pg.image.load('textures/ground/reversec3.png').convert_alpha()
reversec3 = pg.transform.scale(reversec3, (40, 40))
reversec4 = pg.image.load('textures/ground/reversec4.png').convert_alpha()
reversec4 = pg.transform.scale(reversec4, (40, 40))
















arbre1 = pg.image.load('textures/Tree/Tree-1-4.png')  # Load the decoration texture
arbre1 = pg.transform.scale(arbre1, (60, 80))  # Resize the decoration texture
arbre2 = pg.image.load('textures/Tree/Tree-1-2.png')  # Load the decoration texture
arbre2 = pg.transform.scale(arbre2, (30, 40))  # Resize the decoration texture
arbre3 = pg.image.load('textures/Tree/Tree-3-4.png')  # Load the decoration texture
arbre3 = pg.transform.scale(arbre3, (60, 80))  # Resize the decoration texture
arbre_coupe = pg.image.load('textures/Tree/Stump.png')  # Load the decoration texture
arbre_coupe = pg.transform.scale(arbre_coupe, (29, 19))  # Resize the decoration texture
coffre_ouvert = pg.image.load('textures/objects/open_chest.png').convert_alpha()  # Load the decoration texture
coffre_ouvert = pg.transform.scale(coffre_ouvert, (23, 40))  # Resize the decoration texture
coffre_ferme = pg.image.load('textures/objects/locked_chest.png').convert_alpha()  # Load the decoration texture
coffre_ferme = pg.transform.scale(coffre_ferme, (24, 24))  # Resize the decoration texture
buisson1 = pg.image.load('textures/Adds/Bush-3.png').convert_alpha()  # Load the decoration texture
buisson1 = pg.transform.scale(buisson1, (40, 30))  # Resize the decoration texture
buisson2 = pg.image.load('textures/Adds/Bush-4.png').convert_alpha()  # Load the decoration texture
buisson2 = pg.transform.scale(buisson2, (40, 30))  # Resize the decoration texture
herbe1 = pg.image.load('textures/Adds/Grass-1.png').convert_alpha()  # Load the decoration texture
herbe1 = pg.transform.scale(herbe1, (40, 25))  # Resize the decoration texture
herbe2 = pg.image.load('textures/Adds/Grass-2.png').convert_alpha()  # Load the decoration texture
herbe2 = pg.transform.scale(herbe2, (40, 25))  # Resize the decoration texture
pierre1 = pg.image.load('textures/Adds/Stone-1.png').convert_alpha()  # Load the decoration texture
pierre1 = pg.transform.scale(pierre1, (50, 30))  # Resize the decoration texture
pierre2 = pg.image.load('textures/Adds/Stone-2.png').convert_alpha()  # Load the decoration texture
pierre2 = pg.transform.scale(pierre2, (30, 20))  # Resize the decoration texture
fleur = pg.image.load('textures/Adds/Flower-3.png').convert_alpha()  # Load the decoration texture
fleur = pg.transform.scale(fleur, (40, 30))  # Resize the decoration texture
loading_image = pg.image.load('textures/menu/loading_screen.png').convert()
home_image = pg.image.load('textures/menu/loading_screen.png').convert()
start_button = pg.image.load('textures/menu/start.png').convert_alpha()
credits_button = pg.image.load('textures\objects\credit.png').convert_alpha()
fence_tex = pg.image.load('textures/Big wooden fence/Big-wooden-fence-4.png').convert_alpha()
fence_tex = pg.transform.scale(fence_tex, (21, 66))  # Resize the decoration texture
cle_tex = pg.image.load('textures/objects/cle.png').convert_alpha()
cle_tex = pg.transform.scale(cle_tex, (30, 22))  # Resize the decoration texture
texture_choisi_carte1 = [[None for _ in range(20)] for _ in range(13)]

textures_1 = {
    1: [pg.transform.rotate(water_texture, angle) for angle in [-90, 90, 180]],
    4: [pg.transform.rotate(water_texture, angle) for angle in [-90, 90, 180]],
}

#carte 2
texture_choisi_carte2 = [[None for _ in range(20)] for _ in range(13)]

textures_2 = {
    1: [pg.transform.rotate(water_texture, angle) for angle in [-90, 90, 180]],
    4: [pg.transform.rotate(water_texture, angle) for angle in [-90, 90, 180]],
}

#carte 3
texture_choisi_carte3 = [[None for _ in range(20)] for _ in range(13)]

textures_3 = {
    1: [pg.transform.rotate(water_texture, angle) for angle in [-90, 90, 180]],
    4: [pg.transform.rotate(water_texture, angle) for angle in [-90, 90, 180]],
}

#carte 4
texture_choisi_carte4 = [[None for _ in range(20)] for _ in range(13)]

textures_4 = {
    1: [pg.transform.rotate(water_texture, angle) for angle in [-90, 90, 180]],
    4: [pg.transform.rotate(water_texture, angle) for angle in [-90, 90, 180]],
}


bas = [] # création d'une liste (vide) pour l'animation du bas
for x in range(0, 900, 90):#on parcour l'image de 90 en 90
    image = spritesheet_bas.subsurface(x, 0, 90, 93)# création de la variable image pour qu'elle soit un surface modifiable
    image = pg.transform.scale(image, (40, 40))# transforme l'image pour que sur la fenetre elle soit en 40*40 
    bas.append(image)#on ajoute les succession d'image dans une liste
i3_anim = 0

# Animation du personnage
droite = [] # création d'une liste (vide) pour l'animation de droite
for x in range(0, 900, 90):#on parcour l'image de 90 en 90
    image = spritesheet_droite.subsurface(x, 0, 90, 93)# création de la variable image pour qu'elle soit un surface modifiable
    image = pg.transform.scale(image, (40, 40))# transforme l'image pour que sur la fenetre elle soit en 40*40 
    droite.append(image) #on ajoute les succession d'image dans une liste
i_anim = 0 

haut = [] # création d'une liste (vide) pour l'animation du haut
for x in range(0, 900, 90):#on parcour l'image de 90 en 90
    image = spritesheet_haut.subsurface(x, 0, 90, 93)# création de la variable image pour qu'elle soit un surface modifiable
    image = pg.transform.scale(image, (40, 40))# transforme l'image pour que sur la fenetre elle soit en 40*40 
    haut.append(image)#on ajoute les succession d'image dans une liste
i2_anim = 0

gauche = [] # création d'une liste (vide) pour l'animation de gauche
for x in range(0, 900, 90):#on parcour l'image de 90 en 90
    image = spritesheet_gauche.subsurface(x, 0, 90, 93)# création de la variable image pour qu'elle soit un surface modifiable
    image = pg.transform.scale(image, (40, 40))# transforme l'image pour que sur la fenetre elle soit en 40*40 
    gauche.append(image)#on ajoute les succession d'image dans une liste
i4_anim = 0
