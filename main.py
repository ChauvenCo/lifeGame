import pygame as py
from pygame.locals import *
from random import randint

# import pyglet
# from pyglet import shapes
#
# window = pyglet.window.Window(500, 500)
# batch = pyglet.graphics.Batch()
#
# red_sequare = shapes.Rectangle(150, 240, 200, 20, color=(255, 55, 55), batch=batch)
# # green_sequare = shapes.Rectangle(175, 220, 150, 20, color=(55, 255, 55), batch=batch)
# # blue_sequare = shapes.Rectangle(200, 200, 100, 20, color=(55, 55, 255), batch=batch)
#
# @window.event
# def on_draw():
#     window.clear()
#     batch.draw()
#
# pyglet.app.run()

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

width = 383
height = 216
launched = True

py.init()
fenetre = py.display.set_mode((width * 5, height * 5), FULLSCREEN)

color = [(255, 255, 255), (0, 0, 0)]

map = []
for h in range(height):
    map.append([])
    for w in range(width):
        # map[h].append(randint(0, 1))

        if (h*width + w)%2 == 0:
            map[h].append(0)
        else:
            map[h].append(1)

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

