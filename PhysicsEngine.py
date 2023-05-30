import numpy as np
class PhysicsEngine:
    def __init__(self, creatures):
        self.creatures = creatures

    def update(self):
        # Check for collisions between all pairs of creatures
        for i in range(len(self.creatures)):
            for j in range(i+1, len(self.creatures)):
                c1 = self.creatures[i]
                c2 = self.creatures[j]
                # If the distance between the creatures is less than the sum of their sizes, they are colliding
                if np.hypot(c1.x - c2.x, c1.y - c2.y) < c1.size + c2.size:
                    self.resolve_collision(c1, c2)

    def resolve_collision(self, c1, c2):
        # When two creatures collide, they bounce off each other
        # This resolution conserves momentum and kinetic energy (i.e. an elastic collision)

        # Calculate the direction vector
        direction = np.array([c1.x - c2.x, c1.y - c2.y])
        direction = direction / np.linalg.norm(direction)  # normalize the direction vector

        # Calculate the relative velocity
        relative_velocity = np.array([c1.dx - c2.dx, c1.dy - c2.dy])

        # Calculate the velocity along the direction of collision
        velocity_along_direction = np.dot(relative_velocity, direction)

        # If the velocity is away from the collision, do nothing
        if velocity_along_direction > 0:
            return

        # Calculate the impulse (j)
        impulse = -(1 + 1) * velocity_along_direction
        impulse /= 1 / c1.size + 1 / c2.size

        # Apply the impulse
        c1.dx += impulse * direction[0] / c1.size
        c1.dy += impulse * direction[1] / c1.size
        c2.dx -= impulse * direction[0] / c2.size
        c2.dy -= impulse * direction[1] / c2.size
