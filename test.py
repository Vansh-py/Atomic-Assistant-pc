from flask import Flask, render_template, request
import pygame
import math
import threading

app = Flask(__name__)

# Function to start the Pygame simulation
def start_simulation(num_electrons):
    pygame.init()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
    CENTER_X, CENTER_Y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    RADIUS = 200  # Radius of the largest orbit

    ELECTRON_DISTRIBUTION = [2, 8, 8, 18, 18, 32, 32]

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

    class Nucleus:
        def __init__(self):
            self.x, self.y = CENTER_X, CENTER_Y
            self.radius = 15

        def draw(self, screen):
            pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)

    class Electron:
        def __init__(self, orbit_radius, angle, speed, color=BLUE):
            self.orbit_radius = orbit_radius
            self.angle = angle
            self.speed = speed
            self.color = color
            self.radius = 5

        def update(self):
            self.angle += self.speed
            if self.angle >= 2 * math.pi:
                self.angle -= 2 * math.pi

        def draw(self, screen):
            x = CENTER_X + int(self.orbit_radius * math.cos(self.angle))
            y = CENTER_Y + int(self.orbit_radius * math.sin(self.angle))
            pygame.draw.circle(screen, self.color, (x, y), self.radius)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Atom Simulation')

    nucleus = Nucleus()

    electrons = []
    orbit_radius_increment = 50
    speed = 0.02
    current_radius = orbit_radius_increment

    for orbit, num_electrons in enumerate(electron_distribution):
        angle_increment = 2 * math.pi / num_electrons
        for i in range(num_electrons):
            angle = i * angle_increment
            electrons.append(Electron(orbit_radius=current_radius, angle=angle, speed=speed))
        current_radius += orbit_radius_increment

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for electron in electrons:
            electron.update()

        screen.fill(WHITE)
        
        for r in range(50, current_radius, 50):
            pygame.draw.circle(screen, BLACK, (CENTER_X, CENTER_Y), r, 1)

        nucleus.draw(screen)

        for electron in electrons:
            electron.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    num_electrons = int(request.form['numElectrons'])
    threading.Thread(target=start_simulation, args=(num_electrons,)).start()
    return "Simulation started! Check the Pygame window."

if __name__ == '__main__':
    app.run(debug=True)
