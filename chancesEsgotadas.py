import pygame
import var
from telaInicial import tela_inicial
from telaScore import tela_score

pygame.init()

def chances_esgotadas(score, round_number):
    
    game_over_sound = pygame.mixer.Sound('sound/game_over_sound.mp3')
    game_over_sound.set_volume(0.5)
    game_over_sound.play()
    
    var.screen.fill(var.BLACK)
    erro_text = var.font_title.render("GAME OVER", True, var.WHITE)
    var.screen.blit(erro_text, ((var.WIDTH - erro_text.get_width()) // 2, (var.HEIGHT - erro_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(5000)
    if score > 0:
        tela_score(score, round_number)
    else:
        tela_inicial()