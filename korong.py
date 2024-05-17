from keres import *

class Korongok(Feladat):
    def __init__(self, kezdő, cél):
        self.kezdő = kezdő
        self.cél = cél

    def célteszt(self, állapot):
        return állapot == self.cél

    def rákövetkező(self, állapot):
        gyerek_cs = list()
        for i in range(1, len(állapot)):
            tmp = list(állapot)
            korong = tmp[0:i+1]
            korong.reverse()
            del tmp[0:i+1]
            tmp = korong + tmp
            tmp = tuple(tmp)
            gyerek_cs.append((f"felső {i+1} korong megfordítva", tmp))
        return gyerek_cs

def kiír(állapot):
    for i in range(len(állapot)):
        print('Korong ' + str(állapot[i]))
    print()

if __name__ == "__main__":
    korongok = Korongok((6,7,3,2,8,5,4,1), (1,2,3,4,5,6,7,8))

    print('Szélességi gráfkeresés')
    result = szélességi_gráfkeresés(korongok)
    eredmény = result.megoldás()
    eredmény = ['kezdőállapot'] + eredmény
    ut = result.út()
    ut.reverse()
    
    for i in range(len(ut)):
        print(f"Lépés {i+1}: {eredmény[i]}")
        kiír(ut[i].állapot)

    print(ut)
