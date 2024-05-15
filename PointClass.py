import ctypes
from copy import deepcopy as cp

class Point:
    def __init__(self, x):
        self.__coord = x
        self.__isInside = None
        self.__particleId = None
        
    @property
    def coord(self):
        return self.__coord
    
    @property
    def isInside(self):
        return self.__isInside
    
    @property
    def particleId(self):
        return self.__particleId
    
    @isInside.setter
    def isInside(self, y):
        self.__isInside = y

    @particleId.setter
    def particleId(self, n):
        if self.__particleId is None:
            self.__particleId = n
            
        elif n is None:
            self.__particleId = None
        
        # Ao alterar a particleId, todas as faces serao transferidas para
        # a nova particle, e a anterior passara a ter um id diferente
        else:
            originalId = cp(self.__particleId)
            destination = ctypes.cast(n, ctypes.py_object).value
            local = ctypes.cast(originalId, ctypes.py_object).value
            
            for i in range(len(local.faces)):
                destination.addFace = local.faces[i]


