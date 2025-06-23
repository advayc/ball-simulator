import pygame
import pygame.gfxdraw
import math
import colorsys
import cv2
import numpy as np

pygame.init()

size = (1920, 1080)
green = (57, 255, 20)
white = (255, 255, 255)
screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("Gravity Collision Simulator")

# video settings for hd
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('simulation.mp4', fourcc, 60.0, (1920, 1080))

class Ball():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.vx = 12  # slightly faster initial x velocity
        self.vy = 0
        self.radius = radius
        self.color = color
        self.gravity = 0.7  # gravity constant
        self.bounce_damping = 1.0  # no energy loss or gain
        self.color_timer = 0
        self.growth_rate = 4.0  # higher growth rate
        self.growth_accumulator = 0  # for fractional growth

    def update_rainbow_color(self):
        self.color_timer += 1
        
        rainbow_colors = []
        for i in range(8):
            hue = (i * 60 + self.color_timer) % 360
            hue_normalized = hue / 360.0
            rgb = colorsys.hsv_to_rgb(hue_normalized, 1.0, 1.0)
            rainbow_colors.append((int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)))
        
        self.color = rainbow_colors[0]

    def grow(self):
        # smoother growth with accumulator
        self.growth_accumulator += self.growth_rate
        
        # only increase radius when accumulator reaches 1.0 or more
        while self.growth_accumulator >= 1.0:
            self.radius += 1
            self.growth_accumulator -= 1.0
            
        self.radius = min(self.radius, boundary_radius)
        # return true if ball has reached maximum size
        return self.radius >= boundary_radius

    def apply_physics(self):
        self.vy += self.gravity
        self.x += self.vx
        self.y += self.vy
        
        self.update_rainbow_color()
        
        collision_occurred = False
        
        dx = self.x - center_x
        dy = self.y - center_y
        distance = math.sqrt(dx * dx + dy * dy)
        
        if distance + self.radius >= boundary_radius:
            # calculate collision point
            collision_distance = boundary_radius - self.radius
            
            if distance > 0:
                nx = dx / distance
                ny = dy / distance
                
                self.x = center_x + nx * collision_distance
                self.y = center_y + ny * collision_distance
                
                # perfect reflection with no energy loss
                dot_product = self.vx * nx + self.vy * ny
                self.vx = (self.vx - 2 * dot_product * nx) * self.bounce_damping
                self.vy = (self.vy - 2 * dot_product * ny) * self.bounce_damping
                
                collision_occurred = True
        
        # boundary collisions with window edges
        if self.x - self.radius <= 0 or self.x + self.radius >= size[0]:
            self.vx = -self.vx * self.bounce_damping
            if self.x - self.radius <= 0:
                self.x = self.radius
            else:
                self.x = size[0] - self.radius
            collision_occurred = True
                
        if self.y - self.radius <= 0 or self.y + self.radius >= size[1]:
            self.vy = -self.vy * self.bounce_damping
            if self.y - self.radius <= 0:
                self.y = self.radius
            else:
                self.y = size[1] - self.radius
            collision_occurred = True
            
        # grow on collision and return whether max size is reached
        return self.grow() if collision_occurred else False
        
    def draw(self, screen):
        pygame.gfxdraw.aacircle(screen, int(self.x), int(self.y), self.radius, self.color)
        pygame.gfxdraw.filled_circle(screen, int(self.x), int(self.y), self.radius, self.color)


height = size[1]
width = size[0]

center_x = width // 2
center_y = height // 2

# set boundary radius as a global constant
boundary_radius = min(size[0], size[1]) // 2 - 100

ball = Ball(center_x - 400, center_y, 30, white)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # draw outer boundary
    pygame.gfxdraw.aacircle(screen, center_x, center_y, boundary_radius + 10, green)
    pygame.gfxdraw.filled_circle(screen, center_x, center_y, boundary_radius + 10, green)
    
    # inner black
    pygame.gfxdraw.aacircle(screen, center_x, center_y, boundary_radius, (0,0,0))
    pygame.gfxdraw.filled_circle(screen, center_x, center_y, boundary_radius, (0,0,0))

    # update and draw ball
    max_size_reached = ball.apply_physics()
    ball.draw(screen)
    
    pygame.display.flip()
    
    # capture frame for video in hd
    string_image = pygame.image.tostring(screen, 'RGB')
    temp_surf = np.frombuffer(string_image, dtype=np.uint8)
    temp_surf = temp_surf.reshape((1080, 1920, 3))
    out.write(cv2.cvtColor(temp_surf, cv2.COLOR_RGB2BGR))
    
    # end the simulation if ball reaches maximum size
    if max_size_reached:
        running = False
    
    clock.tick(60)

# clean up
out.release()
pygame.quit()