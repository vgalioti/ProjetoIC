import numpy as np
from copy import deepcopy as cp

class Particle:
    def __init__(self, f):
        self.__isActive = True
        
        # Altera o id das particulas
        face1 = f
        for i in range(3):
            face1.points[i].particleId = id(self)

        self.__faces = np.stack([face1])

        t1 = tuple(face1.points[0].coord)
        t2 = tuple(face1.points[1].coord)
        t3 = tuple(face1.points[2].coord)
        self.__vertices = {t1, t2, t3}
        

    @property
    def faces(self):
        return self.__faces
    
    @property
    def vertices(self):
        return self.__vertices
    
    @property
    def isActive(self):
        return self.__isActive
    
    @property
    def printPoints(self):
        for i in range(len(self.__faces)):
            for j in range(3):
                print(self.__faces[i].points[j].coord)
    
    @faces.setter
    def addFace(self, f1):
        new_face = f1
        
        #altera o ID das faces antes de adicionar
        for i in range(3):
            new_face.points[i].particleId = None
            new_face.points[i].particleId = id(self)
        
        self.__faces = np.append(self.__faces, [new_face], axis=0)
        
        t1 = tuple(new_face.points[0].coord)
        t2 = tuple(new_face.points[1].coord)
        t3 = tuple(new_face.points[2].coord)
        
        self.__vertices.add(t1)
        self.__vertices.add(t2)
        self.__vertices.add(t3)
        

    @faces.setter
    #OBS: A particle original p1 passa a ter um particleId DIFERENTE DO SEU PROPRIO!
    def addParticle(self, p1):
        for i in range(len(p1.faces)):
            self.addFace = p1.faces[i]
            
        p1.isActive = False


    @isActive.setter
    def isActive(self, state):
        self.__isActive = state
    