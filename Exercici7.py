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


# Fonts
font14 = pygame.font.SysFont("Arial", 14)
font22 = pygame.font.SysFont("Arial", 22)
font50 = pygame.font.SysFont("Arial", 50)

# Variables globals
mouse_data = {"x": -1, "y": -1, "pressed": False, "released": False}
buttons = [
    {"text": "-", "value": "sub", "x": 25, "y": 25, "width": 50, "height": 25, "pressed": False},
    {"text": "+", "value": "add", "x": 75, "y": 25, "width": 50, "height": 25, "pressed": False},
]
counter = 0

# Funció per detectar si el ratolí està dins del rectangle del botó
def is_point_in_rect(mouse_data, button):
    return (
        button["x"] <= mouse_data["x"] <= button["x"] + button["width"] and
        button["y"] <= mouse_data["y"] <= button["y"] + button["height"]
    )

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
    global mouse_data
    mouse_inside = pygame.mouse.get_focused()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Tancar finestra
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_data["x"] = event.pos[0]
                mouse_data["y"] = event.pos[1]
            else:
                mouse_data["x"] = -1
                mouse_data["y"] = -1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_data["pressed"] = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_data["pressed"] = False
            mouse_data["released"] = True

    return True

# Fer càlculs
def app_run():
    global buttons, counter

    for button in buttons:
        if is_point_in_rect(mouse_data, button):
            if mouse_data["pressed"]:
                button["pressed"] = True
            elif mouse_data["released"]:
                button["pressed"] = False   
                # Incrementar o decrementar el comptador segons el botó
                if button["value"] == "add":
                    counter += 1
                else:
                    counter -= 1
        else:
            button["pressed"] = False
    mouse_data["released"] = False  

# Dibuixar
def app_draw():
    screen.fill(WHITE)

    # Dibuixar botons
    for button in buttons:
        draw_button(button)

    # Dibuixar text "Mouse Pressed" si el ratolí està premut
    if mouse_data["pressed"]:
        text = font14.render("Mouse Pressed", True, BLACK)
        screen.blit(text, (135, 30))

    # Dibuixar el comptador al centre
    text_surface = font50.render(str(counter), True, BLACK)
    text_rect = text_surface.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text_surface, text_rect)

    # Actualitzar el dibuix
    pygame.display.update()

# Funció per dibuixar cada botó
def draw_button(button):
    color = ORANGE if button["pressed"] else WHITE
    rect_tuple = (button["x"], button["y"], button["width"], button["height"])
    pygame.draw.rect(screen, color, rect_tuple)  # Dibuixar botó
    pygame.draw.rect(screen, BLACK, rect_tuple, 2)  # Contorn del botó

    # Centrar el text dins del botó
    button_center_x = button["x"] + button["width"] // 2
    button_center_y = button["y"] + button["height"] // 2

    text_surface = font22.render(button["text"], True, BLACK)
    text_rect = text_surface.get_rect(center=(button_center_x, button_center_y))
    screen.blit(text_surface, text_rect)

if __name__ == "__main__":
    main()

