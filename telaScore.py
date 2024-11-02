import pygame
import sys
import var
from telaInicial import tela_inicial
from criaArquivoScores import cria_arquivo_scores

pygame.init()

def tela_score(score, round_number):
    cria_arquivo_scores()
    var.screen.fill(var.BLACK)
    input_box = pygame.Rect((var.WIDTH - 300) // 2, (var.HEIGHT - 50) // 2, 300, 50)
    color_active = var.BLACK
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    with open('scores.txt', 'a') as f:
                        f.write(f'{text};{score};{round_number}\n')
                    done = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        color = color_active

        var.screen.fill(var.BLACK)
        prompt_text = var.font_score.render("Digite seu nome:", True, var.WHITE)
        var.screen.blit(prompt_text, (input_box.x, input_box.y - 40))
        txt_surface = var.font_score.render(text, True, var.WHITE)
        width = max(300, txt_surface.get_width() + 10)
        input_box.w = width
        var.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(var.screen, color, input_box, 2)

        pygame.display.flip()
        pygame.time.delay(100)

    tela_inicial()