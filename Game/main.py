import pygame
import sys

import var
import title

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.screen_size)
    pygame.display.set_caption('2D Platformer Sample')
    var.clock = pygame.time.Clock()

def main():
    while True:
        var.clock.tick(var.FPS)
        input_handle()
        loop_scene()

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def loop_scene():
    pass

init()
main()