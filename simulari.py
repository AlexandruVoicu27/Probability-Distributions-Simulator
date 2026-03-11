import random
import math
import grafice

def Bernoulli(n, p):
    n = int(n)
    p = float(p)
    if p < 0 or p > 1:
        return
    with open("Simulari\\Bernoulli.txt", "w") as f:
        f.write(f"Probabilitatea:{p}\n")
        for _ in range(n):
            if random.random() < p:
                f.write(f"1\n")
            else:
                f.write(f"0\n")
    grafice.Bernoulli()


def Binomiala(p, n, k):
    n = int(n)
    p = float(p)
    k = int(k)

    if p < 0 or p > 1:
        return
    else:
        rezultate = [0] * (k + 1)

    for _ in range(n):
        succese = 0
        for _ in range(k):
            if random.random() < p:
                succese += 1
        rezultate[succese] += 1

    with open("Simulari\\Binomiala.txt", "w") as f:
        f.write(f'Probabilitatea:{p},Numarul de incercari:{n},Numarul de succese:{k}\n')
        for i in range(k + 1):
            f.write(f"{i} succese: {rezultate[i]} ori\n")
    grafice.Binomiala()

def Geometrica(p,n):
    p = float(p)
    if p <= 0 or p >= 1:
        return
    else:
        n_incercari = int(n)
    with open("Simulari\\Geometrica.txt", "w") as f:
        f.write(f"Probabilitatea:{p}\n")
        for _ in range(n_incercari):
            cnt = 1
            while random.random() >= p:
                cnt += 1
            f.write(f"Valorile generate: {cnt}\n")
    grafice.Geometrica()

def Poisson(p, k):
   
    lamda = float(p)
    n_incercari = int((k))

    with open("Simulari\\Poisson.txt", "w") as f:
        f.write(f"Probabilitatea:{p},Numarul de evenimente intr un timp anume:{n_incercari}\n")
        for _ in range(n_incercari):
            L = math.exp(-lamda)
            p = 1.0
            k = 0
            while p > L:
                p *= random.random()
                k += 1
            f.write(f"{k-1}\n")
    grafice.Poisson()

def Exponentiala(n, lamda):
    lamda = float(lamda)
    n = int(n)
    with open("Simulari\\Exponentiala.txt", "w") as f:
        f.write(f"Numarul de incercari:{n}, Lambda:{lamda}\n")
        for _ in range(n):
             u = random.random()
             x = -math.log(u) / lamda
             f.write(f"{x}\n")
    grafice.Exponentiala()

def Normala(n, media, deviatia):
    media = float(media)
    deviatia = float(deviatia)
    n = int(n)

    rezultate = []
    for _ in range(n // 2):
        u1 = random.random()
        u2 = random.random()
        r = math.sqrt(-2 * math.log(u1))
        theta = 2 * math.pi * u2
        z1 = r * math.cos(theta)
        z2 = r * math.sin(theta)
        rezultate.append(media + deviatia * z1)
        rezultate.append(media + deviatia * z2)

    if n % 2 == 1:
        u1 = random.random()
        u2 = random.random()
        r = math.sqrt(-2 * math.log(u1))
        theta = 2 * math.pi * u2
        z1 = r * math.cos(theta)
        rezultate.append(media + deviatia * z1)

    with open("Simulari\\Normala.txt", "w") as f:
        f.write(f"Medie:{media},Deviatia:{deviatia},Numar simular:{n}\n")
        for i in rezultate:
            f.write(str(i)+'\n')
    grafice.Normala()

def Uniforma(n, a, b):
    a = float(a)
    b = float(b)
    n = int(n)

    rezultate = []
    for _ in range(n):
        u = random.random()
        x = a + (b - a) * u
        rezultate.append(x)

    with open("Simulari\\Uniforma.txt", "w") as f:
        f.write(f"Limita inferioara:{a},Limita superioara:{b}\n")
        for i in rezultate:
            f.write(str(i)+'\n')
    grafice.Uniforma()

def Uniforma2(n,a,b):
    print(n,a,b)
    a = int(a)
    b = int(b)
    n = int(n)
    with open("Simulari\\Uniforma2.txt", "w") as f:
        f.write(f"a:{a},b:{b}\n")
        for _ in range(n):
            valoare = random.randint(a,b-1)
            f.write(str(valoare)+'\n') 
    grafice.Uniforma2()

def Disc(n, R):
    x0, y0 = 0, 0
    R = float(R)
    n = int(n)

    rezultate = []
    for _ in range(n):
        u1 = random.random()
        u2 = random.random()
        r = R * math.sqrt(u1)
        theta = 2 * math.pi * u2
        x = x0 + r * math.cos(theta)
        y = y0 + r * math.sin(theta)
        rezultate.append(str(x)+' ' + str(y))

    with open("Simulari\\Disc.txt", "w") as f:
        f.write(f"Raza:{R}\n")
        for i in rezultate:
            f.write(i+'\n')
    grafice.Disc()

def Elipsa(a, b, ns):
    x0, y0 = 0, 0
    a = float(a)
    b = float(b)
    n = int(ns)

    rezultate = []
    for _ in range(n):
        u1 = random.random()
        u2 = random.random()
        r = math.sqrt(u1)
        theta = 2 * math.pi * u2
        x = x0 + a * r * math.cos(theta)
        y = y0 + b * r * math.sin(theta)
        rezultate.append(str(x)+' ' + str(y))

    with open("Simulari\\Elipsa.txt", "w") as f:
        f.write(f"a:{a},b:{b}\n")
        for i in rezultate:
            f.write(i+'\n')
    grafice.Elipsa()

def Dreptunghi(n, a, b,c ,d ):
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    n = int(n)

    rezultate = []

    for _ in range(n):
        u1 = random.random()
        u2 = random.random()
        x = a + (b - a) * u1
        y = c + (d - c) * u2
        rezultate.append(str(x)+' ' + str(y))

    with open("Simulari\\Dreptunghi.txt", "w") as f:
        f.write(f"a:{a},b:{b},c:{c},d:{d}\n")
        for i in rezultate:
            f.write(i+'\n')
    grafice.Dreptunghi()
