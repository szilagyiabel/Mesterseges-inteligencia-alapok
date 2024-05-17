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

        return gyerek_cs

if __name__ == "__main__":
    