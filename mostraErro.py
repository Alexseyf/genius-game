import pygame
import var

pygame.init()

def mostra_erro():
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