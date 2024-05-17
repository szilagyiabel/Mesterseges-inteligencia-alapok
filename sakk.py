A = '🟥'
B = '⬜'
# G = '🟩'
class Sakktabla:
    def __init__(self) -> None:
        self.k = [8*[B] for _ in range(8)]
        self.s = A
        # self.k[3][1] = G
    
    def celteszt(self, state):
        return sum([3*i for i in range(1,22)]) == sum([sum(x) for x in state])

    def rakovetkezo(self, state: list[list]):
        # 
        jelenlegi = self.s
        r = []
        for i in range(8):
            for j in range(8):
                tmp = []
                if  ( j + 1 < 8 and j + 2 < 8):
                    if (state[i][j] == B and state[i][j+1] == B and state[i][j+2] == B):
                        for x in state:
                            tmp.append(x.copy())
                        tmp[i][j] = jelenlegi
                        tmp[i][j+1] = jelenlegi
                        tmp[i][j+2] = jelenlegi
                        #self.s += 1
                        r.append(tmp)
                        del tmp

                tmp = []
                if (i + 1 < 8 and i + 2 < 8):
                    if  (state[i][j] == B and state[i+1][j] == B and state[i+2][j] == B):
                        for x in state:
                            tmp.append(x.copy())
                        tmp[i][j] = jelenlegi
                        tmp[i+1][j] = jelenlegi
                        tmp[i+2][j] = jelenlegi
                        #self.s += 1
                        r.append(tmp)
                        del tmp


        return r


def main():
    s = Sakktabla()
    r = s.rakovetkezo(s.k)
    for x in r:
        for d in x:
            print(d)
        print(30*'-')
    print(len(r))
if __name__ == "__main__":
    main()