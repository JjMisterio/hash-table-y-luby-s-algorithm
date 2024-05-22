import numba as nb
import numpy as np

#For better results execute this code in a Google Colab instance

@nb.njit(parallel=True) #Se usa el modificador para activar la paralelizacion
def luby_sequence(n):
    luby_values = [1]  # Inicializa la lista de valores generados
    seq_len = 1  # Inicializa la longitud de la secuencia
    while len(luby_values) < n:
        for _ in nb.prange(1 << seq_len): #Se usa prange para inicializar el loop en paralelo con numba
            luby_values.append(seq_len)  # Agrega cada valor de la secuencia a la lista
        seq_len += 1  # Aumenta la longitud de la secuencia
    return luby_values

def main():
    n = 150000  # Número de elementos a generar
    luby_values = luby_sequence(n)
    for value in luby_values:
        print("Valor de la secuencia de Luby:", value)
        #print("Lista completa de valores generados:", luby_values)
        #NO USAR la lista completa de valores con 150k elementos o más

if __name__ == "__main__":
    main()

