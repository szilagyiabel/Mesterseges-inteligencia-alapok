from keres import *

class Huszar(Feladat):
    def __init__(self, kezdo, cel):
        self.kezdo = kezdo
        self.cel = cel

    def célteszt(self, allapot):
        return allapot in self.cel
        
    def keres(self, elem, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == elem:
                    return (i, j)
        return None

    def rákövetkező(self, allapot):
        gyerek_csomopontok = list()
        allapot_lista = list(allapot)
        huszar_poz = self.keres('h', allapot_lista)
        lepesek = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        if huszar_poz:
            i, j = huszar_poz
            for di, dj in lepesek:
                uj_i, uj_j = i + di, j + dj
                if 0 <= uj_i < len(allapot_lista) and 0 <= uj_j < len(allapot_lista[0]) and allapot_lista[uj_i][uj_j] == 'o':
                    uj_allapot = [list(sor) for sor in allapot_lista]
                    uj_allapot[i][j], uj_allapot[uj_i][uj_j] = 'o', 'h'
                    gyerek_csomopontok.append(("mozog: " + str(uj_i) + " " + str(uj_j) ,uj_allapot))

        return gyerek_csomopontok
    
if __name__ == "__main__":
    kezdo = (
    ('x', 'h', 'o', 'o', 'o', 'o', 'o', 'x'),
    ('o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'),
    ('o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'),
    ('o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'),
    ('o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'),
    ('o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'),
    ('o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'),
    ('x', 'o', 'o', 'o', 'o', 'o', 'o', 'x'),
    )

    cel = (
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

    huszar_feladat = Huszar(kezdo, cel)

    tmp = huszar_feladat.rákövetkező(kezdo)
    huszar_feladat.rákövetkező(tmp[0][1])

    print("Szélességi keresés")
    eredmeny = szélességi_fakeresés(huszar_feladat)
    ut = eredmeny.út()
    ut.reverse()
    print(ut)