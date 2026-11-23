#remeber to import all helpers into pygame and update all files
import background
import pygame
import intro
import fish
import fishing
import game_over

pygame.init()

#actual screen (width,height)
WIDTH = 1142
HEIGHT = 719

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reel Rush!") #keep name for now

clock = pygame.time.Clock()

# font
title_font = pygame.font.SysFont("ubuntu", 95)
rule_font = pygame.font.SysFont("ubuntu", 48)

# Load boat
boat_image = pygame.image.load(
    "assets/boat.png"
).convert_alpha()

boat_image = pygame.transform.scale(
    boat_image, (230, 200)
)

boat_x = 440
boat_y = 15

# Ocean
ocean = background.OceanBackground(WIDTH, HEIGHT)

# Fish
fish_manager = fish.FishManager(WIDTH, HEIGHT)

# Fishing rod
fishing_rod = fishing.FishingRod(
    boat_x + 211,
    boat_y + 40,
    505
)

#states and game
INTRO = 0
GAME = 1
GAME_OVER = 2
game_state = INTRO
score = 0
game_time = 60


running = True

while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_SPACE:

                if game_state == INTRO:
                    game_state = GAME

                elif game_state == GAME:
                    fishing_rod.start()

    # Intro screen
    if game_state == INTRO:

        intro.draw_intro(
            screen,
            title_font,
            rule_font,
            WIDTH,
            HEIGHT
        )

    # Game screen
    elif game_state == GAME:

        # Draw ocean
        ocean.draw(screen)
        
        game_time -= dt

        if game_time <= 0:
            game_time = 0
            game_state = GAME_OVER

        # Update fish
        fish_manager.update(dt)

        # Update fishing rod
        fishing_rod.update(dt, fish_manager)
        
        for caught_fish in fishing_rod.caught_events:
            score += caught_fish.points

        fishing_rod.caught_events.clear()

        # Draw fish
        fish_manager.draw(screen)

        # Draw boat
        screen.blit(boat_image, (boat_x, boat_y))
        score_text = rule_font.render(
            f"Score: {score}", True, (255, 255, 255))

        screen.blit(score_text, (30, 30))
        
        timer_text = rule_font.render(
            f"Time: {int(game_time)}", True, (255, 255, 255))

        screen.blit(timer_text, (30, 75))

        # Draw fishing line
        fishing_rod.draw(screen)
    elif game_state == GAME_OVER:
        game_over.draw_game_over(
        screen,
        title_font,
        rule_font,
        WIDTH,
        HEIGHT,
        score
    )

    pygame.display.flip()

pygame.quit()

