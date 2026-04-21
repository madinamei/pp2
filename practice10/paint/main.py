import pygame
import sys
import math

pygame.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)

screen.fill(WHITE)

font = pygame.font.SysFont("Arial", 18)

drawing = False
last_pos = None
brush_size = 5
current_color = BLACK

eraser_mode = False
rectangle_mode = False
circle_mode = False
square_mode = False
right_triangle_mode = False
equilateral_triangle_mode = False
rhombus_mode = False

start_pos = None

# Palette
palette = [
    (BLACK, pygame.Rect(10, 10, 40, 40)),
    (RED, pygame.Rect(60, 10, 40, 40)),
    (GREEN, pygame.Rect(110, 10, 40, 40)),
    (BLUE, pygame.Rect(160, 10, 40, 40)),
    (YELLOW, pygame.Rect(210, 10, 40, 40)),
]

# Buttons
eraser_button = pygame.Rect(270, 10, 90, 40)
rectangle_button = pygame.Rect(370, 10, 100, 40)
circle_button = pygame.Rect(480, 10, 90, 40)

# New Shape Buttons
square_button = pygame.Rect(580, 10, 80, 40)
right_tri_button = pygame.Rect(670, 10, 110, 40)
eq_tri_button = pygame.Rect(790, 10, 110, 40)
rhombus_button = pygame.Rect(910, 10, 80, 40)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked_ui = False

                # Color palette
                for color, rect in palette:
                    if rect.collidepoint(event.pos):
                        current_color = color
                        eraser_mode = False
                        rectangle_mode = False
                        circle_mode = False
                        square_mode = False
                        right_triangle_mode = False
                        equilateral_triangle_mode = False
                        rhombus_mode = False
                        clicked_ui = True
                        break

                # Tool buttons
                if eraser_button.collidepoint(event.pos):
                    eraser_mode = True
                    rectangle_mode = circle_mode = square_mode = right_triangle_mode = equilateral_triangle_mode = rhombus_mode = False
                    clicked_ui = True

                elif rectangle_button.collidepoint(event.pos):
                    rectangle_mode = True
                    eraser_mode = circle_mode = square_mode = right_triangle_mode = equilateral_triangle_mode = rhombus_mode = False
                    clicked_ui = True

                elif circle_button.collidepoint(event.pos):
                    circle_mode = True
                    eraser_mode = rectangle_mode = square_mode = right_triangle_mode = equilateral_triangle_mode = rhombus_mode = False
                    clicked_ui = True

                elif square_button.collidepoint(event.pos):
                    square_mode = True
                    eraser_mode = rectangle_mode = circle_mode = right_triangle_mode = equilateral_triangle_mode = rhombus_mode = False
                    clicked_ui = True

                elif right_tri_button.collidepoint(event.pos):
                    right_triangle_mode = True
                    eraser_mode = rectangle_mode = circle_mode = square_mode = equilateral_triangle_mode = rhombus_mode = False
                    clicked_ui = True

                elif eq_tri_button.collidepoint(event.pos):
                    equilateral_triangle_mode = True
                    eraser_mode = rectangle_mode = circle_mode = square_mode = right_triangle_mode = rhombus_mode = False
                    clicked_ui = True

                elif rhombus_button.collidepoint(event.pos):
                    rhombus_mode = True
                    eraser_mode = rectangle_mode = circle_mode = square_mode = right_triangle_mode = equilateral_triangle_mode = False
                    clicked_ui = True

                if not clicked_ui:
                    start_pos = event.pos
                    if not (rectangle_mode or circle_mode or square_mode or
                    right_triangle_mode or equilateral_triangle_mode or rhombus_mode):
                        drawing = True
                        last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and start_pos is not None:
                end_pos = event.pos
                x1, y1 = start_pos
                x2, y2 = end_pos

                # === DRAW SHAPES ===
                if rectangle_mode:
                    rect_x = min(x1, x2)
                    rect_y = min(y1, y2)
                    rect_w = abs(x2 - x1)
                    rect_h = abs(y2 - y1)
                    pygame.draw.rect(screen, current_color, (rect_x, rect_y, rect_w, rect_h), 2)

                elif circle_mode:
                    radius = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
                    if radius > 0:
                        pygame.draw.circle(screen, current_color, (x1, y1), radius, 2)

                elif square_mode:
                    side = min(abs(x2 - x1), abs(y2 - y1))
                    rect_x = x1 if x2 > x1 else x1 - side
                    rect_y = y1 if y2 > y1 else y1 - side
                    pygame.draw.rect(screen, current_color, (rect_x, rect_y, side, side), 2)
                elif right_triangle_mode:
                    points = [(x1, y1), (x2, y1), (x1, y2)]
                    pygame.draw.polygon(screen, current_color, points, 2)

                elif equilateral_triangle_mode:
                    side = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                    height = side * math.sqrt(3) / 2
                    cx, cy = x1, y1
                    p1 = (cx, cy - height * 0.7)
                    p2 = (cx - side/2, cy + height * 0.3)
                    p3 = (cx + side/2, cy + height * 0.3)
                    pygame.draw.polygon(screen, current_color, [p1, p2, p3], 2)

                elif rhombus_mode:
                    dx = x2 - x1
                    dy = y2 - y1
                    points = [
                        (x1, y1),
                        (x1 + dx, y1 + dy),
                        (x1 + dx - dy, y1 + dy + dx),
                        (x1 - dy, y1 + dx)
                    ]
                    pygame.draw.polygon(screen, current_color, points, 2)

                drawing = False
                last_pos = None
                start_pos = None

        if event.type == pygame.MOUSEMOTION:
            if drawing:
                current_pos = event.pos
                draw_color = WHITE if eraser_mode else current_color
                draw_size = 20 if eraser_mode else brush_size
                pygame.draw.line(screen, draw_color, last_pos, current_pos, draw_size)
                last_pos = current_pos

    # === DRAW UI ===
    screen.fill(WHITE, (0, 0, WIDTH, 80))  # Clear top bar

    for color, rect in palette:
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

    # Draw buttons
    buttons = [
        (eraser_button, "Eraser"),
        (rectangle_button, "Rectangle"),
        (circle_button, "Circle"),
        (square_button, "Square"),
        (right_tri_button, "Right Tri"),
        (eq_tri_button, "Eq. Triangle"),
        (rhombus_button, "Rhombus")
    ]

    for btn, text in buttons:
        pygame.draw.rect(screen, GRAY, btn)
        pygame.draw.rect(screen, BLACK, btn, 2)
        txt_surf = font.render(text, True, BLACK)
        screen.blit(txt_surf, (btn.x + 5, btn.y + 12))

    pygame.display.update()