import pygame
import sqlite3
import random
import sys

# Inicialização do Pygame
pygame.init()

# Definições do jogo
WIDTH, HEIGHT = 800, 600
FPS = 60

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicialização da janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Forca")
clock = pygame.time.Clock()

# Inicialização do banco de dados SQLite
conn = sqlite3.connect("forca.db")
cursor = conn.cursor()

# Criar tabela de palavras se não existir
cursor.execute("CREATE TABLE IF NOT EXISTS palavras (palavra TEXT);")
conn.commit()

# Adicionar palavras ao banco de dados (pode personalizar esta lista)
palavras = ["vasco", "flamengo", "fluminense", "gremio", "juventus", "internacional", "vila nova", "avaí", "corinthians"]
cursor.executemany("INSERT INTO palavras VALUES (?);", [(palavra,) for palavra in palavras])
conn.commit()

# Função para obter uma palavra aleatória do banco de dados
def get_random_word():
    cursor.execute("SELECT palavra FROM palavras ORDER BY RANDOM() LIMIT 1;")
    return cursor.fetchone()[0]

# Função para desenhar a interface do jogo e a palavra oculta
def draw_interface(word, guessed_letters, tries):
    screen.fill(WHITE) # Preenche a tela com a cor branca

    # Desenhe a palavra oculta
    font = pygame.font.Font(None, 36)
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    text = font.render(display_word, True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

    # Adicione mais lógica de desenho conforme necessário, como desenhar a forca

# Função para desenhar a forca
def draw_hangman(tries):
    # Limpa a área da forca
    pygame.draw.rect(screen, WHITE, (50, 50, 200, 400))

    # Desenha a forca com base no número de tentativas
    if tries >= 1:
        pygame.draw.circle(screen, BLACK, (150, 100), 50, 2) # cabeça

    if tries >= 2:
        pygame.draw.line(screen, BLACK, (150, 150), (150, 300), 2) # corpo

    if tries >= 3:
        pygame.draw.line(screen, BLACK, (150, 200), (100, 150), 2) # braço esquerdo

    if tries >= 4:
        pygame.draw.line(screen, BLACK, (150, 200), (200, 150), 2) # braço direito

    if tries >= 5:
        pygame.draw.line(screen, BLACK, (150, 300), (100, 400), 2) # perna esquerda

    if tries >= 6:
        pygame.draw.line(screen, BLACK, (150, 300), (200, 400), 2) # perna direita

# Função principal do jogo
def main():
    word_to_guess = get_random_word().upper()
    guessed_letters = set()
    tries = 0

    while True:
        for event in pygame.event.get():
            draw_interface(word_to_guess, guessed_letters, tries)
            draw_hangman(tries)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in range(pygame.K_a, pygame.K_z + 1):
                    letter = chr(event.key).upper()
                    if letter not in guessed_letters:
                        guessed_letters.add(letter)
                        if letter not in word_to_guess:
                            tries += 1

        draw_interface(word_to_guess, guessed_letters, tries)
        draw_hangman(tries)

        # Atualizar a tela
        pygame.display.flip()

        # Definir a taxa de quadros por segundo
        clock.tick(FPS)

# Executar o jogo
if __name__ == "__main__":
    main()
