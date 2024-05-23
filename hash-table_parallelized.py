from numba import njit, prange, config
import numpy as np

# Habilitar diagnósticos de paralelización
config.THREADING_LAYER = 'omp'

class ParallelHashTable:
    def __init__(self, size):
        self.size = size
        self.keys = np.full(size, -1, dtype=np.int32)  # Array para las claves
        self.data = np.full(size, -1, dtype=np.int32)  # Array para los datos

    def hash_function(self, key):
        return key % self.size

    @staticmethod
    @njit(parallel=True)
    def insert_multiple(keys, data, size, new_keys, new_values):
        for i in prange(len(new_keys)):
            key = new_keys[i]
            value = new_values[i]
            hash_value = key % size
            step = 1
            while keys[hash_value] != -1:
                hash_value = (hash_value + step**2) % size
                step += 1
                if step > size:
                    break  # Rompe el bucle si no hay espacio
            keys[hash_value] = key
            data[hash_value] = value

    @staticmethod
    @njit
    def search(keys, data, size, key):
        original_hash = key % size
        hash_value = original_hash
        step = 1
        while keys[hash_value] != -1:
            if keys[hash_value] == key:
                return data[hash_value]
            hash_value = (original_hash + step**2) % size
            step += 1
            if step > size:
                break
        return -1  # Usamos -1 para indicar que no se encontró el valor

    def insert_keys(self, new_keys, new_values):
        ParallelHashTable.insert_multiple(self.keys, self.data, self.size, new_keys, new_values)

    def search_key(self, key):
        return ParallelHashTable.search(self.keys, self.data, self.size, key)

# Ejemplo de uso de la tabla hash paralelizada
hash_table = ParallelHashTable(50)

# Inserta varios pares clave-valor en la tabla
keys_to_insert = np.array([1, 11, 21, 31, 41, 51, 61, 71, 81, 91], dtype=np.int32)
values_to_insert = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], dtype=np.int32)
hash_table.insert_keys(keys_to_insert, values_to_insert)

# Pruebas de búsqueda
print(hash_table.search_key(1))
print(hash_table.search_key(11))
print(hash_table.search_key(21))
print(hash_table.search_key(31))
print(hash_table.search_key(41))
print(hash_table.search_key(51))
print(hash_table.search_key(61))
print(hash_table.search_key(71))
print(hash_table.search_key(81))
print(hash_table.search_key(91))