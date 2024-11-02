import pygame
import var

pygame.init()

def tela_inicial():
    pygame.mouse.set_visible(True)
    pygame.mixer.music.load('music/background_music.mp3')
    pygame.mixer.music.play()
    background = pygame.image.load('imgs/main_background.png')
    background = pygame.transform.scale(background, (var.WIDTH, var.HEIGHT))
    var.screen.blit(background, (0, 0))
    
    #Título
    genius_text = var.font_title.render("GENIUS", True, var.BLACK)
    var.screen.blit(genius_text, (var.WIDTH - var.SIDE_PANEL_WIDTH - 550, 100))
    genius_text = var.font.render("GAME", True, var.BLACK)
    var.screen.blit(genius_text, (var.WIDTH - var.SIDE_PANEL_WIDTH - 440, 160))
    
    # Botão iniciar
    pygame.draw.rect(var.screen, var.GRAY, var.start_button)
    text = var.font.render("Iniciar Jogo", True, var.BLACK)
    var.screen.blit(text, (var.start_button.x + (var.start_button.width - text.get_width()) // 2, var.start_button.y + (var.start_button.height - text.get_height()) // 2))
    
    # Botão score
    pygame.draw.rect(var.screen, var.GRAY, var.score_button)
    score_text = var.font_score.render("Score", True, var.BLACK)
    var.screen.blit(score_text, (var.score_button.x + (var.score_button.width - score_text.get_width()) // 2, var.score_button.y + (var.score_button.height - score_text.get_height()) // 2))
    
    pygame.display.update()