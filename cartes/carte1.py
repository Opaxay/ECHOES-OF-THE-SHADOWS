from textures import *
import random

portail = [] #création de la liste (vide) pour les portails
eaux1 = [] #création de la liste (vide) pour l'eau
murs =[] #création de la liste (vide) pour les murs
bordure = []
decoration_rects1 = []

carte1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 20, 22, 16, 16, 16, 23, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 11, 0, 0, 0, 13, 16],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 11, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 20, 1, 11, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 22,  14, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 11, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 11, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 11, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 11, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 11, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 11, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 1, 11, 0, 0, 0, 0, 0, 0],]



decorations1 = []

decorations1.append((fleur, (400, 200)))
decorations1.append((fleur, (200, 190)))
decorations1.append((fleur, (220, 170)))
decorations1.append((fleur, (230, 195)))
decorations1.append((fleur, (190, 400)))
decorations1.append((fleur, (340, 420)))
decorations1.append((fleur, (320, 50)))

decorations1.append((arbre1, (0, -30)))
decorations1.append((arbre1, (30, -30)))
decorations1.append((arbre1, (40, -30)))
decorations1.append((arbre1, (75, -30)))
decorations1.append((arbre1, (120, -30)))
decorations1.append((arbre1, (180, -30)))
decorations1.append((arbre1, (120, -20)))
decorations1.append((arbre1, (60,-20)))
decorations1.append((arbre1, (160,-20)))
decorations1.append((arbre1, (50, -10)))
decorations1.append((arbre1, (90, -10)))
decorations1.append((arbre1, (140, -10)))
decorations1.append((arbre1, (0, 0)))
decorations1.append((arbre1, (140, 0)))
decorations1.append((arbre1, (75, 0)))
decorations1.append((arbre1, (40, 10)))
decorations1.append((arbre1, (100, 20)))
decorations1.append((arbre1, (75, 20)))
decorations1.append((arbre1, (30, 20)))
decorations1.append((arbre1, (10, 20)))
decorations1.append((arbre1, (-10, 20)))
decorations1.append((arbre1, (130, 20)))
decorations1.append((arbre1, (-10, 30)))
decorations1.append((arbre1, (30, 30)))
decorations1.append((arbre1, (150, 30)))
decorations1.append((arbre1, (95, 35)))
decorations1.append((arbre1, (120, 40)))
decorations1.append((arbre1, (60, 45)))
decorations1.append((arbre1, (0, 60))) 

decorations1.append((arbre_coupe, (240, 20)))
decorations1.append((arbre_coupe, (215, 50)))
decorations1.append((arbre_coupe, (250, 70)))
decorations1.append((arbre_coupe, (220, 80)))

decorations1.append((pierre1, (379, 234))) 
decorations1.append((pierre1, (100, 350)))

decorations1.append((buisson2, (105, 113)))
decorations1.append((buisson1, (139, 117))) 
decorations1.append((buisson2, (63, 124)))  

decorations1.append((arbre3, (-10, 300))) 
decorations1.append((arbre3, (26, 348))) 
decorations1.append((arbre3, (65, 390))) 
decorations1.append((arbre3, (98, 424))) 
decorations1.append((arbre3, (164, 440))) 
decorations1.append((arbre3, (22, 400))) 



decorations1.append((coffre_ferme, (690, 33)))


for y in range(0, 13):
    for x in range(0, 20):
        if carte1[y][x] == 1:
            eaux1.append(pg.Rect(x * 40, y * 40, 40, 40))
            texture_choisi_carte1[y][x] = random.choice(textures_1[1])
        elif carte1[y][x] == 2:
            murs.append(pg.Rect(x * 40, y * 40, 40, 40))
        elif carte1[y][x] == 3:
            portail.append(pg.Rect(x * 40, y * 40, 40, 40))
        elif carte1[y][x] == 4:
            texture_choisi_carte1[y][x] = textures_1[4][0]
        elif carte1[y][x] == 0:
            texture_choisi_carte1[y][x] = random.choice(ground)
        elif carte1[y][x] == 10:
            eaux1.append(pg.Rect(x * 40, y * 40, 40, 40))
            texture_choisi_carte1[y][x] = g_water_texture
        elif carte1[y][x] == 11:
            eaux1.append(pg.Rect(x * 40, y * 40, 40, 40))
            texture_choisi_carte1[y][x] = d_water_texture
        elif carte1[y][x] == 12:
            eaux1.append(pg.Rect(x * 40, y * 40, 40, 40))
            texture_choisi_carte1[y][x] = d_water_texture 
        elif carte1[y][x] == 13:
            eaux1.append(pg.Rect(x * 40, y * 40, 40, 40))
            texture_choisi_carte1[y][x] = d_water_texture 
        elif carte1[y][x] == 14:
            eaux1.append(pg.Rect(x * 40, y * 40, 40, 40))
            texture_choisi_carte1[y][x] = d_water_texture 
        elif carte1[y][x] == 15:
            eaux1.append(pg.Rect(x * 40, y * 40, 40, 40))
            texture_choisi_carte1[y][x] = d_water_texture 
        elif carte1[y][x] == 16:
            eaux1.append(pg.Rect(x * 40, y * 40, 40, 40))
            texture_choisi_carte1[y][x] = d_water_texture 
        elif carte1[y][x] == 17:
            eaux1.append(pg.Rect(x * 40, y * 40, 40, 40))
            texture_choisi_carte1[y][x] = d_water_texture 
        elif carte1[y][x] == 20:
            eaux1.append(pg.Rect(x * 40, y * 40, 40, 40))
            texture_choisi_carte1[y][x] = d_water_texture 
        elif carte1[y][x] == 21:
            eaux1.append(pg.Rect(x * 40, y * 40, 40, 40))
            texture_choisi_carte1[y][x] = d_water_texture 
        elif carte1[y][x] == 22:
            eaux1.append(pg.Rect(x * 40, y * 40, 40, 40))
            texture_choisi_carte1[y][x] = d_water_texture 
        elif carte1[y][x] == 23 :
            eaux1.append(pg.Rect(x * 40, y * 40, 40, 40))
            texture_choisi_carte1[y][x] = d_water_texture 