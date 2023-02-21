import numpy as np 

############
# Question 1
def matrix_op(X, n ,m):
    # construct empty N x N matrices A and B
    matrixA, matrixB = [],[]
    for i in range(n):
        # initialize row with index i
        rowOfA, rowOfB = [],[]
        for j in range(n):
            # initialize row elements indexed ij
            elementA = 2 * (i + X) + 3 * (j - X) 
            elementB = i - np.sqrt(j + X)
            rowOfA.append(elementA)
            rowOfB.append(elementB)
        matrixA.append(rowOfA)
        matrixB.append(rowOfB)
    # convert lists to numpy arrays
    matrixA = np.asarray_chkfinite(matrixA)
    matrixB = np.asarray_chkfinite(matrixB)
    # matrix power
    matrixBPower = matrixB.copy()
    for i in range(m-1):   # m-1 ensures multiplies m times
        matrixBPower = matrixBPower@matrixB
        print(matrixBPower)
    # matrix multiplication
    output = matrixBPower@matrixA
    # round all elements to 2 decimal
    return output.round(2)  
############  

############
# Question 2
def q_sequence(n):
    # use dynamic programming, initial values Q[0] = Q[1] = 1
    QMemory = [1,1]
    # start iteration from Q[2] to Q[n-1]
    for i in range(2,n):
        newElement = QMemory[i - QMemory[i - 1]] + QMemory[i - QMemory[i - 2]]
        QMemory.append(newElement)
    return QMemory
############

############
# Question 3
def polyfit_coeffs(x,y):
    # construct coefficents for the linear polynomial
    coef = []
    for i in range(4):
        coefForA = []
        coefForA.append(p0(x[i]))
        coefForA.append(p1(x[i]))
        coefForA.append(p2(x[i]))
        coefForA.append(p3(x[i]))
        coef.append(coefForA)
    # solve for a0-3 given x0-3 and y0-3
    a = np.linalg.solve(coef,y)
    return a

# helper functions, evalute the polynomials
def p0(x):
    return 1 - pow(x,3)

def p1(x):
    return x + pow(x,2)

def p2(x):
    return pow(x,2) - x

def p3(x):
    return 1 + pow(x,3)

def p(x, a0, a1, a2, a3):
    return a0 * p0(x) + a1 * p1(x) + a2 * p2(x) + a3 * p3(x) 
############