import sys
import pygame
from settings import Settings
from ship import Ship
class AlienInvasion:
    """Overall class to manage game assests and behaviour"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #watching for keyboard and mouse events
            self._check_events()
            self.ship.update()
            self._update_screen()
            #make the most recently drawn screen visible
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """Responds to keydown events"""
        if event.key == pygame.K_RIGHT:
            #move the ship to the right
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            #move the ship to the left
            self.ship.moving_left = True

    def _check_keyup_events(self,event):
        """Responds to keyup events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on teh screen and flip to the new screen"""
        self.screen.fill(self.settings.background_colour)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()