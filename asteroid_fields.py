import sys

import pygame

class AsteroidFields:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""

        #Initialize te Pygame background settings.
        pygame.init()

        #Add the clock function to govern the frame rate
        self.clock = pygame.time.Clock()

        #Create a display window for the graphical elements.
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Asteroid Fields")

    def run_game(self):
        """Start the main loop for the game."""

        #The loop contains an event loop and manages screen updates.
        while True:
            #Monitor keyboard and mouse events.
            for event in pygame.event.get():
                #If the user clicks on the window close button:
                if event.type == pygame.QUIT:
                    sys.exit()
            #Make the most recently drawn screen visible.
            pygame.display.flip()

            #The tick() method takes one argument: the game frame rate
            self.clock.tick(60)
    
if __name__ == '__main__':
    # Make a game instance, and run the game. 
    af = AsteroidFields()
    af.run_game()