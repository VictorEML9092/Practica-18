"""
Created on Monday 25/11/24

@author: Victor Mendoza
"""

def dos_punteros(lista):
    lista.sort()  # Asegura que esté ordenada
    izquierda, derecha = 0, len(lista) - 1

    print("\nLa lista es:", lista)
    objetivo = int(input("\nIngrese el número que desea buscar: "))

    while izquierda < derecha:
        suma = lista[izquierda] + lista[derecha]
        if suma == objetivo:
            return (lista[izquierda], lista[derecha])
        elif suma < objetivo:
            izquierda += 1
        else:
            derecha -= 1
    return None

# Ejemplo de uso
lista = []

cantidad = int(input("Ingrese la cantidad de elementos que tendrá la lista: "))

for i in range(cantidad):
    elemento = int(input("\nIngrese un número: "))
    lista.append(elemento)

print(dos_punteros(lista))  # (2, 7)