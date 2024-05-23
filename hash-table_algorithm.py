class HashTable:
    # Constructor de la clase
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    # Función de hash para calcular la posición basada en la clave
    def hash_function(self, key):
        return key % self.size

    # Función para insertar un par clave-valor en la tabla hash
    def insert(self, key, data):
        hash_value = self.hash_function(key)

        # Sondeo cuadrático en caso de colisión
        step = 1
        while self.table[hash_value] is not None:
            hash_value = (hash_value + step**2) % self.size
            step += 1

        # Inserta el par clave-valor en la posición encontrada
        self.table[hash_value] = (key, data)

    # Función para buscar el valor asociado a una clave
    def search(self, key):
        original_hash = self.hash_function(key)
        hash_value = original_hash
        step = 1

        # Sondeo cuadrático para buscar la clave
        while self.table[hash_value] is not None:
            if self.table[hash_value][0] == key:
                return self.table[hash_value][1]
            hash_value = (original_hash + step**2) % self.size
            step += 1

        return None  # Retorna None si no se encuentra la clave

# Ejemplo de uso
hash_table = HashTable(50)
hash_table.insert(1, 'A')
hash_table.insert(11, 'B')
hash_table.insert(21, 'C')
hash_table.insert(31, 'D')
hash_table.insert(41, 'E')
hash_table.insert(51, 'F')
hash_table.insert(61, 'G')
hash_table.insert(71, 'H')
hash_table.insert(81, 'I')
hash_table.insert(91, 'J')

print(hash_table.search(1))
print(hash_table.search(11))
print(hash_table.search(21))
print(hash_table.search(31))
print(hash_table.search(41))
print(hash_table.search(51))
print(hash_table.search(61))
print(hash_table.search(71))
print(hash_table.search(81))
print(hash_table.search(91))

