# Testes

import numpy as np

def test1():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]

    teste = np.stack([a, b, c])
    print(teste)
    print("")

    d = [10, 11, 12]
    print(id(d))
    teste = np.append(teste, [d], axis = 0)
    print(id(teste[3]))
    print(teste)
    print("")

    teste = np.delete(teste, [2], axis = 0)
    print(teste)
    print("")
    

def change(x):
    x = 1
    

def test2():
    variable = 192
    change(variable)
    print(variable)
    
def test3():
    a = [1, 2, 3]
    b = [4, 5, 6]

    teste = []
    teste.append(a)
    teste.append(b)
    
    print(teste)
    
    teste.pop(0)
    
    print(teste)
    
def test4():
    teste = {0.756, 0.72545, 0.73514}
    print(teste)
    print("")
    
    teste.add(0.124)
    teste.add(0.125)
    print(teste)
    
    a = 0.756
    
    if a in teste:
        print("Halleluya!")
        
def test5():
    teste = {0.756, 0.72545, 0.73514}
    t1 = (0.567, 0.432, 0.555)
    
    teste.add(t1)
    
    print(teste)
    
    if (0.555, 0.432, 0.567) in teste:
        print("Halleluya!")
        
    for x in teste:
        print(x)

def test6():
    teste = [1, 2, 3]
    print(teste)
    print("")
    
    teste.append(4)
    print(teste)
    
def test7():
    from BoxClass import Box
    
    box_center = (1, 2, 3)        # Coordenadas XYZ
    box_length = 4                # Eixo X
    box_width = 5                 # Eixo Y
    box_height = 10               # Eixo Z
    
    teste = Box(box_center, box_length, box_width, box_height)
    
    print(teste.faces(2))
    

if __name__ == "__main__":
    test7()
    
    