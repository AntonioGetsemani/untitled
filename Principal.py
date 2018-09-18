__author__='Antonio Getsemani'

from Memoria_Dinamica import *
lista = []
TiendaDeRopa = ['Playera' , 'Pantalones' , 'Zapatos' , 'Tennis' , 'Pulseras']
precios = [600, 500, 400, 300, 200]
listas= Memoria_Dinamica(TiendaDeRopa)
listas.imprimirLista()
listas.ordenarLista()
listas.imprimirLista()
listas.recorrerArreglo()
listas.imprimirLista()
listas.agregarelementoarray('Gorras')
listas.imprimirLista()
listas.eliminarElemento('Playera')
listas.imprimirLista()
lista2 =Memoria_Dinamica(precios)
lista2.imprimirLista()
lista2.agregarelementoarray(100)
lista2.imprimirLista()