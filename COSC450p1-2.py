#Emily Jetton
#COSC 450
#Python code to create 2 random 2D arrays and multiply them 


from random import seed
from random import randint

print()
print()

matrix = []
r = 5
c = 5

for i in range(r):
    arr = []
    for j in range(c):
        value1 = randint(0,100)
        arr.append(value1)
    matrix.append(arr)
    
print("matrix 1")  
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end = " ")
    print()

print ()

matrix2 = []
r2 = r
c2 = c

for i in range(r2):
    arr2 = []
    for j in range(c2):
        value1 = randint(0,100)
        arr2.append(value1)
    matrix2.append(arr2)
    
print("matrix 2")  
for i in range(r2):
    for j in range(c2):
        print(matrix2[i][j], end = " ")
    print()

newMatrix = []
for i in range(r):
    mult = []
    for j in range(c):
        var1 = int(matrix[i][j])
        var2 = int(matrix2[j][i])
        var3 = var1*var2
        mult.append(var3)
    newMatrix.append(mult)

print()
print("multiplied matricies")  
for i in range(r2):
    for j in range(c2):
        print(newMatrix[i][j], end = " ")
    print()

print()   
