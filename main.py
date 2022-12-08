import pygame as py
from pygame.locals import *
from random import randint

#import pyglet

def applyCell(x, y, mapi):
    aliveNeighbours = 0

    aliveNeighbours += mapi[y-1][x-1] if x > 0 and y > 0 else 0
    aliveNeighbours += mapi[y-1][x] if y > 0 else 0
    aliveNeighbours += mapi[y-1][x+1] if x < len(mapi[0])-1 and y > 0 else 0
    aliveNeighbours += mapi[y][x-1] if x > 0 else 0
    aliveNeighbours += mapi[y][x+1] if x < len(mapi[0])-1 else 0
    aliveNeighbours += mapi[y+1][x-1] if x > 0 and y < len(mapi)-1 else 0
    aliveNeighbours += mapi[y+1][x] if y < len(mapi)-1 else 0
    aliveNeighbours += mapi[y+1][x+1] if x < len(mapi[0])-1 and y < len(mapi)-1 else 0

    if mapi[y][x] == 0:
        returnValue = 1 if aliveNeighbours == 3 else 0
    else:
        returnValue = 0 if aliveNeighbours < 2 or aliveNeighbours > 3 else 1
    return returnValue


py.init()

width = 384
height = 216
fenetre = py.display.set_mode((width * 5, height * 5), FULLSCREEN)
#fenetre = pyglet.window.Window(width * 5, height * 5, "LifeGame")
#batch = pyglet.graphics.Batch()
launched = True

color = [(255, 255, 255), (0, 0, 0)]

map = []
for h in range(height):
    map.append([])
    for w in range(width):
        map[h].append(randint(0, 1))

        # if (h*width + w)%2 == 0:
        #     map[h].append(0)
        # else:
        #     map[h].append(1)

while launched:
    for event in py.event.get():
        if event.type == QUIT:
            launched = False

    tempMap = []
    for h in range(height):
        tempMap.append([])
        for w in range(width):
            tempMap[h].append(map[h][w])

    for h in range(height):
        for w in range(width):
            py.draw.rect(fenetre, color[map[h][w]], py.Rect(w * 5, h * 5, 5, 5))
            map[h][w] = applyCell(w, h, tempMap)

    py.display.update()
    #py.time.wait(50)
py.quit()

# @fenetre.event
# def on_draw():
#     tempMap = []
#     for h in range(height):
#         tempMap.append([])
#         for w in range(width):
#             tempMap[h].append(map[h][w])
#
#     for h in range(height):
#         for w in range(width):
#             pyglet.shapes.Rectangle(w * 5, h * 5, 5, 5, color=color[map[h][w]], batch=batch)
#             map[h][w] = applyCell(w, h, tempMap)
#
#     fenetre.clear()
#     batch.draw()
#
# pyglet.app.run()
