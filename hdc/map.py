import numpy as np

class CleanUpMemory:
    def __init__(self, dimensionality):
        self.memory = set()
        self.dimensionality = dimensionality
        self.dictionary = dict()
    
    def add_hdv(self, X):
        self.memory.add(X)

    def add_pair(self, x):
        X = create_hdv(self.dimensionality)
        self.add_hdv(convert_array2tuple(X))
        self.dictionary[x] = X

    def search_memory(self, X):
        simularity = dict()
        for hdv in self.memory:
            dot_product = np.dot(X, hdv)
            magnitude = np.linalg.norm(vector)
            cosine_similarity = dot_product / (magnitude * magnitude)
            simularity[X] = cosine_similarity
        res = {key: val for key, val in sorted(simularity.items(), key = lambda ele: ele[0], reverse = True)}
        return sorted
    
    def lookup_pair(self, x):
        X = self.dictionary[x]
        return X

def convert_array2tuple(X):
    tuple_arr = tuple(X)
    return tuple_arr

def convert_tuple2array(X):
    array = np.asarray(X)
    return array

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

