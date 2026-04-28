import pygame
from db import get_top_10

WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(180,180,180)


class MenuUI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Verdana", 40)
        self.username = ""

    def run(self):
        while True:
            self.screen.fill(WHITE)

            title = self.font.render("SNAKE", True, BLACK)
            self.screen.blit(title,(320,100))

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return "quit",""

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_BACKSPACE:
                        self.username = self.username[:-1]
                    else:
                        self.username += e.unicode

                if e.type == pygame.MOUSEBUTTONDOWN:
                    return "play", self.username

            pygame.display.update()


class GameOverUI:
    def __init__(self, screen, score, level, best):
        self.screen = screen
        self.score = score
        self.level = level
        self.best = best
        self.font = pygame.font.SysFont("Verdana", 30)

    def run(self):
        while True:
            self.screen.fill((0,0,0))

            self.screen.blit(self.font.render(f"Score {self.score}",True,(255,255,255)),(300,200))

            pygame.display.update()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return "quit"
                if e.type == pygame.KEYDOWN:
                    return "menu"


class LeaderboardUI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Verdana", 24)

    def run(self):
        while True:
            self.screen.fill((0,0,0))

            data = get_top_10()

            y=100
            for i,row in enumerate(data):
                t = self.font.render(f"{i+1}. {row[0]} {row[1]}",True,(255,255,255))
                self.screen.blit(t,(200,y))
                y+=30

            pygame.display.update()

            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    return