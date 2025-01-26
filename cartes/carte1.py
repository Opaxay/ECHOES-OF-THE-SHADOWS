from textures import *
import random

portail = [] #création de la liste (vide) pour les portails
eaux1 = [] #création de la liste (vide) pour l'eau
murs =[] #création de la liste (vide) pour les murs

carte1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'g_o', 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'g_o', 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'g_o', 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'g_o', 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'g_o', 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'g_o', 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'g_o', 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'g_o', 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'g_o', 1, 0, 0, 0, 0, 0, 0, 0],]



decorations1 = []

for i in range(4):
    decorations1.append((fleur, (random.randint(0, 420), random.randint(80, 600))))
    
for i in range(3):
    decorations1.append((pierre2, (random.randint(0, 420), random.randint(80, 600))))

for i in range(9):
    decorations1.append((herbe1, (random.randint(0, 420), random.randint(80, 600))))

for i in range(9):
    decorations1.append((herbe2, (random.randint(0, 420), random.randint(80, 600))))
                       
for i in range(3):
    decorations1.append((buisson1, (random.randint(0, 420), random.randint(80, 600))))

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

decorations1.append((arbre2, (145, 160))) 

decorations1.append((pierre1, (379, 234))) 

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
        elif carte1[y][x] == 'g_o':
            texture_choisi_carte1[y][x] = g_water_texture
        elif carte1[y][x] == 'd_o':
            texture_choisi_carte1[y][x] = d_water_texture
            
