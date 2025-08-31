import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
#    print("Starting Asteroids!")
#    print(f"Screen width: {constants.SCREEN_WIDTH}")
#    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    game_tick_control = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    delta_time = 0

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (bullets, updatable, drawable)

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(delta_time)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                return
            
            for bullet in bullets:
                if asteroid.check_collision(bullet):
                    asteroid.split()
                    bullet.kill()

        screen.fill("black")
        for to_draw in drawable:
            to_draw.draw(screen)
        pygame.display.flip()
        delta_time = game_tick_control.tick(60) / 1000


if __name__ == "__main__":
    main()
