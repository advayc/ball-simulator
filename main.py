import pygame
import pygame.gfxdraw
import math

pygame.init()

size = (750,750)
green=(57, 255, 20)
screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("Gravity Collision Simulator")

class Ball():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.vx = 2  # initial x velocity
        self.vy = 0  # initial y velocity
        self.radius = radius
        self.color = color
        self.gravity = 0.2  # gravity constant
        self.bounce_damping = 0.85  # energy loss on collision

    def apply_physics(self):
        self.vy += self.gravity
        self.x += self.vx
        self.y += self.vy
        
        # check collision with green circle (inner boundary at radius 290)
        dx = self.x - center_x
        dy = self.y - center_y
        distance = math.sqrt(dx * dx + dy * dy)
        
        if distance + self.radius >= 290:
            # Calculate collision point
            collision_distance = 290 - self.radius
            
            # direction vector
            if distance > 0:
                nx = dx / distance
                ny = dy / distance
                
                self.x = center_x + nx * collision_distance
                self.y = center_y + ny * collision_distance
                
                # reflection
                dot_product = self.vx * nx + self.vy * ny
                self.vx = self.vx - 2 * dot_product * nx
                self.vy = self.vy - 2 * dot_product * ny
                
                # energy loss
                self.vx *= self.bounce_damping
                self.vy *= self.bounce_damping
        
        # Boundary collisions with window edges
        if self.x - self.radius <= 0 or self.x + self.radius >= size[0]:
            self.vx = -self.vx * self.bounce_damping
            if self.x - self.radius <= 0:
                self.x = self.radius
            else:
                self.x = size[0] - self.radius
                
        if self.y - self.radius <= 0 or self.y + self.radius >= size[1]:
            self.vy = -self.vy * self.bounce_damping
            if self.y - self.radius <= 0:
                self.y = self.radius
            else:
                self.y = size[1] - self.radius
        
    def draw(self, screen):
        pygame.gfxdraw.aacircle(screen, int(self.x), int(self.y), self.radius, self.color)
        pygame.gfxdraw.filled_circle(screen, int(self.x), int(self.y), self.radius, self.color)


height = size[0]
width = size[1]

center_x = width // 2
center_y = height // 2

ball = Ball(100, 100, 15, (255, 255, 255))

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  #reset game
                ball.x = 100
                ball.y = 100
                ball.vx = 2
                ball.vy = 0

    screen.fill((0, 0, 0))
    
    pygame.gfxdraw.aacircle(screen, center_x, center_y, 300, green)
    pygame.gfxdraw.filled_circle(screen, center_x, center_y, 300, green)
    
    # inner black 
    pygame.gfxdraw.aacircle(screen, center_x, center_y, 290, (0,0,0))
    pygame.gfxdraw.filled_circle(screen, center_x, center_y, 290, (0,0,0))
    
    ball.apply_physics()
    ball.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()