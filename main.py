from imports import *
 
def main():
    
    pygame.mixer.music.load('music/background_music.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.play()
    
    score = 0
    round_number = 1
    sequence = []
    player_sequence = []
    
    tela_inicial()
    start_game = False
    while not start_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if var.score_button.collidepoint(x, y):
                    mostra_score()
                if var.start_button.collidepoint(x, y):
                    start_game_sound = pygame.mixer.Sound('sound/start_game.mp3')
                    start_game_sound.set_volume(0.5)
                    start_game_sound.play()
                    pygame.time.delay(500)
                    start_game = True
                    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.mouse.set_visible(False)
        tela_jogo(score, round_number)
        if round_number == 1:
            pygame.time.delay(1000)

        if len(player_sequence) == 0:
            for _ in range(3):
                sequence.append(random.choice(['green', 'red', 'blue', 'yellow']))

        for color in sequence:
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
            mostra_cor(color)
            pygame.time.delay(500)

        player_sequence = []
        player_turn = True
        index = 0

        while player_turn and index < len(sequence):
            for event in pygame.event.get():
                pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                pygame.mouse.set_visible(True)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cor_jogador = obter_cor_da_posicao(event.pos)
                    
                    if cor_jogador:
                        mostra_cor(cor_jogador)
                        player_sequence.append(cor_jogador)

                        if cor_jogador != sequence[index]:
                            mostra_erro()
                            pygame.time.delay(1000)
                            if 'num_errors' not in locals():
                                num_errors = 0
                            num_errors += 1
                            if num_errors == 3:
                                chances_esgotadas(score, round_number)
                                main()
                            tela_jogo(score, round_number)
                            player_turn = False
                            break

                        if len(player_sequence) == len(sequence):
                            pygame.time.delay(1000)
                            if len(sequence) < 5:
                                score += 1000
                            elif len(sequence) >= 5 and len(sequence) < 10:
                                score += 1600 + round_number
                            else:
                                score += 2500 + round_number * 2
                                
                            player_turn = False
                            round_number += 1
                            sequence.append(random.choice(['green', 'red', 'blue', 'yellow']))
                        else:
                            index += 1
                        if len(player_sequence) == 0:
                            round_number = 1
            
                        tela_jogo(score, round_number)

if __name__ == "__main__":
    main()