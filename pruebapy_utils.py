import random

def createRandomMatrix(rows = 3, columns = 3):

    if not (isinstance(rows, int) and isinstance(columns, int)):
        raise ValueError("Bad parameter data type")
        
    elif rows < 0 or columns < 0:
        raise ValueError("Parameters cannot contain negative values")
    
    matrix = []

    for i in range(columns):
        row = []

        for k in range(rows):
            row.append(random.randint(1, 10))

        matrix.append(row)

    return matrix
