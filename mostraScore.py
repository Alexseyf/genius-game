import pygame
import var
import sys
from telaInicial import tela_inicial
from criaArquivoScores import cria_arquivo_scores

pygame.init()

def mostra_score():
    cria_arquivo_scores()
    jogador = []
    score = []
    round_number = []
    var.screen.fill(var.BLACK)
    with open('scores.txt', 'r') as f:
        for line in f:
            j, s, r = line.strip().split(';')
            jogador.append(j)
            score.append(s)
            round_number.append(r)
    scores = sorted(zip(jogador, score, round_number), key=lambda x: int(x[1]), reverse=True)
    scores = scores[:10]
    
    if scores == []:
        text = var.font_score.render(("Jogue e grave seu primeiro score").upper(), True, var.WHITE)
        var.screen.blit(text, ((var.WIDTH - text.get_width()) // 2, 10))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    tela_inicial()
                    return
    else:    
        for i, (j, s, r) in enumerate(scores):
            y = 50 + i * 30
            text = var.font_score.render(("Ranking").upper(), True, var.WHITE)
            var.screen.blit(text, ((var.WIDTH - text.get_width()) // 2, 10))
            text = var.font_score.render(f"{i + 1}. {j.upper()} {s}", True, var.WHITE)
            var.screen.blit(text, (360, y))
        pygame.display.update()
    
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    tela_inicial()
                    return