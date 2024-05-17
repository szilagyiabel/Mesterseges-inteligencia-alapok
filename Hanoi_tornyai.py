from keres import *
class Hanoi(Feladat):
    def __init__(self,k,c):
        self.kezdő=k
        self.cél=c
    def célteszt(self, állapot):
        return állapot == self.cél
    def rákövetkező(self, állapot):
        gyerek_cs=list()
        for melyiket in range(0,3):
            for hova in ['P','Q','R']:
                flag=True #az operátor alkalmazható
                # operátor alkalmazási előfeltételének vizsgálata
                if állapot[melyiket] != hova:
                    for i in range(0,melyiket):
                        if állapot[i]!= állapot[melyiket] and állapot[i]!=hova:
                            flag=True
                        else:
                            flag=False
                            break
                else:
                    flag = False
                #az operátor malkalamzási függvénye:
                if flag:
                    tmp = list(állapot)
                    tmp[melyiket] = hova
                    e=tuple(tmp)
                    gyerek_cs.append(("melyiket-->>hova",e))

        return gyerek_cs


if __name__ == "__main__":
    ha= Hanoi(('P','P','P'),('R','R','R'))
    print('Szélességi fakeresés')
    result = szélességi_fakeresés(ha)
    ut = result.út()
    ut.reverse()
    print(ut)

    print('Mélységi fakeresés')
    result = mélységi_fakeresés(ha)
    ut = result.út()
    ut.reverse()
    print(ut)


