from FaceClass import Face
from PointClass import Point
from ParticleClass import Particle

import numpy as np
import struct


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
    n1 = data['Normals']
    v1 = data['Vertex1']
    v2 = data['Vertex2']
    v3 = data['Vertex3']
    points = np.hstack(((n1[:, np.newaxis, :]),(v1[:, np.newaxis, :]), (v2[:, np.newaxis, :]), (v3[:, np.newaxis, :])))
    return data

data = read_stl("C:/Users/vinic/OneDrive/Área de Trabalho/CuboTeste.stl")

p1 = Point(data['Vertex1'][0])
p2 = Point(data['Vertex2'][0])
p3 = Point(data['Vertex3'][0])

f1 = Face(data['Normals'][0], p1, p2, p3)

particle1 = Particle(f1)

p1 = Point(data['Vertex1'][1])
p2 = Point(data['Vertex2'][1])
p3 = Point(data['Vertex3'][1])

f1 = Face(data['Normals'][1], p1, p2, p3)

particle2 = Particle(f1)

print(particle1.faces[0].normal)
print(particle1.faces[0].points[0].coord)
print(particle1.faces[0].points[1].coord)
print(particle1.faces[0].points[2].coord)
print("")
print(particle2.faces[0].normal)
print(particle2.faces[0].points[0].coord)
print(particle2.faces[0].points[1].coord)
print(particle2.faces[0].points[2].coord)

# particle1.faces[0].points[0].particleId = id(particle2)
particle2.addParticle = particle1
print("")
print("")
print("")

particle1.printPoints

print("")
print("")
print("")

for x in range(len(particle2.faces)):
    print("")
    print(particle2.faces[x].normal)
    for j in range(3):
        print(particle2.faces[x].points[j].coord)

print("")
print("")
print("")

print(id(particle1))
print(particle1.faces[0].points[0].particleId)
print(id(particle2))
print(particle2.faces[1].points[0].particleId)

print(particle1.isActive)