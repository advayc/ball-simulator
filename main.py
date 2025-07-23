import pygame
import math
import colorsys
import asyncio
import random
import sys

# Check if running in browser
is_web = 'pytest' in sys.modules or 'PYGBAG' in sys.modules or '__EMSCRIPTEN__' in sys.modules

# Initialize pygame for web compatibility
pygame.init()
pygame.font.init()

# Set up display with proper flags for web
flags = pygame.RESIZABLE if is_web else 0
size = (800, 600)
green = (57, 255, 20)
white = (255, 255, 255)
screen = pygame.display.set_mode(size, flags)
pygame.display.set_caption("Ball Animation Simulator")

# UI Setup
font = pygame.font.Font(None, 24)
button_height = 30
button_padding = 5

# Animation styles
STYLES = {
    'Rainbow': {'color_change': True, 'trail': False, 'pulse': False, 'particles': False},
    'Neon Pulse': {'color_change': True, 'trail': False, 'pulse': True, 'particles': False},
    'Particle Trail': {'color_change': True, 'trail': True, 'particles': True, 'pulse': False},
    'Classic': {'color_change': False, 'trail': False, 'pulse': False, 'particles': False}
}

current_style = 'Rainbow'

class Ball():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.vx = 12
        self.vy = 0
        self.radius = radius
        self.base_radius = radius
        self.color = color
        self.base_color = color
        self.gravity = 0.7
        self.color_timer = 0
        self.growth_rate = 4.0
        self.growth_accumulator = 0
        self.pulse_phase = 0
        self.trail = []
        self.particles = []
        
    def update_color(self):
        style = STYLES[current_style]
        if style['color_change']:
            self.color_timer += 0.95
            hue = (self.color_timer) % 360
            hue_normalized = hue / 360.0
            rgb = colorsys.hsv_to_rgb(hue_normalized, 1.0, 1.0)
            self.color = (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
        else:
            self.color = self.base_color
            
        if style['pulse']:
            self.pulse_phase = (self.pulse_phase + 0.1) % (2 * math.pi)
            pulse_factor = 1 + 0.2 * math.sin(self.pulse_phase)
            self.radius = int(self.base_radius * pulse_factor)
        
        if style['trail']:
            self.trail.append(((self.x, self.y), self.color))
            if len(self.trail) > 10:
                self.trail.pop(0)

    def grow(self):
        self.growth_accumulator += self.growth_rate
        
        while self.growth_accumulator >= 1.0:
            self.radius += 1
            self.growth_accumulator -= 1.0
            
        self.radius = min(self.radius, boundary_radius)
        return self.radius >= boundary_radius

    def apply_physics(self):
        self.vy += self.gravity
        self.x += self.vx
        self.y += self.vy
        self.update_color()
        
        collision_occurred = False
        
        dx = self.x - center_x
        dy = self.y - center_y
        distance = math.sqrt(dx * dx + dy * dy)
        
        if distance + self.radius >= boundary_radius:
            collision_distance = boundary_radius - self.radius
            
            if distance > 0:
                nx = dx / distance
                ny = dy / distance
                
                self.x = center_x + nx * collision_distance
                self.y = center_y + ny * collision_distance
                
                dot_product = self.vx * nx + self.vy * ny
                self.vx = (self.vx - 2 * dot_product * nx)
                self.vy = (self.vy - 2 * dot_product * ny)
                
                if STYLES[current_style]['particles']:
                    self.add_collision_particles()
                collision_occurred = True
        
        if self.x - self.radius <= 0 or self.x + self.radius >= size[0]:
            self.vx = -self.vx
            if self.x - self.radius <= 0:
                self.x = self.radius
            else:
                self.x = size[0] - self.radius
            
            if STYLES[current_style]['particles']:
                self.add_collision_particles()
            collision_occurred = True
                
        if self.y - self.radius <= 0 or self.y + self.radius >= size[1]:
            self.vy = -self.vy
            if self.y - self.radius <= 0:
                self.y = self.radius
            else:
                self.y = size[1] - self.radius
            
            if STYLES[current_style]['particles']:
                self.add_collision_particles()
            collision_occurred = True
            
        # Update particles
        if STYLES[current_style]['particles']:
            self.update_particles()
            
        return self.grow() if collision_occurred else False
    
    def add_collision_particles(self):
        for _ in range(5):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 5)
            self.particles.append({
                'x': self.x,
                'y': self.y,
                'vx': math.cos(angle) * speed,
                'vy': math.sin(angle) * speed,
                'life': 1.0,
                'color': self.color
            })
    
    def update_particles(self):
        for particle in self.particles[:]:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 0.05
            if particle['life'] <= 0:
                self.particles.remove(particle)
        
    def draw(self, screen):
        style = STYLES[current_style]
        
        # Draw trail
        if style['trail']:
            for i, ((x, y), color) in enumerate(self.trail):
                alpha = (i + 1) / len(self.trail)
                pygame.draw.circle(screen, color, (int(x), int(y)), 
                                int(self.radius * alpha))
        
        # Draw particles
        if style['particles']:
            for particle in self.particles:
                alpha = int(255 * particle['life'])
                color = (*particle['color'][:3], alpha)
                pygame.draw.circle(screen, color, 
                                (int(particle['x']), int(particle['y'])), 3)

def draw_buttons():
    global current_style
    y = 10
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()[0]
    
    button_rects = {}  # Store button rectangles for event handling
    
    for style in STYLES.keys():
        button_rect = pygame.Rect(10, y, 150, button_height)
        button_rects[style] = button_rect
        color = (100, 200, 100) if style == current_style else (70, 70, 70)
        
        # Hover effect
        if button_rect.collidepoint(mouse_pos):
            color = (150, 255, 150) if style == current_style else (100, 100, 100)
            if mouse_clicked:
                current_style = style
        
        pygame.draw.rect(screen, color, button_rect)
        pygame.draw.rect(screen, (200, 200, 200), button_rect, 1)
        
        text = font.render(style, True, (255, 255, 255))
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)
        
        y += button_height + button_padding
    
    return button_rects

height = size[1]
width = size[0]

center_x = width // 2
center_y = height // 2
boundary_radius = min(size[0], size[1]) // 2 - 100

ball = Ball(center_x - 200, center_y, 15, white)
clock = pygame.time.Clock()

async def main():
    global center_x, center_y, boundary_radius, size, width, height, screen
    running = True
    
    while running:
        # Handle Pygame events properly for web
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                # Handle resizing for web browser
                size = (event.w, event.h)
                width, height = size
                screen = pygame.display.set_mode(size, pygame.RESIZABLE)
                center_x = width // 2
                center_y = height // 2
                boundary_radius = min(width, height) // 2 - 100
            elif event.type == pygame.FINGERDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                # Handle touch/mouse events for button clicks
                pos = pygame.mouse.get_pos() if event.type == pygame.MOUSEBUTTONDOWN else (event.x * width, event.y * height)
                for style, rect in button_rects.items():
                    if rect.collidepoint(pos):
                        current_style = style
                        break

        screen.fill((0, 0, 0))

        # Draw boundary
        pygame.draw.circle(screen, green, (center_x, center_y), boundary_radius + 10)
        pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), boundary_radius)

        # Update and draw ball
        max_size_reached = ball.apply_physics()
        ball.draw(screen)
        
        # Draw UI
        button_rects = draw_buttons()
        
        pygame.display.flip()
        
        if max_size_reached:
            # Reset the ball for continuous demo
            ball.x = center_x - 200
            ball.y = center_y
            ball.radius = ball.base_radius
            ball.vx = 12  # Restored to original speed
            ball.vy = 0
            ball.growth_accumulator = 0
            ball.trail.clear()
            ball.particles.clear()
            print(f"Ball reset with style: {current_style}")
        
        # Web-friendly timing
        clock.tick(60)
        await asyncio.sleep(0)

    pygame.quit()

# Handle web platform correctly
if __name__ == "__main__":
    asyncio.run(main())
