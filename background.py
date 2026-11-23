
import pygame
import math


class OceanBackground:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.wave_time = 0
        
        self.bird_time = 0

        self.birds = pygame.image.load(
            "assets/birds.png"
        ).convert_alpha()

        self.birds = pygame.transform.scale(
            self.birds, (300, 300))

        # Colors
        self.sky_blue = (153, 218, 231)
        self.ocean_blue = (0, 160, 225)
        self.sand = (180, 120, 85)
        self.dark_sand = (85, 48, 35)

        # Load underwater decorations
        self.seaweed1 = pygame.image.load(
            "assets/seaweed_green_a.png"
        ).convert_alpha()

        self.seaweed2 = pygame.image.load(
            "assets/seaweed_grass_a.png"
        ).convert_alpha()

        self.rock = pygame.image.load(
            "assets/rock_a.png"
        ).convert_alpha()

        # Resize decorations
        self.seaweed1 = pygame.transform.scale(
            self.seaweed1, (85, 130)
        )

        self.seaweed2 = pygame.transform.scale(
            self.seaweed2, (65, 100)
        )

        self.rock = pygame.transform.scale(
            self.rock, (55, 45)
        )

    def draw(self, screen):

        self.wave_time += 0.035
        self.bird_time += 0.04

        screen.fill(self.sky_blue)

        # Gently moving birds
        bird_y = -80 + math.sin(self.bird_time) * 5
        screen.blit(self.birds, (700, int(bird_y)))
        # Ocean surface
        wave_points = []

        for x in range(0, self.width + 20, 10):

            y = 155 + math.sin(
                x * 0.015 + self.wave_time
            ) * 10

            wave_points.append((x, int(y)))

        wave_points.append((self.width, self.height))
        wave_points.append((0, self.height))

        pygame.draw.polygon(
            screen, self.ocean_blue, wave_points
        )

        # Ocean floor
        pygame.draw.rect(
            screen, self.sand,
            (0, 525, self.width, self.height - 525)
        )

        # Dark brown
        pygame.draw.rect(
            screen, self.dark_sand,
            (0, 510, self.width, 25)
        )

        # Seaweeeeeeeed
        screen.blit(self.seaweed1, (680, 390))
        screen.blit(self.seaweed2, (750, 430))
        screen.blit(self.seaweed1, (970, 420))

        # Rock
        screen.blit(self.rock, (250, 590))
        screen.blit(self.rock, (850, 600))
        screen.blit(self.rock, (540, 540))
