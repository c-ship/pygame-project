import pygame
import random

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275


class Monster:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.x_dir = 1
        self.y_dir = 1
        self.x_speed = 5
        self.y_speed = 5

    def move_monster(self, width, height, count):
        self.x += self.x_dir * self.x_speed
        self.y += self.y_dir * self.y_speed
        if self.x > width:
            self.x = 0
        if self.x < 0:
            self.x = width
        if self.y > height:
            self.y = 0
        if self.y < 0:
            self.y = height
        if count == 0:
            self.x_dir = random.randrange(-10, 11, 1) / 10
            self.y_dir = random.randrange(-10, 11, 1) / 10


    def display(self, screen):
        monster_image = pygame.image.load("images/monster.png")
        screen.blit(monster_image, (self.x, self.y))

def main():
    width = 510
    height = 480
    background_image = pygame.image.load("images/background.png")
    hero_image = pygame.image.load("images/hero.png")

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Cristine\'s Monster Game') # Set the window bar title
    clock = pygame.time.Clock()

    hero_x = 251
    hero_y = 230
    hero_speed_x = 20
    hero_speed_y = 20
    monster = Monster()
    change_dir_countdown = 120


    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    hero_y += 5
                elif event.key == KEY_UP:
                    hero_y -= 5
                elif event.key == KEY_LEFT:
                    hero_x -= 5
                elif event.key == KEY_RIGHT:
                    hero_x += 5
            if hero_x > 500:
                hero_speed_x = 0
            if hero_x < 10:
                hero_speed_x = 0
            if hero_y > 300:
                hero_speed_y = 0
            if hero_y < 10:
                hero_speed_y = 0


            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic
        monster.move_monster(width, height, change_dir_countdown)
        change_dir_countdown -= 1
        if change_dir_countdown == 0:
            change_dir_countdown = 120




        # Draw background
        screen.blit(background_image, (0,0))
        screen.blit(hero_image, (hero_x, hero_y))
        monster.display(screen)


        # Game display
        pygame.display.update() # updates entire surface as long as no parameter
        clock.tick(60) # frames per second.



    pygame.quit() # this stops python game from running.

if __name__ == '__main__':
    main()
