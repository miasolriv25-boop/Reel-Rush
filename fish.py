
import pygame
import random


class Fish:

    def __init__(self, image, width, height, speed, direction):

        self.image = image
        self.is_dead = False
        self.points = 0
        self.width = width
        self.height = height
        self.speed = speed
        self.direction = direction

        # Random underwater depth
        self.y = random.randint(205, 475)

        # Start outside the screen
        if direction == 1:
            self.x = -width
        else:
            self.x = 1142

            # Flip fish to face left
            self.image = pygame.transform.flip(
                image, True, False
            )

        self.rect = pygame.Rect(
            self.x, self.y, width, height
        )

    def update(self, dt):

        self.x += self.speed * self.direction * dt

        self.rect.x = int(self.x)

    def draw(self, screen):

        screen.blit(self.image, self.rect)

    def off_screen(self, screen_width):

        return (
            self.x > screen_width or
            self.x + self.width < 0
        )


class FishManager:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.fish_list = []
        self.spawn_timer = 10

        # Fish image, speed range, size
        self.fish_data = {
            "blue": (150, 230, 65, 65),
            "brown": (90, 150, 65, 65),
            "green": (110, 180, 70, 70),
            "grey": (200, 280, 65, 65),
            "orange": (160, 260, 60, 60),
            "pink": (230, 320, 55, 55),
            "red": (180, 290, 65, 65)
        }

        # Load fish images
        self.images = {}

        for name in self.fish_data:

            self.images[name] = pygame.image.load(
                f"assets/fish_{name}.png"
            ).convert_alpha()

        # Load dead fish images
        self.dead_images = []

        dead_names = [
            "fish_blue_skeleton.png",
            "fish_green_skeleton.png",
            "fish_orange_skeleton.png",
            "fish_pink_skeleton.png",
            "fish_red_skeleton.png"
        ]

        for name in dead_names:

            image = pygame.image.load(
                f"assets/{name}"
            ).convert_alpha()

            self.dead_images.append(image)

        # Create some starting fish
        for i in range(9):
            self.spawn_fish(random.randint(0, width))

    def spawn_fish(self, start_x=None):

        # Randomly choose a fish
        is_dead = random.random() < 0.15
        if is_dead:
            image = random.choice(self.dead_images)
            min_speed = 80
            max_speed = 150
            fish_width = 65
            fish_height = 65
            points = -10
        else:
            name = random.choice(list(self.fish_data.keys()))
            image = self.images[name]
            min_speed, max_speed, fish_width, fish_height = self.fish_data[name]
            points = 10

        

        # Random direction
        direction = random.choice([-1, 1])

        # Random speed
        speed = random.randint(min_speed, max_speed)

        new_fish = Fish(
            image,
            fish_width,
            fish_height,
            speed,
            direction
        )
        new_fish.is_dead = is_dead
        new_fish.points = points

        if start_x is not None:
            new_fish.x = start_x
            new_fish.rect.x = start_x

        self.fish_list.append(new_fish)

    def update(self, dt):

        # Move every fish
        for fish in self.fish_list:
            fish.update(dt)

        # Remove fish that leave the screen
        self.fish_list = [
            fish for fish in self.fish_list
            if not fish.off_screen(self.width)
        ]

        # Spawn new fish
        self.spawn_timer += dt

        if self.spawn_timer >= 1.2:

            self.spawn_fish()
            self.spawn_timer = 0

    def draw(self, screen):

        for fish in self.fish_list:
            fish.draw(screen)
