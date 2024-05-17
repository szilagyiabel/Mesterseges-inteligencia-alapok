from keres import *
class kiralyno(Feladat):
    def __init__(self,k,c,n):
        self.kezdő = k
        self.cél = c
        self.N = n
    def célteszt(self, á):
        return á[self.N] == self.cél
    def rákövetkező(self,á):
        gyerek_cs = list()
        s=á[self.N]
        for i in range(0,self.N):
            flag= True
            for m in range(0,s):
                if á[m] != i and abs(m-s) != abs(á[m]-i):
                    flag = True
                else:
                    flag =False
                    break

            if flag:
                tmp = list(á)
                tmp[s] = i
                tmp[self.N]=  tmp[self.N]+1 # s= s+1
                e=tuple(tmp)
                gyerek_cs.append(("lerak("+str(s)+","+str(i)+")",e))

        return gyerek_cs


if __name__ == "__main__":
    kir = kiralyno((-1,-1,-1,-1,-1,-1,-1,-1,0),8,8)

    print('Szélességi fakeresés')
    result = szélességi_fakeresés(kir)
    ut = result.út()
    ut.reverse()
    print(ut)

    print('Mélységi fakeresés')
    result = mélységi_fakeresés(kir)
    ut = result.út()
    ut.reverse()
    print(ut)


