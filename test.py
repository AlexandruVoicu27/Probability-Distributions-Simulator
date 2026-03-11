import numpy as np
import matplotlib.pyplot as plt

def plot_Bernoulli_from_file(filename):
    # Citim valorile din fișier
    with open('rezultate.txt', 'r') as f:
        data = [int(line.strip()) for line in f if line.strip() in ['0', '1']]

    data = np.array(data)

    # Calculează frecvențele
    values, counts = np.unique(data, return_counts=True)

    # Plot
    plt.figure(figsize=(6, 4))
    plt.bar(values, counts, tick_label=["0 (Eșec)", "1 (Succes)"])
    plt.title("Simularea Distribuției Bernoulli din fișier")
    plt.xlabel("Rezultat")
    plt.ylabel("Frecvență")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    # Afișează valorile brute
    print("Frecvențe:", dict(zip(values, counts)))