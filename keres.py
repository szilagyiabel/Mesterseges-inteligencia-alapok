
import sys
from segéd import *
import logging


class Feladat:
        
    def __init__(self, kezdő, cél=None):
        logging.info("Feladat inicializálása: {}/{}".format( (kezdő,), (cél, )))
        self.kezdő = kezdő
        self.cél = cél
        
    def rákövetkező(self, állapot):
        raise NotImplementedError
    def érték(self):
           raise NotImplementedError
        
    def célteszt(self, állapot):
        return állapot == self.cél
        
    def útköltség(self, c, állapot1, lépés, állapot2):
        return c + 1

class Csúcs:
        
    def __init__(self, állapot, szülő=None, lépés=None, útköltség=0):
        self.állapot=állapot
        self.szülő = szülő
        self.lépés=lépés
        self.útköltség=útköltség
        if szülő:
            self.mélység = szülő.mélység + 1
        else:
           self.mélység = 0
        logging.info("állapot: {}, szülő: {}/{} ".format( (állapot, ), (szülő,
            ), útköltség ) )

    def __repr__(self):
        return "<Csúcs: %s>" % (self.állapot, )
        
    def út(self):
        x, válasz = self, [self]
        while x.szülő:
            válasz.append(x.szülő)
            x = x.szülő
        return válasz
    def megoldás(self):
            utam = self.út()
            utam.reverse()
            return [csúcs.lépés for csúcs in utam[1:]]
        
    def kiterjeszt(self, feladat):
        for (művelet, következő) in feladat.rákövetkező(self.állapot):
            if következő not in [csúcs.állapot for csúcs in self.út()]:
               yield Csúcs(következő, self, művelet,
                   feladat.útköltség(self.útköltség, self.állapot, művelet,
    	       következő))

def fakeresés(feladat, perem):

    perem.append(Csúcs(feladat.kezdő))
    while perem:

        csúcs = perem.pop()

        if feladat.célteszt(csúcs.állapot):
            return csúcs
        else:
            perem.extend(csúcs.kiterjeszt(feladat))

    return None

def szélességi_fakeresés(feladat):
    return fakeresés(feladat,Sor())

def mélységi_fakeresés(feladat):
    return fakeresés(feladat,Verem())


def gráfkeresés(feladat, perem):

    kifejtési_sor = set()
    perem.append(Csúcs(feladat.kezdő))
    while perem:

        csúcs = perem.pop()
        if feladat.célteszt(csúcs.állapot):
            return csúcs

        if csúcs not in kifejtési_sor:
            kifejtési_sor.add(csúcs)
            perem.extend(csúcs.kiterjeszt(feladat))

    return None


def szélességi_gráfkeresés(feladat):
    return gráfkeresés(feladat,Sor())

def mélységi_gráfkeresés(feladat):
    return gráfkeresés(feladat,Verem())


