
import random

import pygame

from core import menu, settings


class Bullet:

    def __init__(self, window, x, y, color, direction):
        self.window = window
        self.x = x
        self.y = y
        self.radius = 5
        self.color = color
        self.direction = direction

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)

    def check_hit(self, models):
        for model in models:
            if model.x <= self.x <= model.x + model.width:
                if model.y <= self.y <= model.y + model.height:
                    model.hp -= 10
                    return True
        return False


class Player:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.x = 200
        self.y = 300
        self.width = 50
        self.height = 50
        self.speed = 5
        self.hp = 100
        self.img = pygame.image.load('images/ships/6.png')
        self.bullet_list = []

    def draw_name(self):
        text_font = pygame.font.Font(None, 30)
        render_text = text_font.render(self.name, 1, pygame.Color('Green'))
        self.window.blit(render_text, (self.x - 15, self.y - 15))

    def draw_hp(self):
        text_font = pygame.font.Font(None, 30)
        render_text = text_font.render(str(self.hp), 1, pygame.Color('Green'))
        self.window.blit(render_text, (0, settings.display_height - 20))

    def shout(self):
        if len(self.bullet_list) < 5:
            self.bullet_list.append(Bullet(self.window, self.x + (self.width//2), self.y, pygame.Color('Green'), 1))

    def die(self):
        if self.hp <= 0:
            menu.end_menu(self.window, 'Вы проиграли', pygame.color.Color('Red'))


class Enemy:

    def __init__(self, window):
        self.window = window
        self.name = 'Enemy'
        self.x = 250
        self.y = 50
        self.width = 50
        self.height = 50
        self.speed = 10
        self.hp = 100
        self.img = pygame.image.load('images/ships/7.png')
        self.bullet_list = []
        self.turn = 'left'
        self.shooting = False

    def draw_name(self):
        text_font = pygame.font.Font(None, 30)
        render_text = text_font.render(self.name, 1, pygame.Color('Red'))
        self.window.blit(render_text, (self.x - 15, self.y - 15))

    def draw_hp(self):
        text_font = pygame.font.Font(None, 30)
        render_text = text_font.render(str(self.hp), 1, pygame.Color('Red'))
        self.window.blit(render_text, (0, 5))

    def shout(self):
        self.shooting = random.choice([True, False, False, False, False, False])
        if len(self.bullet_list) < 25 and self.shooting:
            self.bullet_list.append(Bullet(self.window, self.x + (self.width // 2), self.y + self.height,
                                           pygame.Color('Red'), (-1)))

    def move(self):
        if self.turn == 'left':
            if self.x > 10:
                self.x -= self.speed
            else:
                self.turn = 'right'
        else:
            if self.x < (settings.display_width - 10):
                self.x += self.speed
            else:
                self.turn = 'left'

    def die(self):
        if self.hp <= 0:
            menu.end_menu(self.window, 'Вы победили', pygame.color.Color('Green'))
