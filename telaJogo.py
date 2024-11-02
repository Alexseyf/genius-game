import pygame
import var

pygame.init()

def tela_jogo(score, round_number):
    var.screen.fill(var.BLACK)
    
    var.screen.blit(var.genius_board, (0, 0))

    pygame.draw.rect(var.screen, var.BLACK, (var.WIDTH - var.SIDE_PANEL_WIDTH, 0, var.SIDE_PANEL_WIDTH, var.HEIGHT))
    font = pygame.font.SysFont('Arial', 30)

    score_text = font.render(f"{score}", True, var.WHITE)
    var.screen.blit(score_text, (var.WIDTH - var.SIDE_PANEL_WIDTH + var.SIDE_PANEL_WIDTH - score_text.get_width() - 20, 550))
    
    pygame.display.update()