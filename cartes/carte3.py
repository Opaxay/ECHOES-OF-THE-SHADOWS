from textures import *
import random

portail = [] #création de la liste (vide) pour les portails
eaux3 = [] #création de la liste (vide) pour l'eau
murs =[] #création de la liste (vide) pour les murs

carte3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],]

decorations3 = []

decorations3.append((arbre1, (0, 340)))
decorations3.append((arbre1, (60, 355)))
decorations3.append((arbre1, (120, 360)))
decorations3.append((arbre1, (95, 365)))
decorations3.append((arbre1, (150, 370)))
decorations3.append((arbre1, (30, 370)))
decorations3.append((arbre1, (-10, 370)))
decorations3.append((arbre1, (130, 380)))
decorations3.append((arbre1, (-10, 380)))
decorations3.append((arbre1, (10, 380)))
decorations3.append((arbre1, (30, 380)))
decorations3.append((arbre1, (75, 380)))
decorations3.append((arbre1, (100, 380)))
decorations3.append((arbre1, (40, 390)))
decorations3.append((arbre1, (75, 400)))
decorations3.append((arbre1, (140, 400)))
decorations3.append((arbre1, (0, 400)))
decorations3.append((arbre1, (140, 410)))
decorations3.append((arbre1, (90, 410)))
decorations3.append((arbre1, (50, 410)))
decorations3.append((arbre1, (160, 420)))
decorations3.append((arbre1, (60, 420)))
decorations3.append((arbre1, (120, 420)))
decorations3.append((arbre1, (180, 430)))
decorations3.append((arbre1, (120, 430)))
decorations3.append((arbre1, (75, 430)))
decorations3.append((arbre1, (40, 430)))
decorations3.append((arbre1, (-20, 430)))

for y in range(0, 13):
    for x in range(0, 20):
        if carte3[y][x] == 1:
            eaux3.append(pg.Rect(x * 40, y * 40, 40, 40))
            texture_choisi_carte3[y][x] = random.choice(textures_3[1])
        elif carte3[y][x] == 2:
            murs.append(pg.Rect(x * 40, y * 40, 40, 40))
        elif carte3[y][x] == 3:
            portail.append(pg.Rect(x * 40, y * 40, 40, 40))
        elif carte3[y][x] == 4:
            texture_choisi_carte3[y][x] = textures_3[4][0]
        else:
            texture_choisi_carte3[y][x] = random.choice(ground)