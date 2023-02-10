import pygame

import asset
import var

def loop():
    display()

def display():
    var.screen.blit(asset.Img.background, [0, 0])

    for i in range(15):
        for j in range(20):
            if var.World.field[i][j] == 1:
                var.screen.blit(asset.Img.block_dirt, [j * 40, i * 40])
                
    pygame.display.flip()

def mouse_up(x, y, button):
    pass