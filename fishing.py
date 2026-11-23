
import pygame


class FishingRod:

    def __init__(self, start_x, start_y, bottom_y):

        self.start_x = start_x
        self.start_y = start_y
        self.bottom_y = bottom_y

        self.hook_y = start_y

        self.drop_speed = 350
        self.reel_speed = 500

        self.state = "idle"

        self.caught_fish = None

        # Stores fish caught for the scoring system later
        self.caught_events = []

    def start(self):

        # Only allow fishing when the line is idle
        if self.state == "idle":

            self.state = "dropping"
            self.caught_fish = None

    def update(self, dt, fish_manager):

        # DROP THE LINE
        if self.state == "dropping":

            self.hook_y += self.drop_speed * dt

            # Hook collision area
            hook_rect = pygame.Rect(
                self.start_x - 8,
                int(self.hook_y) - 8,
                16,
                16
            )

            # Check every fish
            for fish in fish_manager.fish_list:

                if hook_rect.colliderect(fish.rect):

                    # Attach fish to hook
                    self.caught_fish = fish

                    # Remove fish from ocean
                    fish_manager.fish_list.remove(fish)

                    # Save fish for scoring later
                    self.caught_events.append(fish)

                    # Start reeling
                    self.state = "reeling"

                    break

            # If hook reaches the bottom, reel up
            if self.hook_y >= self.bottom_y:

                self.state = "reeling"

        # REEL THE LINE BACK UP
        elif self.state == "reeling":

            self.hook_y -= self.reel_speed * dt

            # Return to starting position
            if self.hook_y <= self.start_y:

                self.hook_y = self.start_y
                self.state = "idle"
                self.caught_fish = None

    def draw(self, screen):

        if self.state != "idle":

            # Draw fishing line
            pygame.draw.line(
                screen,
                (20, 20, 20),
                (self.start_x, self.start_y),
                (self.start_x, int(self.hook_y)),
                3
            )

            # Draw hook
            pygame.draw.circle(
                screen,
                (40, 40, 40),
                (self.start_x, int(self.hook_y)),
                7
            )

            # Draw caught fish attached to hook
            if self.caught_fish is not None:

                fish_image = self.caught_fish.image

                fish_x = self.start_x - fish_image.get_width() // 2
                fish_y = int(self.hook_y) - fish_image.get_height() // 2

                screen.blit(
                    fish_image,
                    (fish_x, fish_y)
                )
