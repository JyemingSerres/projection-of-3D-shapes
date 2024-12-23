"""
Created on 12/15/2024
by Jye-Ming Serres
"""
import math
from enum import Enum


# Display settings
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
TARGET_FRAME_RATE = 100

# Math constants
GOLDEN_RATIO = (1 + math.sqrt(5))/2

# Colors
class Color(Enum):
    WHITE = (255, 255,255),
    RED = (255, 0, 0),
    GREEN = (0, 255, 0),
    BLUE = (0, 0, 255),
    YELLOW = (255, 255, 0),
    MAGENTA = (255, 0, 255),
    CYAN = (0, 255, 255),
    DEEP_SPACE = (10, 10, 20),