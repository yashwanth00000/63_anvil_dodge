import random
import pygame


class Particle:
    """A small dust particle spawned on anvil ground impact."""

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        # Random outward velocity — mostly horizontal with slight upward drift
        self.vx = random.uniform(-2.5, 2.5)
        self.vy = random.uniform(-3.0, -0.5)
        self.radius = random.randint(2, 5)
        self.lifetime = random.randint(15, 30)  # frames
        self.age = 0
        # Earthy dust tones
        shade = random.randint(120, 180)
        self.color = (shade, shade - 20, shade - 40)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.12  # gentle gravity pulls particles back down
        self.age += 1

    def is_dead(self):
        return self.age >= self.lifetime

    def render(self, surface):
        # Fade out by reducing alpha over lifetime
        alpha = max(0, 255 - int(255 * self.age / self.lifetime))
        s = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(
            s,
            (*self.color, alpha),
            (self.radius, self.radius),
            self.radius,
        )
        surface.blit(s, (int(self.x) - self.radius, int(self.y) - self.radius))
