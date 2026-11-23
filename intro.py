
import pygame

# Colors
WHITE = (255, 255, 255)
LIGHT_BLUE = (153, 218, 231)
OCEAN_BLUE = (0, 160, 225)


def draw_intro(screen, font, small_font, width, height):

    screen.fill(LIGHT_BLUE)

    # Ocean water
    pygame.draw.rect(screen, OCEAN_BLUE,
                     (0, 180, width, height - 180))

    # Waves along the top of the ocean
    wave_points = [
        (0, 180), (40, 165), (120, 165),
        (190, 150), (270, 170), (400, 175),
        (520, 185), (650, 205), (750, 190),
        (880, 195), (960, 165), (1060, 165),
        (width, 190), (width, height),
        (0, height)
    ]

    pygame.draw.polygon(screen, OCEAN_BLUE, wave_points)

    # Title
    title = font.render("Reel Rush!", True, WHITE)
    title_rect = title.get_rect(center=(width // 2, 85))
    screen.blit(title, title_rect)

    # Underline
    pygame.draw.line(screen, WHITE,
                     (width // 2 - 255, 130),
                     (width // 2 + 255, 130), 5)

    # Rules
    rules = [
        "Rules:",
        "1. 60 seconds to catch as many fish",
        "   as possible",
        "2. Faster fish = more points",
        "3. Don't catch the dead fish!",
        "Press Space to Start!"
    ]

    y = 210

    for rule in rules:
        text = small_font.render(rule, True, WHITE)
        screen.blit(text, (85, y))
        y += 48

    # Start instructions
    start = small_font.render(
        "Press SPACE to start fishing!", True, WHITE
    )

    start_rect = start.get_rect(
        center=(width // 2, height - 65))