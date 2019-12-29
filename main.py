import pygame
from pygame.locals import *

class App:
    """
    This class holds all logic for a simple game of snake.

    There are three objects in play: top text rect, snake container,
    and snake itself.
    """
    def __init__(self):
        self._running = True
        self._screen = None
        self._background = None
        self.size = self.weight, self.height = 640, 400
    
    def on_init(self):
        # init screen
        pygame.init()
        self._screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        # fill background
        self._background = pygame.Surface(self._screen.get_size())
        self._background = self._background.convert()
        self._background.fill((10, 10, 10))

        # display some text
        font = pygame.font.Font(None, 36)
        text = font.render("Welcome to Snake!", 1, (255, 0, 0))
        textpos = text.get_rect()
        textpos.centerx = self._background.get_rect().centerx
        textpos.top = 6
        self._background.blit(text, textpos)

        # build container for snake
        width, height = self._screen.get_size()
        container = pygame.Surface((width, height-36))
        container = container.convert()
        container.fill((10, 10, 10))

        # display some more text within container
        cont_text = font.render("This is the place where the snake will roam.", 1, (115, 194, 251)) 
        cont_text_pos = cont_text.get_rect()
        cont_text_pos.centerx = container.get_rect().centerx
        cont_text_pos.centery = container.get_rect().centery
        container.blit(cont_text, cont_text_pos)
        self._background.blit(container, (0, 42))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        # blit everything to the screen
        self._screen.blit(self._background, (0,0))
        pygame.display.flip()

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        
        self.on_cleanup()

if __name__ == "__main__":
    app = App()
    app.on_execute()

