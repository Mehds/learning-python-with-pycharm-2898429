import pygame
from pygame.locals import Rect

INACTIVE_COLOR = "#16302B"
ACTIVE_COLOR = "#C0E5C8"


class Cell(Rect):
    def __init__(self, pos: tuple, dimensions: tuple, active=False):
        self.active = active
        self.future_state = None

        super().__init__(pos, dimensions)

    def draw(self, surface):
        """
            This method checks what state the cell is in, and draws it in the appropriate color on the provided surface
        """
        color = ACTIVE_COLOR if self.active else INACTIVE_COLOR
        return pygame.draw.rect(surface, color, self)

    def __str__(self):
        return "X" if self.active else "_"

    def flip(self):
        self.active = not self.active

    def set_active(self):
        self.active = True

    def set_inactive(self):
        self.active = False

    # based on the number of living_neighbors and the current state of the cell
    # decide what it's future_state should be.
    def set_future_state(self, living_neighbors: int):
        pass

    # set the current state to the future state
    # then set the future_state to None, we don't need to keep that information around
    def update(self):
        pass