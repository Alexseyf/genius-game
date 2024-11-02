import pygame
import var

pygame.init()

def mostra_cor(color):
    if color == 'green':
        var.screen.blit(var.genius_green, (0, 0))
    elif color == 'red':
        var.screen.blit(var.genius_red, (0, 0))
    elif color == 'blue':
        var.screen.blit(var.genius_blue, (0, 0))
    elif color == 'yellow':
        var.screen.blit(var.genius_yellow, (0, 0))
    
    pygame.event.pump()
    pygame.display.update()
    pygame.time.delay(400)
    
    var.screen.blit(var.genius_board, (0, 0))
    # pygame.event.pump()   
    pygame.display.update()
    pygame.time.delay(250)