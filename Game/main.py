import pygame
import sys

import var
import asset

import title
import field

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.screen_size)
    pygame.display.set_caption('2D Platformer Sample')
    var.clock = pygame.time.Clock()

    load_image()

def load_image():
    asset.Img.background = pygame.image.load('Image/Background.png')
    asset.Img.block_dirt = pygame.image.load('Image/Dirt.png')

def main():
    while True:
        var.clock.tick(var.FPS)
        input_handle()
        loop_scene()

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()

            if var.scene == 'title':
                title.mouse_up(mouse[0], mouse[1], event.button)

        if event.type == pygame.KEYDOWN:
            key = event.key

            if var.scene == 'field':
                field.key_down(key)

        if event.type == pygame.KEYUP:
            key = event.key

            if var.scene == 'field':
                field.key_up(key)

def loop_scene():
    if var.scene == 'title':
        title.loop()

    elif var.scene == 'field':
        field.loop()

init()
main()