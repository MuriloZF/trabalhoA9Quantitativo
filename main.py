import math
from tabulate import tabulate


erp = []

def collect():
    with open("dataset/machine.data", "r") as f:
        for line in f:
            columns = line.strip().split(",")
            erp.append(int(columns[9]))

def table(size : int, erp : list, amplitude : int, classe : int, amplitudeClasse : int):
    index = 9*[None] # I da tabela
    for i in range(1, 10, +1):
        index[i-1] = i
    
    intervalo = 9*[None] # intervalo da tabela
    print(f'5- Intervalos:')
    for i in range(0, 9, +1):
        if i == 0:
            primeiroNumero = erp[i]
        else:
            primeiroNumero = primeiroNumero + amplitudeClasse
        print(f'Intervalo {i}: {primeiroNumero} |- {primeiroNumero + amplitudeClasse}') 
        intervalo[i] = (primeiroNumero, primeiroNumero + amplitudeClasse)

    fi = 9*[None] # fi da tabela
    for i in range(0, 9, +1):
        counter = 0
        (primeiroNumero, limite) = intervalo[i]
        for valor in erp:
            if valor >= primeiroNumero and valor < limite:
                counter += 1
        fi[i] = counter
    print(f'6- Fi: {fi}')
    #prova real fi
    soma = 0
    for i in range(0, 9, +1):
        soma += fi[i]
    print(f'Prova real fi: {soma}')

    xi = 9*[None] # xi da tabela
    for i in range(0, 9, +1):
        (primeiroNumero, limite) = intervalo[i]
        xi[i] = math.ceil((primeiroNumero + limite) / 2)
    print(f'7- Xi: {xi}')

    frequenciaAcumulada = 9*[None] # Fi da tabela
    somaFi = 0
    for i in range(0, 9, +1):
        somaFi += fi[i]
        frequenciaAcumulada[i] = somaFi
    print(f'8- Fi: {frequenciaAcumulada}')

    # Montagem da tabela
    tabela = [["i", index],["intervalo", intervalo],["fi", fi],["xi", xi],["Fi", frequenciaAcumulada]]
    print(tabulate(tabela, tablefmt="rounded_grid"))


def main():
    collect()
    print(f'ERP: {erp}')
    size = len(erp)
    erp.sort() # Passo 1- Rol
    amplitude = erp[size - 1] - erp[0] # Passo 2- Amplitude
    classe = math.ceil(1 + 3.33 * math.log10(size)) # Passo 3- Quantidade de classes ( Arredonda para cima)
    amplitudeClasse = math.ceil(amplitude / classe) # Passo 4- Amplitude de classes (Arredonda para cima)
    print(f'1- rol: {erp}')
    print(f'2- Amplitude: {amplitude}')
    print(f'3- Classe: {classe}')
    print(f'4- Amplitude Classe: {amplitudeClasse}')
    table(size, erp, amplitude, classe, amplitudeClasse) 
main()
