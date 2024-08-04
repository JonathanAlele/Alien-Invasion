class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's setttings"""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.background_colour = (110, 110, 110)

        # Ship settings
        self.ship_speed = 5.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 3
