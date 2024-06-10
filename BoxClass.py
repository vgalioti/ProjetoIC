from ParticleClass import Particle

class Box:
    def __init__(self, center, length, width, height):
        self.__center = center
        
        # Determinacao das faces da caixa
        x1 = center[0]
        y1 = center[1]
        z1 = center[2]
        x = length / 2.0
        y = width / 2.0
        z = height / 2.0
        
        self.__Zmax = z1 + z
        self.__Zmin = z1 - z
        self.__Xmax = x1 + x
        self.__Xmin = x1 - x
        self.__Ymax = y1 + y
        self.__Ymin = y1 - y
        
        self.__faceXY1 = {(x1 + x, y1 + y, z1 - z), (x1 + x, y1 - y, z1 - z), 
                          (x1 - x, y1 + y, z1 - z), (x1 - x, y1 - y, z1 - z)}
        self.__faceXY2 = {(x1 + x, y1 + y, z1 + z), (x1 + x, y1 - y, z1 + z), 
                          (x1 - x, y1 + y, z1 + z), (x1 - x, y1 - y, z1 + z)}
        self.__faceXZ1 = {(x1 + x, y1 - y, z1 + z), (x1 + x, y1 - y, z1 - z), 
                          (x1 - x, y1 - y, z1 + z), (x1 - x, y1 - y, z1 - z)}
        self.__faceXZ2 = {(x1 + x, y1 + y, z1 + z), (x1 + x, y1 + y, z1 - z), 
                          (x1 - x, y1 + y, z1 + z), (x1 - x, y1 + y, z1 - z)}
        self.__faceZY1 = {(x1 - x, y1 + y, z1 + z), (x1 - x, y1 + y, z1 - z), 
                          (x1 - x, y1 - y, z1 + z), (x1 - x, y1 - y, z1 - z)}
        self.__faceZY2 = {(x1 + x, y1 + y, z1 + z), (x1 + x, y1 + y, z1 - z), 
                          (x1 + x, y1 - y, z1 + z), (x1 + x, y1 - y, z1 - z)}


    def faces(self, n):
        if n == 1:
            return self.__faceXY1
        elif n == 2:
            return self.__faceXY2
        elif n == 3:
            return self.__faceXZ1
        elif n == 4:
            return self.__faceXZ2
        elif n == 5:
            return self.__faceZY1
        elif n == 6:
            return self.__faceZY2

 
    def checkParticles(self, particles):
        result = []
        check1 = False
        check2 = False
        
        for x in particles:
            for y in x.vertices:

                if y[2] > self.__Zmax:
                    check1 = True
                elif y[2] < self.__Zmax:
                    check2 = True
                    
                if (check1 == True) and (check2 == True):
                    result.append(x)
                    break
                
            check1 = False
            check2 = False
    
        return result