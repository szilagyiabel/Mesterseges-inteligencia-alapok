import random

def lerakhato(matrix, sor, oszlop, is_vertical):
    try:
        if is_vertical:
            for i in range(3):
                if matrix[sor + i][oszlop] != 0:
                    return False
        else:
            for i in range(3):
                if matrix[sor][oszlop + i] != 0:
                    return False
    except IndexError:
        return False
    return True

def lerak(matrix, sor, oszlop, is_vertical):
    if is_vertical:
        for i in range(3):
            matrix[sor + i][oszlop] = 1
    else:
        for i in range(3):
            matrix[sor][oszlop + i] = 1

def doit():
    matrix = [[0 for _ in range(8)] for _ in range(8)]
    lerakott_dominok = 0
    attempts = 0
    max_attempts = 1000  

    while lerakott_dominok < 21 and attempts < max_attempts:
        is_vertical = random.choice([True, False])
        if is_vertical:
            sor = random.randint(0, 5)
            oszlop = random.randint(0, 7)
        else:
            sor = random.randint(0, 7)
            oszlop = random.randint(0, 5)
        
        if lerakhato(matrix, sor, oszlop, is_vertical):
            lerak(matrix, sor, oszlop, is_vertical)
            lerakott_dominok += 1
        attempts += 1
    
    if lerakott_dominok < 21:
        print(lerakott_dominok)
    return matrix

csinal = doit()
for row in csinal:
    print(row)
