import numpy as np
from PointClass import Point
from copy import deepcopy as cp

class Face:
    def __init__(self, n1, v1, v2, v3):
        self.__normal = cp(n1)
        self.__points = np.stack([cp(v1), cp(v2), cp(v3)])
    
    @property
    def normal(self):
        return self.__normal
    
    @property
    def points(self):
        return self.__points

