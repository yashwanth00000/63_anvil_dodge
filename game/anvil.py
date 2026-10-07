import random
import pygame


class Anvil:
    def __init__(self, screen_width, speed_multiplier=1.0):
        self.screen_width = screen_width
        self.width = 40
        self.height = 32
        self.x = random.randint(20, screen_width - self.width - 20)
        self.y = -self.height
        self.speed = random.uniform(4.5, 7.0) * speed_multiplier

    def update(self):
        self.y += self.speed

    def is_off_screen(self, screen_height):
        return self.y > screen_height + 10

    @property
    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)

    def _get_tint(self):
        """Return (tint_color, blend_factor) based on falling speed."""
        if self.speed < 7.0:
            # Slow: no tint, normal grey appearance
            return (0, 0, 0), 0.0
        elif self.speed < 11.0:
            # Medium: orange warning, blend grows from 0.0 to 1.0 across the range
            t = (self.speed - 7.0) / 4.0
            return (230, 160, 40), t
        else:
            # Fast: hot red danger, blend grows from 0.6 to 1.0
            t = min(1.0, 0.6 + (self.speed - 11.0) / 15.0)
            return (220, 50, 30), t

    @staticmethod
    def _blend(base, tint, factor):
        """Linearly interpolate between base and tint colours."""
        return tuple(int(b + (t - b) * factor) for b, t in zip(base, tint))

    def render(self, surface):
        _, blend = self._get_tint()
        tint_color, _ = self._get_tint()

        top_color = self._blend((120, 120, 130), tint_color, blend)
        base_color = self._blend((80, 80, 90), tint_color, blend)
        edge_color = self._blend((200, 200, 210), tint_color, blend)

        top_rect = pygame.Rect(int(self.x) + 4, int(self.y), self.width - 8, 14)
        pygame.draw.rect(surface, top_color, top_rect, border_radius=2)

        base_rect = pygame.Rect(int(self.x), int(self.y) + 14, self.width, 18)
        pygame.draw.rect(surface, base_color, base_rect, border_radius=3)
        pygame.draw.rect(surface, edge_color, base_rect, width=1, border_radius=3)