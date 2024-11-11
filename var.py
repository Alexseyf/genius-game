import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

WIDTH = 900
HEIGHT = 600
SIDE_PANEL_WIDTH = 300

genius_board = pygame.image.load('imgs/genius.png')
genius_blue = pygame.image.load('imgs/genius_blue.png')
genius_green = pygame.image.load('imgs/genius_green.png')
genius_yellow = pygame.image.load('imgs/genius_yellow.png')
genius_red = pygame.image.load('imgs/genius_red.png')
genius_all = pygame.image.load('imgs/genius_all.png')
genius_icon = pygame.image.load('imgs/genius.png')

board_size = (WIDTH - SIDE_PANEL_WIDTH, HEIGHT)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_icon(genius_icon)
pygame.display.set_caption("Genius Game")

start_button = pygame.Rect((WIDTH - 800) // 2, (HEIGHT + 300) // 2, 200, 40)
score_button = pygame.Rect((WIDTH - 800) // 2, (HEIGHT + 400) // 2, 200, 40)

font_title = pygame.font.SysFont('Arial', 60)
font_score = pygame.font.SysFont('Arial', 22)
font = pygame.font.SysFont('Arial', 30)

genius_board = pygame.transform.scale(genius_board, board_size)
genius_blue = pygame.transform.scale(genius_blue, board_size)
genius_green = pygame.transform.scale(genius_green, board_size)
genius_yellow = pygame.transform.scale(genius_yellow, board_size)
genius_red = pygame.transform.scale(genius_red, board_size)
genius_all = pygame.transform.scale(genius_all, board_size)