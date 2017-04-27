import pygame
# global variables
background_image = pygame.image.load("images/background.png")
hero_image = pygame.image.load("images/hero.png")

def main():
    width = 510
    height = 480
    blue_color = (78, 94, 78)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Cristine\'s Monster Game') # Set the window bar title
    clock = pygame.time.Clock()

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(blue_color)
        screen.blit(background_image, (0,0))
        screen.blit(hero_image, (255, 240))
        

        # Game display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
