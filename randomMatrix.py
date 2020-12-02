import numpy as np
import random


dis_porcentaje = [1] * 65 + [2] * 20 + [3] * 15


class nodo:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class mapaMatriz:
    def __init__(self, n):
        self.tamaño = n
        self.matrizAdj = []
        for i in range(n):
            self.matrizAdj.append([0 for i in range(self.tamaño)])

    def relacion_matriz(self, v1, v2, peso):
        if v1 == v2:
            return
        else:
            nodo1 = nodo(v1)
            nodo1.next = self.matrizAdj[v2]
            nodo2 = nodo(v2)
            nodo2.next = self.matrizAdj[v1]
            self.matrizAdj[v1][v2] = peso
            self.matrizAdj[v2][v1] = peso

    def generar_matriz(self):
        global dis_porcentaje
        for c in range(self.tamaño):
            for i in range(self.tamaño):
                pesoAl = random.choice(dis_porcentaje)
                self.relacion_matriz(c, i, pesoAl)

    def imprimir_mapa(self):
        for x in range(self.tamaño):
            print(self.matrizAdj[x])

    def imprimir_relaciones(self):
        for j in range(self.tamaño):
            print("Lista de Relaciones del vertice {}\n Cabeza".format(j), end="")
            for i in range(self.tamaño):
                temp = nodo(self.matrizAdj[i][j])
                if j == i:
                    continue
                else:
                    while temp:
                        print(" --(", temp.vertex, ")--> {}".format(i), end="")
                        temp = temp.next
            print("\n")


mapa = mapaMatriz(10)
mapa.generar_matriz()
mapa.imprimir_mapa()
mapa.imprimir_relaciones()
