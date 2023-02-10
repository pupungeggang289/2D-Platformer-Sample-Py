import pygame

import asset
import var

import functiongame

def loop():
    functiongame.player_move()
    display()

def display():
    var.screen.blit(asset.Img.background, [0, 0])

    for i in range(15):
        for j in range(20):
            if var.World.field[i][j] == 1:
                var.screen.blit(asset.Img.block_dirt, [j * 40, i * 40])
    
    pygame.draw.rect(var.screen, (0, 0, 0), [var.World.Player.x - 16, var.World.Player.y - 16, 32, 32])

    pygame.display.flip()

def mouse_up(x, y, button):
    pass

def key_down(key):
    if var.state == '':
        if key == pygame.K_SPACE:
            if var.World.Player.jump > 0:
                functiongame.jump()
                var.World.Player.jump -= 1

        if key == pygame.K_w:
            var.Input.Key.up = True

        if key == pygame.K_a:
            var.Input.Key.left = True

        if key == pygame.K_s:
            var.Input.Key.down = True

        if key == pygame.K_d:
            var.Input.Key.right = True

def key_up(key):
    if var.state == '':
        if key == pygame.K_w:
            var.Input.Key.up = False

        if key == pygame.K_a:
            var.Input.Key.left = False

        if key == pygame.K_s:
            var.Input.Key.down = False

        if key == pygame.K_d:
            var.Input.Key.right = False