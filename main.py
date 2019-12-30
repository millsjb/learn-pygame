import os
import pygame
from pygame.locals import *
from pygame.compat import geterror

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')

# functions to create our resources
def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(data_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print('Cannot load sound: %s' % fullname)
        raise SystemExit(str(geterror()))
    return sound

class App():
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
        self._clock = None
        self._allsprites = None
    
    def on_init(self):
        # init screen
        pygame.init()
        self._screen = pygame.display.set_mode(self.size, pygame.SWSURFACE)
        pygame.display.set_caption('Sneaky Snake')
        pygame.mouse.set_visible(0)
        self._running = True

        # fill background
        self._background = pygame.Surface(self._screen.get_size())
        self._background = self._background.convert()
        self._background.fill((10, 10, 10))

        # Put Text On The Background, Centered
        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render("Welcome to Snake!", 1, (255, 0, 0))
            textpos = text.get_rect(centerx=self._background.get_width()/2)
            textpos.top = 6
            self._background.blit(text, textpos)

        # build container for snake
        width, height = self._screen.get_size()
        container = pygame.Surface((width, height-36))
        container = container.convert()
        container.fill((250, 250, 250))

        # display some more text within container
        cont_text = font.render("This is the place where the snake will roam.", 1, (115, 194, 251)) 
        cont_text_pos = cont_text.get_rect()
        cont_text_pos.centerx = container.get_rect().centerx
        cont_text_pos.centery = container.get_rect().centery
        container.blit(cont_text, cont_text_pos)
        self._background.blit(container, (0, 42))

        # Display The Background
        self._screen.blit(self._background, (0, 0))
        pygame.display.flip()

        # Prepare Game Objects
        self._clock = pygame.time.Clock()
        collision_sound = load_sound('whiff.wav')
        snake = Snake()
        self._allsprites = pygame.sprite.RenderPlain((snake))

    def on_event(self, event):
        """handle input events"""
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            self._running = False
        
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
            self._clock.tick(60)

            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()
            self._allsprites.update()

            # blit everything to the screen
            self._screen.blit(self._background, (0,0))
            self._allsprites.draw(self._screen)
            pygame.display.flip()
        
        self.on_cleanup()

class Snake(pygame.sprite.Sprite):
    """moves a growing snake across the screen"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image, self.rect = load_image('alien1.gif', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 80
        self.move = 9

    def update(self):
        """move the snake one position"""
        self._slither()

    def _slither(self):
        newpos = self.rect.move((self.move, 0))

        if not self.area.contains(newpos):
            if self.rect.left < self.area.left \
                    or self.rect.right > self.area.right \
                    or self.rect.top < self.area.top \
                    or self.rect.bottom > self.area.bottom:
                self.move = -self.move # reverse the offset
                newpos = self.rect.move((self.move, 0))
                self.image = pygame.transform.flip(self.image, 1, 0)
            self.rect = newpos

if __name__ == "__main__":
    app = App()
    app.on_execute()

