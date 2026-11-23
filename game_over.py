
import pygame

WHITE = (255, 255, 255)
OCEAN_BLUE = (0, 160, 225)
LIGHT_BLUE = (153, 218, 231)


def draw_game_over(screen, title_font, rule_font, width, height, score):

    screen.fill(LIGHT_BLUE)

    pygame.draw.rect(
        screen,
        OCEAN_BLUE,
        (0, 180, width, height - 180)
    )

    title = title_font.render("GAME OVER!", True, WHITE)
    title_rect = title.get_rect(center=(width // 2, 200))
    screen.blit(title, title_rect)

    score_text = rule_font.render(
        f"Final Score: {score}", True, WHITE
    )
    score_rect = score_text.get_rect(
        center=(width // 2, 340)
    )
    screen.blit(score_text, score_rect)

    message = rule_font.render(
        "Thanks for playing Reel Rush!", True, WHITE
    )
    message_rect = message.get_rect(
        center=(width // 2, 430)
    )
    screen.blit(message, message_rect)

    restart = rule_font.render(
        "Press ESC to quit", True, WHITE
    )
    restart_rect = restart.get_rect(
        center=(width // 2, 550)
    )
    screen.blit(restart, restart_rect)
