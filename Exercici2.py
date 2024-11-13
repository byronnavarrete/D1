#!/usr/bin/env python3

import math
import pygame
import sys

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
PINK = (255, 105, 180)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Inicialitzar la font
fontArial = pygame.font.SysFont("Arial", 15)

# Funció per dibuixar la quadrícula - en cas que `utils` no estigui disponible
def draw_grid(pygame, screen, spacing):
    width, height = screen.get_size()
    for x in range(0, width, spacing):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, height))
    for y in range(0, height, spacing):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (width, y))

# Bucle de l'aplicació
def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60)  # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Botó tancar finestra
            return False
    return True

# Fer càlculs (no es fa res en aquest cas)
def app_run():
    pass

# Dibuixar
def app_draw():
    screen.fill(WHITE)
    draw_grid(pygame, screen, 50)  # Dibuixar una quadrícula amb espaiat de 50 píxels

    # Dibuixar els punts i textos amb alineacions específiques
    pygame.draw.circle(screen, BLUE, (100, 50), 5)
    draw_text("Poma", fontArial, 100, 50, "left", "bottom")

    pygame.draw.circle(screen, BLUE, (100, 100), 5)
    draw_text("Pera", fontArial, 100, 100, "center", "center")

    pygame.draw.circle(screen, BLUE, (100, 150), 5)
    draw_text("Raïm", fontArial, 100, 150, "right", "top")

    pygame.draw.circle(screen, BLUE, (250, 50), 5)
    draw_text("Plàtan", fontArial, 250, 50, "left", "top")

    pygame.draw.circle(screen, BLUE, (250, 100), 5)
    draw_text("Préssec", fontArial, 250, 100, "center", "center")

    pygame.draw.circle(screen, BLUE, (250, 150), 5)
    draw_text("Maduixa", fontArial, 250, 150, "right", "bottom")

    pygame.display.update()

# Funció per dibuixar text amb alineació configurable
def draw_text(text, font, x, y, align_x="left", align_y="top"):
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect()

    # Configurar l'alineació horitzontal
    if align_x == "center":
        text_rect.centerx = x
    elif align_x == "right":
        text_rect.right = x
    else:
        text_rect.left = x

    # Configurar l'alineació vertical
    if align_y == "center":
        text_rect.centery = y
    elif align_y == "bottom":
        text_rect.bottom = y
    else:
        text_rect.top = y

    screen.blit(text_surface, text_rect)
    pygame.draw.line(screen, (0, 0, 0), (x, y), (x + 50, y), 1)

if __name__ == "__main__":
    main()