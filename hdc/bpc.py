# Binary Splatter Codes
from enum import Enum
import random
import numpy

class Mode(Enum):
    BINARY = 1
    BIPOLAR = 2

class HyperVectorType(Enum):
    TR

class SplatterCode():
    def __init__(self, mode, dimensionality):
        self.mode = mode
        self.dimensionality = dimensionality
        self.vector_bank = set()
    
    def add_item(self, X):
        self.vector_bank.add(X)
    
    

def generate_code(mode):
    match mode:
        case "BINARY":
            return generate_binary()
        case "BIPOLAR":
            return generate_bipolar()

def generate_bipolar(n):
    hdv = rand((-1, 1), n)
    return hdv
    
def generate_binary(n):
    hdv = rand((0, 1), n)
    return hdv
    
def generate_permutation_matrix(n):
    permutation_matrix = np.identity(n)
    np.random.shuffle(permutation_matrix)
    return permutation_matrix
    
def generate_pair_association(A, B):
    pm = generate_permutation_matrix()
    pair = np.logical_xor(pm * A, B)
    return pair

def recover_pair_element(A, B, P):
    pass # Where does P comes from???

def invert_permutation_matrix(X):
    ipm = np.transpose(X)
    return ipm

def create_holistic_sum_vector(P):
    # P is a list of pairs
    hsm = set()
    for p in P:
        hsm.add(p)
    return hsm

def extend_holistic_sum_vector(H, P):
    # H is an existing holistic sum vector
    # P is an addition pair we want to add
    try:
        H.add(P)
    except ValueError:
        pass
    return H