import pygame as pg

pg.init()

pg.display.set_mode((1, 1))

spritesheet = pg.image.load('textures/Zelda/Zelda_animation.png').convert_alpha()
ground = []
ground1 = pg.image.load('textures/ground/ground1.png').convert_alpha()
ground2 = pg.image.load('textures/ground/ground2.png').convert_alpha()
ground3 = pg.image.load('textures/ground/ground3.png').convert_alpha()
ground4 = pg.image.load('textures/ground/ground4.png').convert_alpha()

for i in range(1, 5):
    ground.append(pg.image.load(f'textures/ground/ground{i}.png').convert_alpha())
    ground[i - 1] = pg.transform.scale(ground[i - 1], (40, 40))  # Remplacez (40, 40) par la taille de votre rectangle
    


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
credits_button = pg.image.load('textures\objects\locked_chest.png').convert_alpha()

decorations = []

decorations.append((arbre1, (100, 100)))  # Example decoration
decorations.append((arbre2, (100, 200)))  # Example decoration
decorations.append((arbre3, (100, 300)))  # Example decoration
decorations.append((arbre1, (200, 100)))  # Example decoration
decorations.append((coffre_ouvert, (200, 200)))  # Example decoration
decorations.append((coffre_ferme, (230, 215)))  # Example decoration
decorations.append((buisson1, (100, (400))))  # Example decoration
decorations.append((buisson2, (150, (400))))  # Example decoration
decorations.append((herbe1, (200, (400))))  # Example decoration
decorations.append((herbe2, (250, (400))))  # Example decoration
decorations.append((pierre1, (300, (400))))  # Example decoration
decorations.append((pierre2, (350, (400))))  # Example decoration
decorations.append((fleur, (400, (400))))  # Example decoration

texture_choisi = [[None for _ in range(20)] for _ in range(13)]

textures = {
    1: [pg.transform.rotate(water_texture, angle) for angle in [-90, 90, 180]],
    4: [pg.transform.rotate(water_texture, angle) for angle in [-90, 90, 180]],
}