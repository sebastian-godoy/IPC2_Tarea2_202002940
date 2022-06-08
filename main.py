from lista_c import lista

hola = lista()
hola.agregar(1)
hola.agregar(2)
hola.agregar(3)
hola.agregar(4)
hola.agregar(5)
hola.imprimir()
print("Por favor, ingrese el numero del cual desea ver los datos: ")
eleccion = int(input())
print("Su numero actual es: ")
print(hola.buscar(eleccion))