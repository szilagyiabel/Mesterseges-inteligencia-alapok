def is_szoko(ev):
    if ev%4==0 and ev%100 !=0 or ev%400==0:
        return True
    else:
        return False

def szoko_evek(ev1,ev2):
    sz_evek=[]
    #sz_evek = list()
    for i in range(ev1,ev2+1):
        if(is_szoko(i)):
            sz_evek.append(i)

    return sz_evek

def paros_paratlan():
    count_paros=0
    count_paratlan=0
    x=int(input("Kérem a kövi számot: "))
    while x!=0:
        if x%2==0:
            count_paros= count_paros+1
        else:
            count_paratlan=count_paratlan+1
        x = int(input("Kérem a kövi számot: "))

    print("Paros szamok száma:"+ str(count_paros))


def tuple_example():
    T=(1,"alma",[-2,5.9])
    print(T)
    print(T[1])
    tmp=list(T)
    tmp[0]=1001
    T2=tuple(tmp)
    print(T2)

def lista_example():
    a = list()
    a.append(2)
    a.append(-1)
    a.append(5)
    a.reverse()
    print(a)
    a.sort(reverse=True)
    print(a)
    print("A lista elemeinek száma " + str(len(a)))


if __name__ == "__main__":
   # print(szoko_evek(1900,2024))
   #paros_paratlan()
   #lista_example()
   tuple_example()

