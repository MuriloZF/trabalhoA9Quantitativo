import math

erp = []
size = 208 # Quantidade de valores -1
def collect():
    with open("dataset/machine.data", "r") as f:
        for line in f:
            columns = line.strip().split(",")
            erp.append(int(columns[9]))


def main():
    collect()
    erp.sort() # Passo 1- Rol
    amplitude = erp[size] - erp[0] # Passo 2- Amplitude
    classe = math.ceil(1 + 3.33 * math.log10(size)) # Passo 3- Quantidade de classes ( Arredonda para cima)
    amplitudeClasse = math.ceil(amplitude / classe) # Passo 4- Amplitude de classes (Arredonda para cima)
    print(erp)
    print(f'Amplitude: {amplitude}')
    print(f'Classe: {classe}')
    print(f'Amplitude Classe: {amplitudeClasse}')

main()
