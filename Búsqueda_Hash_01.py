"""
Created on Monday 25/11/24

@author: Victor Mendoza
"""

def contiene_duplicados(lista):
    hash_table = {}
    print("\nLa lista es:", lista)

    for elemento in lista:
        if elemento in hash_table:
            return True  # Duplicado encontrado
        hash_table[elemento] = True
    return False  # No se encontraron duplicados

# Ejemplo de uso
lista = []

cantidad = int(input("Ingrese la cantidad de elementos que tendrá la lista: "))

for i in range(cantidad):
    elemento = int(input("\nIngrese un número: "))
    lista.append(elemento)

lista.sort()

print("¿Contiene duplicados?", contiene_duplicados(lista))