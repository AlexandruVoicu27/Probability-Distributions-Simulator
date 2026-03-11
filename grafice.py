import numpy as np
import matplotlib.pyplot as plt

def Bernoulli():                                   
    with open("Simulari\\Bernoulli.txt", 'r') as f:
        linii = f.readlines()
    
    p = float(linii[0].split(":")[1].strip())
    date = [int(l.strip()) for l in linii[1:] if l.strip() in ['0', '1']]
    data = np.array(date)

    values, counts = np.unique(data, return_counts=True)
    plt.figure(figsize=(6, 4))
    plt.bar(values, counts, tick_label=["0 (Eșec)", "1 (Succes)"])
    plt.title(f"Simularea Distribuției Bernoulli cu probabilitatea: {p} %")
    plt.xlabel("Rezultat")
    plt.ylabel("Frecvență")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    result = dict(zip(values, counts))
    print("Rezultate simulare:", result)
    
def Binomiala():
    with open("Simulari\\Binomiala.txt", 'r') as f:
        linii = f.readlines()

    prima_linie = linii[0].strip().lower()
    parti = prima_linie.split(',')
    p = float(parti[0].split(':')[1].strip())
    n = int(parti[1].split(':')[1].strip())  
    valori = []
    frecvente = []

    for linie in linii[1:]:
        if "succese" in linie:
            numar_succese = int(linie.split("succese")[0].strip())
            frecventa = int(linie.split(":")[1].strip().split()[0])
            valori.append(numar_succese)
            frecvente.append(frecventa)
    
    plt.figure(figsize=(8, 4))
    plt.bar(valori, frecvente, align='center', edgecolor='black')
    plt.title(f"Distribuția binomială (n={n}, p={p})")
    plt.xlabel("Număr de succese")
    plt.ylabel("Frecvență")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    print(f"Probabilitatea: {p}, Număr de încercări: {n}")
    print("Distribuția:", dict(zip(valori, frecvente)))

def Geometrica():   
    
    with open("Simulari\\Geometrica.txt", 'r') as f:
        linii = f.readlines()   
    p = float(linii[0].split(":")[1].strip())
    date = []
    for linie in linii[1:]:
        valoare = int(linie.split(":")[1].strip())
        date.append(valoare)

    data_geom = np.array(date)
    '''plt.figure(figsize=(8, 4))'''
    plt.hist(data_geom, bins=range(1, max(data_geom)+1), align='left', edgecolor='black')
    plt.title(f"Simularea distributiei geometrice cu probabilitatea: {p} %")
    plt.xlabel("Numarul de încercari până la primul succes")
    plt.ylabel("Frecvență")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def Poisson():

    with open("Simulari\\Poisson.txt", 'r') as f:
        linii = f.readlines() 
    prima_linie = linii[0].strip().lower()
    parti = prima_linie.split(',')

    lam = float(parti[0].split(':')[1].strip())
    interval = int(parti[1].split(':')[1].strip())  

    date = [int(l.strip()) for l in linii[1:] if l.strip().isdigit()]
    data_poisson = np.array(date)
    valori, frecvente = np.unique(data_poisson, return_counts=True)

    plt.figure(figsize=(8, 4))
    plt.bar(valori, frecvente, align='center', edgecolor='black')
    plt.title(f"Distribuția Poisson (λ = {lam})")
    plt.xlabel("Număr de apariții")
    plt.ylabel("Frecvență")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    print(f"Lambda: {lam}")
    print("Distribuția:", dict(zip(valori, frecvente)))

def Exponentiala():
    with open("Simulari\\Exponentiala.txt", 'r') as f:
        linii = f.readlines()
    prima_linie = linii[0].strip().lower()
    parti = prima_linie.split(',')
    nr_incerari = int(parti[0].split(':')[1].strip())
    lam = float(parti[1].split(':')[1].strip())
    date = [float(l.strip()) for l in linii[1:] if l.strip()]
    data_exp = np.array(date)

    plt.figure(figsize=(8, 4))
    plt.hist(data_exp, bins='auto', edgecolor='black')
    plt.title(f"Distribuția exponențială simulată (λ = {lam})")
    plt.xlabel("Timp între evenimente")
    plt.ylabel("Frecvență")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    print(f"Lambda (rata): {lam}, Număr de încercări: {nr_incerari}")
    print("Valori generate:", data_exp)

def Uniforma():
    with open("Simulari\\Uniforma.txt", 'r') as f:
        linii = f.readlines()

    prima_linie = linii[0].strip().lower()
    parti = prima_linie.split(',')
    a = float(parti[0].split(':')[1].strip())
    b = float(parti[1].split(':')[1].strip())
    date = [float(l.strip()) for l in linii[1:] if l.strip()]
    data = np.array(date)
    plt.figure(figsize=(10, 2))
    plt.scatter(data, np.zeros_like(data), color='green', label='Valori generate')
    plt.axvline(a, color='red', linestyle='--', label=f'a = {a}')
    plt.axvline(b, color='blue', linestyle='--', label=f'b = {b}')
    plt.axhline(0, color='black', linewidth=1)
    plt.title(f"Distribuția Uniformă [{a}, {b})")
    plt.xlabel("Valori")
    plt.yticks([])  
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()

    print(f"a = {a}, b = {b}")
    print("Valori generate:", data)

def Uniforma2():
    with open("Simulari\\Uniforma2.txt", 'r') as f:
        linii = f.readlines()

    prima_linie = linii[0].strip().lower()
    parti = prima_linie.split(',')
    a = float(parti[0].split(':')[1].strip())
    b = float(parti[1].split(':')[1].strip())

    date = [float(l.strip()) for l in linii[1:] if l.strip()]
    data = np.array(date)

    plt.figure(figsize=(10, 2))
    plt.scatter(data, np.zeros_like(data), color='green', label='Valori generate', zorder=3)
    plt.axvline(a, color='red', linestyle='--', label=f'a = {a}', zorder=2)
    plt.axvline(b, color='blue', linestyle='--', label=f'b = {b}', zorder=2)
    plt.axhline(0, color='black', linewidth=1, zorder=1)
    plt.title(f"Distribuția Uniformă Continuă pe intervalul [{a}, {b})")
    plt.xlabel("Valori")
    plt.yticks([])  
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

    print(f"Interval: [{a}, {b})")
    print("Valori generate:", data)

def Normala():
    with open("Simulari\\Normala.txt", 'r') as f:
        linii = f.readlines()
    prima_linie = linii[0].strip().lower()
    parti = prima_linie.split(',')
    medie = float(parti[0].split(':')[1].strip())
    deviatia = float(parti[1].split(':')[1].strip())
    nr_simulari = int(parti[2].split(':')[1].strip())
    date = [float(l.strip()) for l in linii[1:] if l.strip()]
    data = np.array(date)

    plt.figure(figsize=(8, 4))
    plt.hist(data, bins=10, color='skyblue', edgecolor='black')
    plt.axvline(medie, color='red', linestyle='--', linewidth=2, label=f'Medie = {medie}')
    plt.title(f"Distribuția Normală (μ = {medie}, σ = {deviatia})")
    plt.xlabel("Valori")
    plt.ylabel("Frecvență")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()

    print(f"Media: {medie}, Deviația: {deviatia}, Număr simulări: {nr_simulari}")
    print("Valori generate:", data)
                               
def Dreptunghi():
    x = []
    y = []
    with open("Simulari\\Dreptunghi.txt", "r") as f:
        linie = f.readline()
        parte = linie.split(",")
        for linie in f:
            temp = linie.strip().split()
            x.append(float(temp[0]))
            y.append(float(temp[1]))
    a = float(parte[0].split(":")[1])
    b = float(parte[1].split(":")[1])
    c = float(parte[2].split(":")[1])
    d = float(parte[3].split(":")[1])

    plt.plot(a, c, 'ro',ms = 7)
    plt.plot(b, d, 'ro',ms = 7)
    plt.plot(x, y, 'ko')
    plt.text(a, c, f"  ({a}, {b})", color="red", fontsize=9)
    plt.text(b, d, f"  ({c}, {d})", color="red", fontsize=9)
    plt.xlabel("Axa X")
    plt.ylabel("Axa Y")
    plt.title("Distribuția uniformă pe dreptunghi (vector)")
    plt.grid(True)
    plt.tight_layout()    
    plt.show()

def Disc():
    x = []
    y = []
    with open("Simulari\\Disc.txt", "r") as f:
        linie = f.readline()
        r = float(linie.split(":")[1])
        for linie in f:
            temp = linie.strip().split()
            x.append(float(temp[0]))
            y.append(float(temp[1]))

    theta = np.linspace(0, 2 * np.pi, 100)
    x1 =r* np.cos(theta)
    y1 =r* np.sin(theta)

    plt.plot(x1, y1, color='blue', linewidth=2)
    plt.plot(x, y, 'ko')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel("Axa X")
    plt.ylabel("Axa Y")
    plt.title("Distribuția uniformă pe disc (vector)")
    plt.grid(True)
    plt.tight_layout()    
    plt.show()

def Elipsa():
    x = []
    y = []
    with open("Simulari\\Elipsa.txt", "r") as f:
        linie = f.readline()
        parte = linie.split(",")
        a = float(parte[0].split(":")[1])
        b = float(parte[1].split(":")[1])
        for linie in f:
            temp = linie.strip().split()
            x.append(float(temp[0]))
            y.append(float(temp[1]))

    theta = np.linspace(0, 2 * np.pi, 100)
    x1 =a* np.cos(theta)
    y1 =b* np.sin(theta)

    plt.plot(x1, y1, color='blue', linewidth=2)
    plt.plot(x, y, 'ko')
    plt.xlabel("Axa X")
    plt.ylabel("Axa Y")
    plt.title("Distribuția uniformă pe elipsă (vector)")
    plt.grid(True)
    plt.tight_layout()    
    plt.show()


'''Bernoulli("bernoulli.txt")'''
'''Geometrica('geometrica.txt')'''
# Binomiala('binomiala.txt')
# Poisson('poisson.txt')
# Exponentiala('exponentiala.txt')
# Uniforma('uniforma.txt')
# Normala("normala.txt")
# Dreptunghi('dreptunghi.txt')
# Disc('disc.txt')
# Elipsa('elipsa.txt')
# Uniforma2()
