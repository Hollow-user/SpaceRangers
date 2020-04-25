
import pygame

from core import menu, settings, utils
from core.models import Enemy, Player

pygame.init()

window = pygame.display.set_mode((settings.display_width, settings.display_height))  # Окно для игры
pygame.display.set_caption(settings.title)  # Задаем имя для нашего окна с игрой
clock = pygame.time.Clock()  # Создаем часы


def start_game():
    player = Player(window, settings.player_name)
    enemy = Enemy(window)
    models = [player, enemy]

    menu.start_menu(window)
    while True:
        clock.tick(settings.max_fps)

        for model in models:
            model.die()
            for bullet in model.bullet_list:
                if 0 < bullet.y < settings.display_height:
                    bullet.y -= bullet.direction * settings.game_speed * 2
                    if bullet.check_hit(models):
                        model.bullet_list.remove(bullet)
                else:
                    model.bullet_list.remove(bullet)

        enemy.shout()
        enemy.move()

        keys = pygame.key.get_pressed()
        utils.key_pressed(keys, window, player)
        utils.draw_window(window, models)

        for event in pygame.event.get():  # Проверка на события происходящие в окне игры
            if event.type == pygame.QUIT:
                """ проверяем событие нажатие на крестик"""
                pygame.quit()


if __name__ == '__main__':
    start_game()
