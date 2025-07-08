import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    playing = True
    player_spawn_x = SCREEN_WIDTH / 2
    player_spawn_y = SCREEN_HEIGHT / 2
    player = Player(player_spawn_x, player_spawn_y)
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Shot.containers = (bullets, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    AsteroidField()
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        for i in drawable:
            i.draw(screen)
        player.update(dt, bullets, updatable, drawable)
        for obj in updatable:
            if obj != player:
                obj.update(dt)
        for i in asteroids:
            for b in bullets:
                if i.checkcollision(b):
                    i.split()
                    b.kill()
        for i in asteroids:
            if i.checkcollision(player):
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        delta = clock.tick(60)
        dt = delta / 1000

if __name__ == "__main__":
    main()
