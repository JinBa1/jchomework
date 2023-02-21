import numpy as np 

def matrix_op(X, n ,m):
    # construct empty N x N matrices A and B
    matrixA, matrixB = []
    for i in range(n):
        # initialize row with index i
        rowOfA, rowOfB = []
        for j in range(n):
            # initialize row elements indexed ij
            elementA = 2 * (i + X) + 3 * (j - X) 
            elementB = i - np.sqrt(j + X)
            rowOfA.append(elementA)
            rowOfB.append(elementB)
        matrixA.append(rowOfA)
        matrixB.append(rowOfB)
    
    # matrix power
    for i in range(m):
        matrixB = np.matmul(matrixB, matrixB)
    
    output = np.matmul(matrixB, matrixA)
    output.round(2)
    return output

def main():
    print(matrix_op(6, 2, 3))
    