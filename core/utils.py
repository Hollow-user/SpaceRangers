
import pygame

from core import menu, settings


def draw_window(window, models):
    """ Отображение обьектов на окне """
    window.blit(settings.background1, (0, 0))

    for model in models:
        window.blit(model.img, (model.x, model.y))
        model.draw_name()
        model.draw_hp()
        for bullet in model.bullet_list:
            bullet.draw()

    pygame.display.update()  # Обновление окна чтобы видеть изменения


def key_pressed(keys, window, player):
    """ Проверяем нажатие и определяем действие """
    if keys[pygame.K_LEFT] and player.x > player.speed:
        player.x -= player.speed
    if keys[pygame.K_RIGHT] and player.x < (settings.display_width - player.speed - player.width):
        player.x += player.speed
    if keys[pygame.K_UP] and player.y > player.speed:
        player.y -= player.speed
    if keys[pygame.K_DOWN] and player.y < (settings.display_height - player.speed - player.height):
        player.y += player.speed
    if keys[pygame.K_SPACE]:
        player.shout()
    if keys[pygame.K_ESCAPE]:
        menu.game_menu(window)
