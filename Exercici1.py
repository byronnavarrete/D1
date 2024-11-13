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


# Variables globals
window_size = { 
    "width": 0, 
    "height": 0, 
    "center": {
        "x": 0,
        "y": 0
    } 
}

# Configuració inicial de Pygame
pygame.init()
WHITE = (255, 255, 255)  # Color blanc per al fons
screen = pygame.display.set_mode((800, 600))  # Crear la finestra de 800x600 píxels
clock = pygame.time.Clock()  # Crear el rellotge per limitar FPS

# Funció per dibuixar una quadrícula - Per defecte assumeix que `utils` té aquesta funció
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

# Fer càlculs
def app_run():
    global window_size

    window_size["width"] = screen.get_width()
    window_size["height"] = screen.get_height()
    window_size["center"]["x"] = int(screen.get_width() / 2)
    window_size["center"]["y"] = int(screen.get_height() / 2)

# Dibuixar
def app_draw():
    screen.fill(WHITE)
    draw_grid(pygame, screen, 50)  # Dibuixar una quadrícula amb espaiat de 50 píxels

    for q in range(20, 0, -1):
        perspective = (q / 20)

        q_ample = q * 25 * perspective
        q_alt = q * 20 * perspective

        x = window_size["center"]["x"] - int(q_ample / 2)
        y = window_size["center"]["y"] - int(q_alt / 2)

        parell = (q % 2) == 0
        if parell:
            color = (0, 0, q * 10)  # Color blau
        else:
            color = (0, q * 10, 0)  # Color verd

        q_rect_tuple = (x, y, q_ample, q_alt)
        pygame.draw.rect(screen, color, q_rect_tuple)

    pygame.display.update()

if __name__ == "__main__":
    main()