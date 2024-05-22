import random

luby_values = [1]  # Inicializa la lista de valores generados

def luby_sequence():
    global luby_values  # Permitir el acceso a la variable global
    yield 1  # El primer valor de la secuencia es siempre 1
    seq_len = 1  # Inicializa la longitud de la secuencia
    while True:
        for i in range(1 << seq_len):
            luby_values.append(seq_len)  # Agrega cada valor de la secuencia a la lista
            yield seq_len  # Produce cada valor de la secuencia
        seq_len += 1  # Aumenta la longitud de la secuencia

def main():
    luby_gen = luby_sequence()
    for _ in range(150000):
        current_value = next(luby_gen)
        print("Valor de la secuencia de Luby:", current_value)
        #print("Lista completa de valores generados:", luby_values) 
       

if __name__ == "__main__":
    main()
