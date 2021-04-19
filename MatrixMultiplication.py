def matrixMultiplication(A, B):
    if len(A[0]) != len(B):
        raise Exception("Need to match inner dimensions")
        
    newMatrix = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for x in range(len(A)):
        for y in range(len(B[0])):
            tmpA = A[x]
            tmpB = []
            for k in range(len(B)):
                tmpB.append(B[k][y])
            newMatrix[x][y] = sum([tmpA[x]*tmpB[x] for x in range(len(A[0]))])
            
    return newMatrix
