# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    total_score = 0
    total_lives = 3

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Score label
    # pygame.display.set_caption("Score Label")
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if player.imune <= 0 and asteroid.collides_with(player):
                player.imune = 2
                total_lives -= 1
                if total_lives == 0:
                    print("Game over!")
                    print(f"Total score: {total_score}")
                    sys.exit()

            for shot in shots:
                if shot.collides_with(asteroid):
                    total_score += 100
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        score_text = font.render(f"Score: {total_score}", True, "white")
        lives_text = font.render(f"Lives: {total_lives}", True, "white")
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, SCREEN_HEIGHT - 30))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # 60 FPS limit
        dt = clock.tick(60) / 1000 

if __name__ == "__main__":
    main()