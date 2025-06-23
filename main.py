import pygame

pygame.init()

size = (750,750)
green=(57, 255, 20)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Window")

class Ball():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.vx = 0  # x velocity
        self.vy = 0  # y velocity
        self.radius = radius
        self.color = color
        self.gravity = 0.05  # gravity constant

    def apply_gravity(self):
        self.vy += self.gravity  # gravity pulls down (increases y velocity)
        self.y += self.vy  # apply velocity to position
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


height=size[0]
width=size[1]

center_x = width // 2
center_y = height // 2

ball = Ball(center_x, center_y, 15, (255, 255, 255)) # white ball

running = True
clock = pygame.time.Clock()  # Create a clock object to control frame rate
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, green, (center_x, center_y), 300)
    pygame.draw.circle(screen, (0,0,0), (center_x, center_y), 290)
    
    ball.apply_gravity()  # Apply gravity to the ball each frame
    ball.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()