from keres import *

class Huszar(Feladat):
    def __init__(self, kezdő, cél):
        self.kezdő = kezdő
        self.cél = cél

    def célteszt(self, állapot):
        if állapot in cél:
            return True
        return False
        
    def keres(elem, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == elem:
                    return (i, j) 
        return None 

    def rákövetkező(self, állapot):
        gyerek_cs = list()

        állapot_lista = list(állapot)
        huszar_poz = Huszar.keres('h', állapot_lista)

        if huszar_poz:
            i, j = huszar_poz
            lépések = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

        for di, dj in lépések:
            m, n = i + di, j + dj
            if 0 <= m < 7 and 0 <= n < 7 and állapot_lista[m][n] == 'o':
                uj_állapot = [list(sor) for sor in állapot_lista]
                uj_állapot[i][j] = 'x' 
                uj_állapot[m][n] = 'h'
                gyerek_cs.append(("mozog: " + str(m) + " " + str(n) ,uj_állapot))

        print_gyerekek(gyerek_cs)
        return gyerek_cs

def kiír(matrix):
    for row in matrix:
        print(" ".join(row))

def print_gyerekek(gyerek_cs):
    for (mozgas, uj_állapot) in gyerek_cs:
        print("Mozgás:", mozgas)
        kiír(uj_állapot)
        print()

if __name__ == "__main__":
    kezdő = (
    ('x', 'h', 'o', 'o', 'o', 'o', 'o', 'x'),
    ('o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'),
    ('o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'),
    ('o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'),
    ('o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'),
    ('o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'),
    ('o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'),
    ('x', 'o', 'o', 'o', 'o', 'o', 'o', 'x'),
    )

    cél = (
        (
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'h', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
        ),
        (
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('h', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
        ),
        (
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'h', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
            ('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'),
        )
    )

    huszár = Huszar(kezdő, cél)
    tmp = huszár.rákövetkező(kezdő)
    huszár.rákövetkező(tmp[0][1])

    print("Mélységi keresés")
    eredmeny = szélességi_gráfkeresés(huszár)
    ut = eredmeny.út()
    ut.reverse()
    print(ut)

    