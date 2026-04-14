import pygame
import os
import sys

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((800, 500))
        pygame.display.set_caption("Music Player")

        self.font = pygame.font.SysFont("Arial", 28)

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        self.playlist = [
            os.path.join(BASE_DIR, "music", "track1.mp3"),
            os.path.join(BASE_DIR, "music", "track2.mp3")
        ]

        self.index = 0
        self.playing = False

        pygame.mixer.music.load(self.playlist[self.index])

    def play(self):
        pygame.mixer.music.play()
        self.playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False

    def next(self):
        self.index = (self.index + 1) % len(self.playlist)
        pygame.mixer.music.load(self.playlist[self.index])
        self.play()

    def prev(self):
        self.index = (self.index - 1) % len(self.playlist)
        pygame.mixer.music.load(self.playlist[self.index])
        self.play()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.play()

                    elif event.key == pygame.K_s:
                        self.stop()

                    elif event.key == pygame.K_n:
                        self.next()

                    elif event.key == pygame.K_b:
                        self.prev()

                    elif event.key == pygame.K_q:
                        running = False

            self.screen.fill((30, 30, 30))

            text = self.font.render(
                f"Track: {os.path.basename(self.playlist[self.index])}",
                True,
                (255, 255, 255)
            )
            self.screen.blit(text, (50, 200))

            pygame.display.update()

        pygame.quit()
        sys.exit()