import pygame
import numpy as np
import random
from PhysicsEngine import PhysicsEngine

# Pygame setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Genome:
    def __init__(self):
        # For simplicity, the genome is represented as a dictionary
        # You could also use a numpy array, list, or other data structure
        self.traits = {
            'size': np.random.randint(5, 15),
            'speed': np.random.uniform(0.5, 2.0),
            # Regarding sight and detection
            'sightRange': np.random.uniform(0.5, 2.0),  # Range of the sight
            'sightFeeler': np.random.uniform(1, 8),     # Number of detection feelers
            'sightFOV': np.random.uniform(1, 360),      # The angle of which the sight feelers are spread out
            # Mitosis (reproduction)

            # Add other traits here

        }

    def mutate(self):
        # Choose a trait to mutate at random
        trait_to_mutate = random.choice(list(self.traits.keys()))
        # Apply mutation (randomly increase or decrease the trait)
        self.traits[trait_to_mutate] += np.random.uniform(-0.1, 0.1)


class Creature:
    def __init__(self):
        self.x = np.random.randint(0, SCREEN_WIDTH)
        self.y = np.random.randint(0, SCREEN_HEIGHT)
        self.genome = Genome()  # Each creature has its own genome
        self.color = WHITE
        self.energy = 100
        self.size = self.genome.traits['size']
        self.speed = self.genome.traits['speed']

    def move(self):
        # Random movement as an example
        self.x += np.random.randint(-self.speed, self.speed + 1)
        self.y += np.random.randint(-self.speed, self.speed + 1)

    def eat(self, pellets):
        # Example of simple eating behaviour
        for pellet in pellets:
            if np.hypot(pellet.x - self.x, pellet.y - self.y) < self.size:
                self.energy += pellet.size  # Eat the pellet, gain energy
                pellets.remove(pellet)  # Remove eaten pellet from list
                break

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size)


class Pellet:
    def __init__(self):
        self.x = np.random.randint(0, SCREEN_WIDTH)
        self.y = np.random.randint(0, SCREEN_HEIGHT)
        self.size = 5
        self.color = GREEN

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size)

creatures = [Creature() for _ in range(10)]
pellets = [Pellet() for _ in range(200)]
physics_engine = PhysicsEngine(creatures)

run = True
while run:
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for creature in creatures:
        creature.move()
        creature.eat(pellets)
        creature.draw(win)

    for pellet in pellets:
        pellet.draw(win)

    physics_engine.update()
    pygame.display.update()

pygame.quit()
