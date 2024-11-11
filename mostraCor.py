import pygame
import var

pygame.init()

def mostra_cor(color):
    if color == 'green':
        var.screen.blit(var.genius_green, (0, 0))
        green_sound = pygame.mixer.Sound('sound/green_sound.mp3')
        green_sound.set_volume(0.5)
        green_sound.play()
    elif color == 'red':
        var.screen.blit(var.genius_red, (0, 0))
        red_sound = pygame.mixer.Sound('sound/red_sound.mp3')
        red_sound.set_volume(0.5)
        red_sound.play()
    elif color == 'blue':
        var.screen.blit(var.genius_blue, (0, 0))
        blue_sound = pygame.mixer.Sound('sound/blue_sound.mp3')
        blue_sound.set_volume(0.5)
        blue_sound.play()
    elif color == 'yellow':
        var.screen.blit(var.genius_yellow, (0, 0))
        yellow_sound = pygame.mixer.Sound('sound/yellow_sound.mp3')
        yellow_sound.set_volume(0.5)
        yellow_sound.play()
    
    pygame.event.pump()
    pygame.display.update()
    pygame.time.delay(400)
    
    var.screen.blit(var.genius_board, (0, 0))
    # pygame.event.pump()   
    pygame.display.update()
    pygame.time.delay(250)