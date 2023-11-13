"""Langton's ant implementation."""
from enum import Enum, IntEnum

import numpy as np
from PIL import Image


class Dir(IntEnum):
    """Possible directions."""

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Color(Enum):
    """Possible colors."""

    WHITE = 1
    BLACK = 0


def invert_color(grid, x, y):
    """Invert the color of grid at x, y coordinate."""
    if grid[y][x] == Color.BLACK.value:
        grid[y][x] = Color.WHITE.value
    else:
        grid[y][x] = Color.BLACK.value


def next_direction(grid, x, y, direction):
    """Compute next direction according to current position and direction."""
    if grid[y][x] == Color.BLACK.value:
        turn_right = False
    else:
        turn_right = True
    direction_index = direction.value
    if turn_right:
        direction_index = (direction_index + 1) % 4
    else:
        direction_index = (direction_index - 1) % 4
    directions = [Dir.UP, Dir.RIGHT, Dir.DOWN, Dir.LEFT]
    direction = directions[direction_index]
    return direction


def next_position(x, y, direction):
    """Compute next position according to direction."""
    if direction == Dir.UP:
        y -= 1
    elif direction == Dir.RIGHT:
        x -= 1
    elif direction == Dir.DOWN:
        y += 1
    elif direction == Dir.LEFT:
        x += 1
    return x, y


def ant(width, height, start_direction=Dir.UP):
    """Langton's ant."""
    grid = np.ones((width, height), bool)
    x = width // 2
    y = height // 2
    direction = start_direction

    i = 0
    while 0 <= x < width and 0 <= y < height:
        invert_color(grid, x, y)
        direction = next_direction(grid, x, y, direction)
        x, y = next_position(x, y, direction)
        i += 1

    Image.fromarray(grid).save("s.png")
    print(width * height - np.sum(grid))


if __name__ == "__main__":
    ant(width=1024, height=1024, start_direction=Dir.UP)
