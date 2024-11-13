#!/usr/bin/env python3

import math
import pygame
import sys
import random

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
PINK = (255, 105, 180)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED_2 = (255, 0, 0)
YELLOW = (240, 187, 64)
ORANGE = (226, 137, 50)
RED = (202, 73, 65)
PURPLE = (135, 65, 152)

colors = [GREEN, YELLOW, ORANGE, RED, PURPLE, BLUE]

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Inicialitzar Pygame i configurar paràmetres inicials
pygame.init()

# Definició de colors
WHITE = (255, 255, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]  # Llista de colors aleatoris

# Configurar pantalla i rellotge
screen = pygame.display.set_mode((800, 600))  # Tamany de la finestra
clock = pygame.time.Clock()

# Variables globals
mouse_pos = { "x": -1, "y": -1 }
dots = []

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
    global mouse_pos, dots
    mouse_inside = pygame.mouse.get_focused()  # El ratolí està dins de la finestra?

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Botó tancar finestra
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_pos["x"] = event.pos[0]
                mouse_pos["y"] = event.pos[1]
            else:
                mouse_pos["x"] = -1
                mouse_pos["y"] = -1
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Clic del ratolí
            dots.append({ 
                "x": mouse_pos["x"],
                "y": mouse_pos["y"],
                "radius": 25,
                "color": random.choice(colors)  # Color aleatori de la llista
            })
    return True

# Fer càlculs
def app_run():
    global dots

    delta_time = clock.get_time() / 1000.0  # Convertir a segons
    speed = 5  # Velocitat de reducció del radi

    for dot in dots:
        dot["radius"] -= speed * delta_time
        if dot["radius"] < 5:
            dot["radius"] = 5  # Mantenir un radi mínim de 5

# Dibuixar
def app_draw():
    screen.fill(WHITE)
    draw_grid(pygame, screen, 50)  # Dibuixar una quadrícula amb espaiat de 50 píxels
    
    # Dibuixar punts
    for dot in dots:
        center = (dot["x"], dot["y"])
        pygame.draw.circle(screen, dot["color"], center, int(dot["radius"]))

    pygame.display.update()

if __name__ == "__main__":
    main()