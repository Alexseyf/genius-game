import os

def cria_arquivo_scores():
    if not os.path.exists('scores.txt'):
        with open('scores.txt', 'w'):
            pass