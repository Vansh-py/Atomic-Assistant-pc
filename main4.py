import pygame
import math

# Initialize Pygame
pygame.init()

# Constants for colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
CENTER_X, CENTER_Y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
RADIUS = 200  # Radius of the largest orbit

# Electron distribution based on the 2, 8, 8 rule
ELECTRON_DISTRIBUTION = [2, 8, 8, 18, 18, 32, 32]

# Ask user for number of electrons
num_electrons = int(input("Enter the number of electrons: "))

# Calculate electron distribution
def calculate_electron_distribution(num_electrons):
    distribution = []
    for electrons_in_orbit in ELECTRON_DISTRIBUTION:
        if num_electrons > 0:
            electrons = min(num_electrons, electrons_in_orbit)
            distribution.append(electrons)
            num_electrons -= electrons
        else:
            break
    return distribution

electron_distribution = calculate_electron_distribution(num_electrons)

# Class for nucleus
class Nucleus:
    def __init__(self):
        self.x, self.y = CENTER_X, CENTER_Y
        self.radius = 15  # Radius of the nucleus

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

# Class for electron
class Electron:
    def __init__(self, orbit_radius, angle, speed, color=BLUE):
        self.orbit_radius = orbit_radius
        self.angle = angle
        self.speed = speed
        self.color = color
        self.radius = 5  # Radius of the electron

    def update(self):
        self.angle += self.speed  # Update angle to simulate movement
        if self.angle >= 2 * math.pi:
            self.angle -= 2 * math.pi

    def draw(self, screen):
        x = CENTER_X + int(self.orbit_radius * math.cos(self.angle))
        y = CENTER_Y + int(self.orbit_radius * math.sin(self.angle))
        pygame.draw.circle(screen, self.color, (x, y), self.radius)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Atom Simulation')

# Create nucleus
nucleus = Nucleus()

# Create electrons in different orbits
electrons = []
orbit_radius_increment = 50
speed = 0.02  # Constant speed for all electrons
current_radius = orbit_radius_increment

for orbit, num_electrons in enumerate(electron_distribution):
    angle_increment = 2 * math.pi / num_electrons
    for i in range(num_electrons):
        angle = i * angle_increment
        electrons.append(Electron(orbit_radius=current_radius, angle=angle, speed=speed))
    current_radius += orbit_radius_increment

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update electrons
    for electron in electrons:
        electron.update()

    # Draw everything
    screen.fill(WHITE)
    
    # Draw orbits
    for r in range(50, current_radius, 50):
        pygame.draw.circle(screen, BLACK, (CENTER_X, CENTER_Y), r, 1)  # Draw concentric circles for orbits
    
    # Draw nucleus
    nucleus.draw(screen)
    
    # Draw electrons
    for electron in electrons:
        electron.draw(screen)

    # Refresh screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
