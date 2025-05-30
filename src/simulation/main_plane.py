import pygame as pg


global bg_color


class Plane:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    FPS = 60
    bg_color = WHITE

    def __init__(self, width, height):
        self.size = (width, height)

    def render_plane(self):
        # pygame setup
        pg.init()
        screen = pg.display.set_mode(self.size)
        clock = pg.time.Clock()
        running = True
        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            # fill the screen with a color to wipe away anything from last frame
            screen.fill(self.bg_color)

            # flip() the display to put your work on screen
            pg.display.flip()

            clock.tick(self.FPS)  # limits FPS
        print('Program closed(((')
        pg.quit()

    def close_plane(self):
        print('Program closed!')
        pg.quit()


plane = Plane(1200, 720)
plane.render_plane()
plane.close_plane()
