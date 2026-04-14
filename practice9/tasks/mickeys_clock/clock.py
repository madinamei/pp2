import pygame
import sys
import os
from datetime import datetime


class MickeyClock:
    def __init__(self):
        pygame.init()

        self.WIDTH = 800
        self.HEIGHT = 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Mickey Clock")

        self.clock = pygame.time.Clock()

        self.center_x = self.WIDTH // 2
        self.center_y = self.HEIGHT // 2

        clock_path = os.path.join("images", "clock.png")
        self.clock_image = pygame.image.load(clock_path).convert_alpha()
        self.clock_image = pygame.transform.scale(self.clock_image, (700, 700))
        self.image_rect = self.clock_image.get_rect(center=(self.center_x, self.center_y))

        right_hand_path = os.path.join("images", "right.png")
        left_hand_path = os.path.join("images", "left.png")

        self.right_hand = pygame.image.load(right_hand_path).convert_alpha()
        self.left_hand = pygame.image.load(left_hand_path).convert_alpha()

        self.right_hand = pygame.transform.scale(self.right_hand, (180, 60))
        self.left_hand = pygame.transform.scale(self.left_hand, (220, 60))

    def run(self):
        running = True

        while running:
            current_time = datetime.now()
            minutes = current_time.minute
            seconds = current_time.second

            minute_angle = -(minutes * 6) + 90
            second_angle = -(seconds * 6) + 90

            rotated_minute_hand = pygame.transform.rotate(self.right_hand, minute_angle)
            rotated_second_hand = pygame.transform.rotate(self.left_hand, second_angle)

            minute_rect = rotated_minute_hand.get_rect(center=(self.center_x, self.center_y))
            second_rect = rotated_second_hand.get_rect(center=(self.center_x, self.center_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.clock_image, self.image_rect)
            self.screen.blit(rotated_minute_hand, minute_rect)
            self.screen.blit(rotated_second_hand, second_rect)

            pygame.display.flip()
            self.clock.tick(1)

        pygame.quit()
        sys.exit()