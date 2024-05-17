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

    for is_vertical in [True, False]:
        for sor in range(8):
            for oszlop in range(8):
                if (is_vertical and sor > 5) or (not is_vertical and oszlop > 5):
                    continue
                if lerakhato(matrix, sor, oszlop, is_vertical) and lerakott_dominok < 21:
                    lerak(matrix, sor, oszlop, is_vertical)
                    lerakott_dominok += 1
                    if lerakott_dominok == 21:
                        break
            if lerakott_dominok == 21:
                break
        if lerakott_dominok == 21:
            break

    if lerakott_dominok < 21:
        print(lerakott_dominok)
    return matrix

csinal = doit()
for row in csinal:
    print(row)