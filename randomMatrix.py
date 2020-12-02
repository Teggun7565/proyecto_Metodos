import numpy as np
import random


class mapaMatriz():
	def __init__(self, n):



    def generador_mapa(self):
        global dis_porcentaje
        mapa = [[random.choice(dis_porcentaje)
                 for i in range(n)] for j in range(n)]

        mapa_bordado = np.pad(
            mapa, pad_width=1, mode="constant", constant_values="#")

        return mapa_bordado
