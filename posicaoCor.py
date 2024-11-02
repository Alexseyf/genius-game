import pygame
import var

pygame.init()

def obter_cor_da_posicao(pos):
    x, y = pos
    if x < (var.WIDTH - var.SIDE_PANEL_WIDTH) / 2 and y <var.HEIGHT / 2:
        return 'green'
    elif x < (var.WIDTH - var.SIDE_PANEL_WIDTH) / 2 and y > var.HEIGHT / 2:
        return 'red'
    elif x > (var.WIDTH - var.SIDE_PANEL_WIDTH) / 2 and y > var.HEIGHT / 2:
        return 'blue'
    elif x > (var.WIDTH - var.SIDE_PANEL_WIDTH) / 2 and y < var.HEIGHT / 2:
        return 'yellow'
    return None