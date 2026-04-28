import pygame
import sys
import math
from datetime import datetime
from collections import deque

pygame.init()
pygame.key.set_repeat(400, 30)

WIDTH, HEIGHT = 1000, 700
TOOLBAR_HEIGHT = 90

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (230, 230, 230)

font = pygame.font.SysFont("Arial", 16)
text_font = pygame.font.SysFont("Arial", 28)

canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT)).convert_alpha()
canvas.fill(WHITE)

current_color = BLACK
brush_size = 5
tool = "pencil"

drawing = False
start_pos = None
last_pos = None

text_mode = False
text_pos = None
text_value = ""

palette = [
    (BLACK, pygame.Rect(10, 10, 35, 35)),
    (RED, pygame.Rect(50, 10, 35, 35)),
    (GREEN, pygame.Rect(90, 10, 35, 35)),
    (BLUE, pygame.Rect(130, 10, 35, 35)),
    (YELLOW, pygame.Rect(170, 10, 35, 35)),
]

buttons = {
    "pencil": pygame.Rect(220, 10, 70, 35),
    "line": pygame.Rect(295, 10, 60, 35),
    "eraser": pygame.Rect(360, 10, 70, 35),
    "fill": pygame.Rect(435, 10, 55, 35),
    "text": pygame.Rect(495, 10, 55, 35),
    "rect": pygame.Rect(555, 10, 70, 35),
    "circle": pygame.Rect(630, 10, 70, 35),
    "square": pygame.Rect(705, 10, 70, 35),
    "right_tri": pygame.Rect(780, 10, 90, 35),
    "eq_tri": pygame.Rect(875, 10, 90, 35),
    "rhombus": pygame.Rect(10, 50, 85, 30),
}

size_buttons = {
    2: pygame.Rect(110, 50, 55, 30),
    5: pygame.Rect(170, 50, 55, 30),
    10: pygame.Rect(230, 50, 55, 30),
}


def to_canvas_pos(pos):
    x, y = pos
    return x, y - TOOLBAR_HEIGHT


def inside_canvas(pos):
    x, y = pos
    return 0 <= x < WIDTH and TOOLBAR_HEIGHT <= y < HEIGHT


def flood_fill(surface, start, fill_color):
    width, height = surface.get_size()
    x, y = start

    target_color = surface.get_at((x, y))
    new_color = pygame.Color(*fill_color)

    if target_color == new_color:
        return

    queue = deque([(x, y)])

    while queue:
        px, py = queue.popleft()

        if not (0 <= px < width and 0 <= py < height):
            continue

        if surface.get_at((px, py)) != target_color:
            continue

        surface.set_at((px, py), new_color)

        queue.extend([
            (px + 1, py),
            (px - 1, py),
            (px, py + 1),
            (px, py - 1),
        ])


def draw_shape(surface, selected_tool, start, end, color, size):
    x1, y1 = start
    x2, y2 = end

    if selected_tool == "line":
        pygame.draw.line(surface, color, start, end, size)

    elif selected_tool == "rect":
        rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(surface, color, rect, size)

    elif selected_tool == "circle":
        radius = int(math.hypot(x2 - x1, y2 - y1))
        pygame.draw.circle(surface, color, start, radius, size)

    elif selected_tool == "square":
        side = min(abs(x2 - x1), abs(y2 - y1))
        rx = x1 if x2 >= x1 else x1 - side
        ry = y1 if y2 >= y1 else y1 - side
        pygame.draw.rect(surface, color, (rx, ry, side, side), size)

    elif selected_tool == "right_tri":
        points = [(x1, y1), (x2, y1), (x1, y2)]
        pygame.draw.polygon(surface, color, points, size)

    elif selected_tool == "eq_tri":
        side = math.hypot(x2 - x1, y2 - y1)
        height = side * math.sqrt(3) / 2
        points = [
            (x1, y1 - height / 2),
            (x1 - side / 2, y1 + height / 2),
            (x1 + side / 2, y1 + height / 2),
        ]
        pygame.draw.polygon(surface, color, points, size)

    elif selected_tool == "rhombus":
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
        pygame.draw.polygon(surface, color, points, size)


def save_canvas():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"paint_{timestamp}.png"
    pygame.image.save(canvas, filename)
    print("Saved:", filename)


def draw_ui():
    pygame.draw.rect(screen, LIGHT_GRAY, (0, 0, WIDTH, TOOLBAR_HEIGHT))

    for color, rect in palette:
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

    for key, rect in buttons.items():
        color = WHITE if tool == key else GRAY
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        label = font.render(key.capitalize(), True, BLACK)
        screen.blit(label, (rect.x + 5, rect.y + 8))

    for size, rect in size_buttons.items():
        color = WHITE if brush_size == size else GRAY
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        label = font.render(str(size), True, BLACK)
        screen.blit(label, (rect.x + 20, rect.y + 7))

    info = font.render("1/2/3 size | Ctrl/Cmd+S save | Enter confirm | Esc cancel", True, BLACK)
    screen.blit(info, (300, 55))


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            mods = pygame.key.get_mods()
            if (mods & pygame.KMOD_CTRL) or (mods & pygame.KMOD_META):
                if event.key == pygame.K_s:
                    save_canvas()

            if event.key == pygame.K_1:
                brush_size = 2
            elif event.key == pygame.K_2:
                brush_size = 5
            elif event.key == pygame.K_3:
                brush_size = 10

            if text_mode:
                if event.key == pygame.K_RETURN:
                    if text_value.strip():
                        rendered = text_font.render(text_value, True, current_color, None)
                        canvas.blit(rendered, text_pos)
                    text_mode = False
                    text_value = ""

                elif event.key == pygame.K_ESCAPE:
                    text_mode = False
                    text_value = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_value = text_value[:-1]

                else:
                    if event.unicode.isprintable():
                        text_value += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked_ui = False

            for color, rect in palette:
                if rect.collidepoint(event.pos):
                    current_color = color
                    clicked_ui = True

            for key, rect in buttons.items():
                if rect.collidepoint(event.pos):
                    tool = key
                    clicked_ui = True

            for size, rect in size_buttons.items():
                if rect.collidepoint(event.pos):
                    brush_size = size
                    clicked_ui = True

            if not clicked_ui and inside_canvas(event.pos):
                cpos = to_canvas_pos(event.pos)

                if tool == "fill":
                    flood_fill(canvas, cpos, current_color)

                elif tool == "text":
                    text_mode = True
                    text_pos = cpos
                    text_value = ""

                elif tool in ["pencil", "eraser"]:
                    drawing = True
                    last_pos = cpos

                else:
                    drawing = True
                    start_pos = cpos

        if event.type == pygame.MOUSEMOTION:
            if drawing and inside_canvas(event.pos):
                cpos = to_canvas_pos(event.pos)

                if tool == "pencil":
                    pygame.draw.line(canvas, current_color, last_pos, cpos, brush_size)
                    last_pos = cpos

                elif tool == "eraser":
                    pygame.draw.line(canvas, WHITE, last_pos, cpos, brush_size * 3)
                    last_pos = cpos

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if drawing and inside_canvas(event.pos):
                end_pos = to_canvas_pos(event.pos)

                if tool not in ["pencil", "eraser"]:
                    draw_shape(canvas, tool, start_pos, end_pos, current_color, brush_size)

            drawing = False

    preview = canvas.copy()

    if drawing and start_pos is not None:
        mouse_pos = pygame.mouse.get_pos()
        if inside_canvas(mouse_pos):
            end_pos = to_canvas_pos(mouse_pos)
            draw_shape(preview, tool, start_pos, end_pos, current_color, brush_size)

    if text_mode and text_pos is not None:
        rendered = text_font.render(text_value + "|", True, current_color, None)
        preview.blit(rendered, text_pos)

    screen.fill(WHITE)
    screen.blit(preview, (0, TOOLBAR_HEIGHT))
    draw_ui()
    pygame.display.update()