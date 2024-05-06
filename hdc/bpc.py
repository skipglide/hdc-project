# Binary Splatter Codes
from enum import Enum
import random
import numpy

class Mode(Enum):
    BINARY = 1
    ELEMENTARY = 2

class SplatterCode():
    def __init__(self, mode, dimensionality):
        self.mode = mode
        self.dimensionality = dimensionality
        self.vector_bank = set()

    def generate_hdv(self, type):
        N = self.dimensionality
        hdv = rand((-1, 1), N)
        return hdv