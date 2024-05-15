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

if __name__ == "__main__":
    test3()
    
    