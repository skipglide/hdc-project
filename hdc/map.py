import numpy as np

class CleanUpMemory:
    def __init__(self, dimensionality):
        self.memory = set()
        self.dimensionality = dimensionality
        self.dictionary = dict()
    
    def add_hdv(self, X):
        self.memory.add(X)

    def add_pair(x):
        create_hdv(self.dimensionality)
        self.add_hdv(X)
        self.dictionary[X] = x

    def cosine_simularity(self, X, n):
        simularity = dict()
        for hdv in self.memory:
            dot_product = np.dot(X, hdv)
            magnitude = np.linalg.norm(vector)
            cosine_similarity = dot_product / (magnitude * magnitude)
            simularity[X] = cosine_similarity
        
        return simularity[:n]
    
    def lookup_pair(self, X):
        x = self.dictionary[X]
        return x


def create_hdv(d):
    hdv = np.random.choice([-1, 1], size=d)
    return hdv

def bundle(A, B):
    X = A + B
    X = np.clip(X, -1, 1)
    return X

def bind(A, B):
    X = A * B
    return X

def protect(X):
    X = np.roll(X, 1)
    return X

def unprotect(X):
    X = np.roll(X, -1)
    return X

