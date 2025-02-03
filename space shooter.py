import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Load assets
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
bullet_img = pygame.image.load("bullet.png")

# Player setup
player = pygame.Rect(WIDTH//2 - 25, HEIGHT - 100, 50, 50)
player_speed = 5

# Enemy setup
enemies = []
enemy_speed = 3

# Bullet setup
bullets = []
bullet_speed = -7

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append(pygame.Rect(player.x + 20, player.y, 10, 20))
    
    # Move bullets
    for bullet in bullets[:]:
        bullet.y += bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)
    
    # Spawn enemies
    if random.randint(1, 50) == 1:
        enemies.append(pygame.Rect(random.randint(0, WIDTH - 50), 0, 50, 50))
    
    # Move enemies
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
    
    # Check for collisions
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break
    
    # Draw player
    screen.blit(player_img, (player.x, player.y))
    
    # Draw enemies
    for enemy in enemies:
        screen.blit(enemy_img, (enemy.x, enemy.y))
    
    # Draw bullets
    for bullet in bullets:
        screen.blit(bullet_img, (bullet.x, bullet.y))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
