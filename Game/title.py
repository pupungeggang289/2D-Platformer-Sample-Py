import pygame

import asset
import var

def loop():
    display()

def display():
    var.screen.blit(asset.Img.background, [0, 0])
    pygame.display.flip()

def mouse_up(x, y, button):
    if button == 1:
        var.scene = 'field'
        var.state = ''