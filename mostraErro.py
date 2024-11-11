import pygame
import var

pygame.init()

def mostra_erro():
    
    error_sound = pygame.mixer.Sound('sound/error_sound.mp3')
    error_sound.set_volume(0.7)
    error_sound.play()
    
    pygame.mouse.set_visible(False)
    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    for _ in range(3):
        var.screen.blit(var.genius_all, (0, 0))
        pygame.display.update()
        pygame.time.delay(500)
        var.screen.blit(var.genius_board, (0, 0))
        pygame.display.update()
        pygame.time.delay(500)
    var.screen.blit(var.genius_board, (0, 0))
    pygame.display.update()
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)