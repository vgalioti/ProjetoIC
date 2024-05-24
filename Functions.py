from FaceClass import Face
from PointClass import Point
from ParticleClass import Particle

import numpy as np
import struct
from datetime import datetime


def read_stl(filename):
    with open(filename, 'rb') as f:
        Header = f.read(80)
        nn = f.read(4)
        Numtri = struct.unpack('i', nn)[0]
        record_dtype = np.dtype([
            ('Normals', np.float32, (3,)),
            ('Vertex1', np.float32, (3,)),
            ('Vertex2', np.float32, (3,)),
            ('Vertex3', np.float32, (3,)),
            ('atttr', '<i2', (1,)),
        ])
        data = np.zeros((Numtri), dtype=record_dtype)
        for i in range(0, Numtri, 10):
            d = np.fromfile(f, dtype=record_dtype, count=10)
            data[i:i+len(d)] = d

    #normals = data['Normals']
    return data



def checkVertices(particleGroup):
    lastAdd = particleGroup[-1]
    deleted = []
    
    for i in range(len(particleGroup) - 1):
        for x in lastAdd.vertices:
            if (particleGroup[i].isActive == True) and (x in particleGroup[i].vertices):
    
                lastAdd.addParticle = particleGroup[i]
                deleted.append(i)
                
                break
            
    # Para limpar as particles inativas
    j = 0
    for k in range(len(deleted)):
        index = deleted[k] + j
        particleGroup.pop(index)
        j = j - 1



def groupFaces(data):
    sizeData = len(data['Vertex1'])
    particleGroup = []
    
    for i in range(sizeData):

        p1 = Point(data['Vertex1'][i])
        p2 = Point(data['Vertex2'][i])
        p3 = Point(data['Vertex3'][i])
        f1 = Face(data['Normals'][i], p1, p2, p3)
    
        particleGroup.append(Particle(f1))
        checkVertices(particleGroup)
    
    return particleGroup
    
    

if __name__ == "__main__":
    start_time = datetime.now()
    data = read_stl("C:/Users/vinic/OneDrive/Área de Trabalho/Particle_Bed.stl")
    print("##########")
    print("OBJETIVO:")
    print(len(data['Vertex1']))
    print("##########")
    print("")
    
    teste = groupFaces(data)

    print("NÚMERO DE PARTICLES:")
    print(len(teste))
    print("")
    print('Duration: {}'.format(datetime.now() - start_time))
