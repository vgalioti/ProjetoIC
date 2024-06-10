from FaceClass import Face
from PointClass import Point
from ParticleClass import Particle
from BoxClass import Box

import numpy as np
from math import sqrt
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



def exportSTL(particleList):
    f = open("export.stl", "w")
    f.write("solid TesteSolid\n")
    
    for x in particleList:
        for i in range(len(x.faces)):
            a = "facet normal " + str(x.faces[i].normal[0]) + \
                            " " + str(x.faces[i].normal[1]) + \
                            " " + str(x.faces[i].normal[2]) + "\n"
            f.write(a)
            f.write("  outer loop\n")

            for k in range(3):
                b = "    vertex " + str(x.faces[i].points[k].coord[0]) + \
                              " " + str(x.faces[i].points[k].coord[1]) + \
                              " " + str(x.faces[i].points[k].coord[2]) + "\n"
                f.write(b)
            
            f.write("  endloop\n")
            f.write("endfacet\n")

    f.write("endsolid TesteSolid")
            


def checkVertices(particleGroup):
    lastAdd = particleGroup[-1]
    deleted = []
    
    for i in range(len(particleGroup) - 1):
        if lastAdd.vertices & particleGroup[i].vertices:
    
            lastAdd.addParticle = particleGroup[i]
            deleted.append(i)
                   
    j = 0
    # Para limpar as particles inativas
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



def checkMaxMin(particles):
    minimum = set()
    maximum = set()
    
    for x in particles:
        minimum.add(min(x.vertices))
        maximum.add(max(x.vertices, key = lambda x: x[0] + x[1] + x[2]))
    
    # Por enquanto é uma aproximacao. Precisa melhorar
    return [min(minimum, key = lambda x: x[0] + x[1] + x[2]), max(maximum, key = lambda x: x[0] + x[1] + x[2])]


if __name__ == "__main__":
    start_time = datetime.now()
    
    data = read_stl("C:/Users/vinic/OneDrive/Área de Trabalho/STL Testes/Particle_Bed.stl")
    
    print("Número de Faces:")
    print(len(data['Vertex1']))
    print("")
    
    particles = groupFaces(data)

    print("Número de Particles:")
    print(len(particles))
    print("")
    
    coords = checkMaxMin(particles)
    
    print("Máximo e Mínimo:")
    print(f"{coords[1]} e {coords[0]} \n")
    
    print('Duration: {}'.format(datetime.now() - start_time))
    print("")
    
    box_center = (0, 0, 0)        # Coordenadas XYZ
    box_length = 1                # Eixo X
    box_width = 1                 # Eixo Y
    box_height = 0.1                # Eixo Z

    teste = Box(box_center, box_length, box_width, box_height)
    
    test1 = teste.checkParticles(particles)
    exportSTL(test1)
    