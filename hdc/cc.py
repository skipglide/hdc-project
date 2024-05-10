# Cognitive Code
import numpy as np
class ItemMemory:
    def __init__(self):
        self.catalog = set()
    
    def add_entry(self,X):
        self.catalog.add(X)

    def clean_up(self, X):
        # return a vector from the catalog
        pass

def return_sum_vector(X):
    sum_vector = np.array([])
    for x in X:
        sum_vector = np.add(sum_vector, x)
    return sum_vector

def sum_vector_mapping(X):
    sum_vector = return_sum_vector(X)
    return sum_vector

def mean_vector_mapping(X):
    mean_vector = np.linalg.norm(return_sum_vector(X))
    return mean_vector

def hamming_distance(A, B):
    difference = np.bitwise_xor(A, B)
    return np.sum(difference)