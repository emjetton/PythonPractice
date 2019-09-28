#Emily Jetton
#COSC 450
#Python code to create 2 random 2D arrays and multiply them 


from random import seed
from random import randint

print()
print()

matrix = []
r = 3
c = 3

for i in range(r):
    arr = []
    for j in range(c):
        value1 = randint(0,100)
        arr.append(value1)
    matrix.append(arr)
    
    
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end = " ")
    print()

print ()

matrix2 = []
r2 = 3
c2 = 3

for i in range(r2):
    arr2 = []
    for j in range(c2):
        value1 = randint(0,100)
        arr2.append(value1)
    matrix2.append(arr2)
    
    
for i in range(r2):
    for j in range(c2):
        print(matrix2[i][j], end = " ")
    print()