import pygame

def main():
    width = 510
    height = 480
    background_image = pygame.image.load("images/background.png")
    hero_image = pygame.image.load("images/hero.png")
    monster_image = pygame.image.load("images/monster.png")


    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Cristine\'s Monster Game') # Set the window bar title
    clock = pygame.time.Clock()


    # Game initialization
    monster_x = 50
    monster_y = 50

    stop_game = False

    while not stop_game:
        for event in pygame.event.get(): #even handling loop that handles user input
            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        monster_x += 1

        # Draw background
        screen.blit(background_image, (0,0))
        screen.blit(hero_image, (251, 230))
        screen.blit(monster_image, (monster_x, 40))

        # Game display
        pygame.display.update() # updates entire surface as long as no parameter
        clock.tick(60) # frames per second.



    pygame.quit() # this stops python game from running.

if __name__ == '__main__':
    main()
