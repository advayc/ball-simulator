import pygame
import pygame.gfxdraw
import math
import colorsys
import asyncio

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=2048)

size = (1920, 1080)
green = (57, 255, 20)
white = (255, 255, 255)
screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("Gravity Collision Simulator")

full_song = None
song_length = 0
segment_duration = 0.2
total_segments = 0
current_segment_index = 0
last_collision_time = 0
last_play_time = 0
is_playing = False

try:
    full_song = pygame.mixer.Sound('UNITY.mp3')
    song_length = full_song.get_length()
    total_segments = int(song_length / segment_duration)
    print(f"Loaded audio: {song_length:.2f} seconds, {total_segments} segments")
except Exception as e:
    print(f"Error loading audio: {e}")
    full_song = None

class Ball():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.vx = 12
        self.vy = 0
        self.radius = radius
        self.color = color
        self.gravity = 0.7
        self.color_timer = 0
        self.growth_rate = 4.0
        self.growth_accumulator = 0

    def update_rainbow_color(self):
        self.color_timer += 0.95
        
        rainbow_colors = []
        for i in range(8):
            hue = (i * 60 + self.color_timer) % 360
            hue_normalized = hue / 360.0
            rgb = colorsys.hsv_to_rgb(hue_normalized, 1.0, 1.0)
            rainbow_colors.append((int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255)))
        
        self.color = rainbow_colors[0]

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
        self.update_rainbow_color()
        
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
                
                play_collision_sound()
                collision_occurred = True
        
        if self.x - self.radius <= 0 or self.x + self.radius >= size[0]:
            self.vx = -self.vx
            if self.x - self.radius <= 0:
                self.x = self.radius
            else:
                self.x = size[0] - self.radius
            
            play_collision_sound()
            collision_occurred = True
                
        if self.y - self.radius <= 0 or self.y + self.radius >= size[1]:
            self.vy = -self.vy
            if self.y - self.radius <= 0:
                self.y = self.radius
            else:
                self.y = size[1] - self.radius
            
            play_collision_sound()
            collision_occurred = True
            
        return self.grow() if collision_occurred else False
        
    def draw(self, screen):
        pygame.gfxdraw.aacircle(screen, int(self.x), int(self.y), self.radius, self.color)
        pygame.gfxdraw.filled_circle(screen, int(self.x), int(self.y), self.radius, self.color)

def play_collision_sound():
    global last_collision_time, current_segment_index, last_play_time, is_playing
    
    current_time = pygame.time.get_ticks()
    
    if current_time - last_collision_time > 200 and full_song and total_segments > 0:
        pygame.mixer.stop()
        is_playing = False
        
        channel = pygame.mixer.find_channel()
        if channel:
            start_time = (current_segment_index * segment_duration) % song_length
            
            channel.play(full_song)
            pygame.time.set_timer(pygame.USEREVENT + 1, int(segment_duration * 1000), True)
            
            is_playing = True
            last_play_time = current_time
            last_collision_time = current_time
            current_segment_index = (current_segment_index + 1) % total_segments
            
            print(f"Playing segment {current_segment_index}/{total_segments} at {start_time:.2f}s")

height = size[1]
width = size[0]

center_x = width // 2
center_y = height // 2
boundary_radius = min(size[0], size[1]) // 2 - 100

ball = Ball(center_x - 400, center_y, 30, white)
clock = pygame.time.Clock()

async def main():
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.USEREVENT + 1:
                pygame.mixer.stop()
                is_playing = False

        screen.fill((0, 0, 0))

        pygame.gfxdraw.aacircle(screen, center_x, center_y, boundary_radius + 10, green)
        pygame.gfxdraw.filled_circle(screen, center_x, center_y, boundary_radius + 10, green)
        
        pygame.gfxdraw.aacircle(screen, center_x, center_y, boundary_radius, (0,0,0))
        pygame.gfxdraw.filled_circle(screen, center_x, center_y, boundary_radius, (0,0,0))

        max_size_reached = ball.apply_physics()
        ball.draw(screen)
        
        pygame.display.flip()
        
        if max_size_reached:
            running = False
        
        clock.tick(60)
        await asyncio.sleep(0)

    pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())
