from FaceClass import Face
from PointClass import Point
from ParticleClass import Particle

import numpy as np
import struct
import ctypes
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

def checkVertices(vertexGroup, particleGroup):
    
    for i in range (len(vertexGroup)):
        for j in range(3):
            if (vertexGroup[i].coord == particleGroup.faces[0].points[j].coord).all() and \
                vertexGroup[i].particleId != id(particleGroup):

                holdId = vertexGroup[i].particleId
                vertexParticle = ctypes.cast(holdId, ctypes.py_object).value
                particleGroup.addParticle = vertexParticle
                
                break


def groupFaces(data):
    sizeData = len(data['Vertex1'])
    particleGroup = []
    vertexGroup = []
    
    
    for i in range(sizeData):

        p1 = Point(data['Vertex1'][i])
        p2 = Point(data['Vertex2'][i])
        p3 = Point(data['Vertex3'][i])
        f1 = Face(data['Normals'][i], p1, p2, p3)
    
        particleGroup.append(Particle(f1))
        checkVertices(vertexGroup, particleGroup[i])
        
        for x in range(3):
            vertexGroup.append(particleGroup[i].faces[0].points[x])
    
    # Clean clones
    i = 0
    while i < len(particleGroup):
        
        if particleGroup[i].isActive == False:
            particleGroup.pop(i)
            i = i - 1
        
        i = i + 1
    
    
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