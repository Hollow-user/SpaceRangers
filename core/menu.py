import pygame

from core import settings

click = False


class Button:
    def __init__(self, window, number, image):
        self.window = window
        self.image = pygame.image.load(image)
        self.x = settings.display_width/2 - 100
        self.y = settings.display_height/10 * number
        self.rect = pygame.Rect(self.x, self.y, 200, 50)

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

    def click(self, mx, my):
        if self.rect.collidepoint(mx, my):
            if click:
                return True
            else:
                return False


def handle_events(menu_events):
    global click
    for menu_event in menu_events:
        if menu_event.type == pygame.QUIT:
            pygame.quit()
        if menu_event.type == pygame.MOUSEBUTTONDOWN:
            if menu_event.button == 1:
                click = True


def start_menu(window):
    """ Стартовое меню """
    global click
    running = True
    button_start = Button(window, 1, 'images/buttons/start.png')
    button_exit = Button(window, 2, 'images/buttons/exit.png')
    buttons = (button_start, button_exit)
    while running:
        window.blit(settings.background2, (0, 0))
        for button in buttons:
            button.draw()
        mx, my = pygame.mouse.get_pos()
        menu_events = pygame.event.get()
        handle_events(menu_events)

        if button_start.click(mx, my):
            running = False
            click = False
        elif button_exit.click(mx, my):
            pygame.quit()

        pygame.display.update()
        click = False


def game_menu(window):
    """  Игровое меню """
    global click
    running = True
    button_resume_game = Button(window, 1, 'images/buttons/continue.png')
    button_exit = Button(window, 2, 'images/buttons/exit.png')
    buttons = (button_resume_game, button_exit)
    while running:
        window.blit(settings.background3, (0, 0))
        for button in buttons:
            button.draw()
        mx, my = pygame.mouse.get_pos()
        menu_events = pygame.event.get()
        handle_events(menu_events)

        if button_resume_game.click(mx, my):
            running = False
        elif button_exit.click(mx, my):
            pygame.quit()

        pygame.display.update()
        click = False


def end_menu(window, text, color):
    """ Меню в конце игры """
    running = True
    while running:
        window.blit(settings.background4, (0, 0))
        menu_events = pygame.event.get()
        handle_events(menu_events)

        text_font = pygame.font.Font(None, 30)
        render_text = text_font.render(text, 1, color)
        window.blit(render_text, (settings.display_width//2 - 70, settings.display_height//2 - 20))

        pygame.display.update()
