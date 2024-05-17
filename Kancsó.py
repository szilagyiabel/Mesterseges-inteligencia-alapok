from keres import *
class Kancso(Feladat):
    def __init__(self,k,c):
        self.kezdő=k
        self.cél=c
        self.M1=3
        self.M2=5
        self.M3=8

    def célteszt(self,állapot):
        return állapot[0] == self.cél or állapot[1]== self.cél or állapot[2]==self.cél

    def rákövetkező(self, állapot):
        a1,a2,a3 = állapot
        gyerek_csomópontok=list()
        #tölt 1-ből 2-be:
        if a1!=0 and a2 != self.M2:
            T = min([a1,self.M2-a2])
            gyerek_csomópontok.append(("a1-ből a2-be",(a1-T,a2+T,a3)))
        # tölt 1-ből 3-be:
        if a1 != 0 and a3 != self.M3:
            T = min([a1, self.M3 - a3])
            gyerek_csomópontok.append(("a1-ből a3-be", (a1 - T, a2, a3+T)))

            # tölt 2-ből 1-be:
        if a2 != 0 and a1 != self.M1:
            T = min([a2, self.M1 - a1])
            gyerek_csomópontok.append(("a2-ből a1-be", (a1 + T, a2 - T, a3)))

            # tölt 2-ből 3-be:
        if a2 != 0 and a3 != self.M3:
            T = min([a2, self.M3 - a3])
            gyerek_csomópontok.append(("a2-ből a3-be", (a1, a2 - T, a3+T)))

            # tölt 3-ből 1-be:
        if a3 != 0 and a1 != self.M1:
            T = min([a3, self.M1 - a1])
            gyerek_csomópontok.append(("a3-ből a1-be", (a1 +T, a2 , a3-T)))

            # tölt 3-ből 2-be:
        if a3 != 0 and a2 != self.M2:
            T = min([a3, self.M2 - a2])
            gyerek_csomópontok.append(("a3-ből a2-be", (a1, a2 + T, a3-T)))

        return gyerek_csomópontok


if __name__ == "__main__":
    korso=Kancso((0,0,8),4)

    print('Szélességi fakeresés')
    result = szélességi_fakeresés(korso)
    ut = result.út()
    ut.reverse()
    print(ut)

    print('Mélységi fakeresés')
    result = mélységi_fakeresés(korso)
    ut = result.út()
    ut.reverse()
    print(ut)







