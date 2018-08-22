#Create an initial settings class

class Settings():
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialise the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)
        
        # Ship settings
        #self.ship_speed_factor = 1.5
        self.ship_limit = 2
        
        # Bullet settings
        #self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)        
        self.bullets_allowed = 3
        
        # Alien settings
        #self.alien_speed = 0.75
        self.fleet_drop_speed = 10
        #self.fleet_direction = 1
        
        # How quickly the game speeds up
        self.speedup_scale = 1.4
        self.score_scale = 1.5
        
        self.initialise_dynamic_settings()
        
    def initialise_dynamic_settings(self):
        """Initialise settings that change through the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed = 0.75
        self.fleet_direction = 1
        
        # Scoring
        self.alien_points = 50
        
    def increase_speed(self):
        """Increase speed settings and alien points."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
