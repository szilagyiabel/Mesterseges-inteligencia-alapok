from keres import *

class Domino(Feladat):
    def __init__(self, kezdo, N):
        super().__init__(kezdo + (0,))
        self.N = N

    def célteszt(self, állapot):
        return állapot[-1] == self.N

    def rákövetkező(self, állapot):
        gyerek_cs = list()
        D = állapot[-1]
        tabla = állapot[:-1]

        if D >= self.N:
            return gyerek_cs

        for i in range(8):
            for j in range(8):
                if self.elerhető(tabla, i, j):
                    uj_tabla = list(tabla)
                    if j <= 5 and all(uj_tabla[i*8 + k] == 0 for k in range(j, j+3)):
                        for k in range(j, j+3):
                            uj_tabla[i*8 + k] = 1
                        uj_állapot = tuple(uj_tabla) + (D+1,)
                        gyerek_cs.append((f"lerak({i},{j}) vízszintes", uj_állapot))

                    if i <= 5 and all(uj_tabla[(i+k)*8 + j] == 0 for k in range(3)):
                        for k in range(3):
                            uj_tabla[(i+k)*8 + j] = 1
                        uj_állapot = tuple(uj_tabla) + (D+1,)
                        gyerek_cs.append((f"lerak({i},{j}) függőleges", uj_állapot))

        return gyerek_cs

    def elerhető(self, tabla, i, j):
        return tabla[i*8 + j] == 0

if __name__ == "__main__":
    kezdo = (0,) * 64
    dom = Domino(kezdo, 21)

    print('mélységi_fakeresés')
    result = mélységi_fakeresés(dom)

    ut = result.út()
    ut.reverse()
    for csucs in ut:
        print(csucs.lépés)
