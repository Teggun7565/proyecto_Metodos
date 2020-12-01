import random
import numpy as np
# from webweb import Web


# Inventario de objetos y parametros
dis_porcentaje = ["0"] * 65 + ["1"] * 20 + ["2"] * 15
stamina = 100
vidaInicial = 100
tutorial_combate = False
#------------------------------------------------------


# metodo que genera una matriz adyacente que representara el mapa
def generador_mapa(n):
    global dis_porcentaje
    mapa = [[random.choice(dis_porcentaje)
             for i in range(n)] for j in range(n)]

    # for i in range(n):
    #     mapa[i][i] = "0"

    for i in range(n):
        for j in range(n):
            mapa[j][i] = mapa[i][j]

    # for x in range(n):
    #     print(mapa[x])

    mapa_bordado = np.pad(
        mapa, pad_width=1, mode="constant", constant_values="#")

    # for x in range(n + 2):
    #     print(mapa_bordado[x])
    # web = Web(mapa)
    # web.display.scaleLinkWidth = True
    # web.show()

    return mapa_bordado
#------------------------------------------------------


# metodo para imprimir el mapa actual
def displayMap(mapa, n):
    for x in range(n + 2):
        print(mapa[x])
#------------------------------------------------------


# metodo que controla el movimiento del usuario
def movimiento(mapaElegido, posicion, n):
    posicion_pasada = None
    x = 0
    valorY = n / 2
    y = int(valorY)

    posicion = None

    while posicion != "C":

        x_pasada = x
        y_pasada = y

        mover = input("N, S, E, O, MAPA \n>>>").upper()

        if mover == "N":
            y = y - 1

        if mover == "S":
            y = y + 1

        if mover == "E":
            x = x + 1

        if mover == "O":
            x = x - 1

        if mover == "MAPA":
            displayMap(mapaElegido, n)
            print("\n")

        posicion = mapaElegido[y][x]
        mapaElegido[y][x] = "x"

        if posicion == "x" and posicion_pasada != "x" and mover != "MAPA":
            print("Retrocedes pasos...")

        if posicion == "1":
            print("Te enfrentas contra un enemigo!\n")
            print("--------------------------------------------------------------\n")
            combate()

        if posicion == "#":
            print("Este es el borde! No puedes seguir adelante!")
            x = x_pasada
            y = y_pasada
            posicion = mapaElegido[y][x]

    print("\nHaz capturado el castillo enemigo!")
    print("ERES VICTORIOSO!")
#------------------------------------------------------


# metodo de combate, genera las escenas de combate
def combate():
    global tutorial_combate
    if tutorial_combate == False:
        print("\tHaz empezado una plea contra un enemigo!")
        print("\tEsto ssignifica que solo uno saldra vivo de esto!")

        print("\nComo Jugar\n\nEl jugador tomara turnos en elegir movimientos.")
        print("Cada movimiento tiene su rango de daño, sea largo o corto.")
        print("Incluso hasta te puedes curar! (Nota: Puedes fallar el movimiento!)")

        print("\nLos oponentes comienzan con 100 de vida cada uno.")
        print("El primero al reducir a su enemigo a 0 sera el ganador!")

        print("\nEso es todo! Buena suerte!")
        tutorial_combate = True

    jugando = True

    while jugando:
        global vidaInicial
        ganador = None
        vidaActual = vidaInicial
        vidaEnemigo = 100

        turno = random.randint(1, 2)
        if turno == 1:
            turnoJugador = True
            turnoEnemigo = False
            print("\nAtacas primero!")
        else:
            turnoJugador = False
            turnoEnemigo = True
            print("\nTu enemigo ataca primero!")

        print("\nTu vida: ", vidaActual,
              "Vida Enemiga: ", vidaEnemigo)

        while (vidaActual != 0 or vidaEnemigo != 0):

            subirVida = False
            fallar = False

            moves = {"Golpe": random.randint(18, 25),
                     "Golpe Fuerte": random.randint(10, 35),
                     "Curar": random.randint(20, 25)}

            if turnoJugador:
                print("\nElija un movimiento:\n1. Golpe (Daño entre 18-25)\n2. Golpe Fuerte (Daño entre 10-35)\n3. Curar (Restaurar de 20-25 de vida)\n")

                movimiento_jugador = input("> ").lower()

                movimiento_falla = random.randint(1, 5)
                if movimiento_falla == 1:
                    fallar = True
                else:
                    fallar = False

                if fallar:
                    movimiento_jugador = 0
                    print("Fallaste!")
                else:
                    if movimiento_jugador in ("1", "golpe"):
                        movimiento_jugador = moves["Golpe"]
                        print("\nUsaste Golpe. Hizo ",
                              movimiento_jugador, " de daño.")
                    elif movimiento_jugador in ("2", "golpe fuerte"):
                        movimiento_jugador = moves["Golpe Fuerte"]
                        print("\nUsaste Golpe Fuerte. Hizo ",
                              movimiento_jugador, " de daño.")
                    elif movimiento_jugador in ("3", "curar"):
                        subirVida = True
                        movimiento_jugador = moves["Curar"]
                        print("\nUsaste Curar. Recuperaste ",
                              movimiento_jugador, " de vida.")
                    else:
                        print("\nEso no es un movimiento valido; intente de nuevo.")
                        continue

            else:

                movimiento_falla = random.randint(1, 5)
                if movimiento_falla == 1:
                    fallar = True
                else:
                    fallar = False

                if fallar:
                    movimiento_enemigo = 0
                    print("Tu enemigo fallo!")
                else:
                    if vidaEnemigo > 30:
                        if vidaActual > 75:
                            movimiento_enemigo = moves["Golpe"]
                            print("\nEl enemigo utiliza Golpe. Hizo ",
                                  movimiento_enemigo, " de daño.")
                        elif vidaActual > 35 and vidaActual <= 75:
                            imoves = ["Golpe", "Golpe Fuerte"]
                            imoves = random.choice(imoves)
                            movimiento_enemigo = moves[imoves]
                            print("\nEl enemigo utiliza ", imoves,
                                  ". Hizo ", movimiento_enemigo, " de daño.")
                        elif vidaActual <= 35:
                            movimiento_enemigo = moves["Golpe Fuerte"]
                            print("\nEl enemigo utiliza Fuerte Golpe. Hizo ",
                                  movimiento_enemigo, " de daño.")
                    else:
                        Curar_o_pelear = random.randint(1, 2)
                        if Curar_o_pelear == 1:
                            subirVida = True
                            movimiento_enemigo = moves["Curar"]
                            print("\nEl enemigo usa Curar. recupera ",
                                  movimiento_enemigo, " de vida.")
                        else:
                            if vidaActual > 75:
                                movimiento_enemigo = moves["Golpe"]
                                print("\nEl enemigo usa Golpe. Hizo ",
                                      movimiento_enemigo, " de daño.")
                            elif vidaActual > 35 and vidaActual <= 75:
                                imoves = ["Golpe", "Golpe Fuerte"]
                                imoves = random.choice(imoves)
                                movimiento_enemigo = moves[imoves]
                                print("\nEl enemigo utiliza ", imoves,
                                      ". Hizo ", movimiento_enemigo, " de daño.")
                            elif vidaActual <= 35:
                                movimiento_enemigo = moves["Golpe Fuerte"]
                                print(
                                    "\nEl enemigo utiliza Golpe Fuerte. Hizo ", movimiento_enemigo, " de daño.")

            if subirVida:
                if turnoJugador:
                    vidaActual += movimiento_jugador
                    if vidaActual > vidaInicial:
                        vidaActual = vidaInicial
                else:
                    vidaEnemigo += movimiento_enemigo
                    if vidaEnemigo > 100:
                        vidaEnemigo = 100
            else:
                if turnoJugador:
                    vidaEnemigo -= movimiento_jugador
                    if vidaEnemigo < 0:
                        vidaEnemigo = 0
                        ganador = "Jugador"
                        break
                else:
                    vidaActual -= movimiento_enemigo
                    if vidaActual < 0:
                        vidaActual = 0
                        ganador = "Enemigo"
                        break

            print("\nTu vida: ", vidaActual,
                  "Vida enemiga: ", vidaEnemigo)

            turnoJugador = not turnoJugador
            turnoEnemigo = not turnoEnemigo

        if ganador == "Jugador":
            print("\nTu vida: ", vidaActual,
                  "Vida enemiga: ", vidaEnemigo)
            print("\nFelicitaciones! Ganaste, ahora vas por la victoria!!")
        else:
            print("\nTu vida: ", vidaActual,
                  "Vida enemiga: ", vidaEnemigo)
            print(
                "\nHaz sido derrotado... no podras continuar")
            print("Quieres empezar de nuevo?")
            re_set = input(">").lower()

        if ganador != "Jugador":
            if re_set == "si" or "Si":
                reset()
            else:
                exit()

        if ganador == "Jugador":
            jugando = False

#------------------------------------------------------


# metodo de estados, donde se toma registro del estado del usuario

#------------------------------------------------------


# posicionamiento en el tablero
custom_Value = int(input("Tamaño de matriz:\n>>>"))
mapaElegido = generador_mapa(custom_Value)
posicion = mapaElegido[0][0]
valorY = int(custom_Value / 2)
mapaElegido[valorY][0] = "S"
mapaElegido[valorY][custom_Value + 1] = "C"
displayMap(mapaElegido, custom_Value)


#------------------------------------------------------


# metodo principal, el que corre todos los metodos (main)
def main():
    generador_mapa(custom_Value)
    movimiento(mapaElegido, posicion, custom_Value)


main()
#------------------------------------------------------


# metodo que resetea los estados
def reset():
    print("\n\n-------------------Nueva Partida-------------------\n\n")
    custom_Value = int(input("Tamaño de matriz:\n>>>"))
    dis_porcentaje = ["0"] * 65 + ["1"] * 20 + ["2"] * 15
    stamina = 100
    vidaInicial = 100
    tutorial_combate = False
    mapaElegido = generador_mapa(custom_Value)
    posicion = mapaElegido[0][0]
    valorY = int(custom_Value / 2)
    mapaElegido[valorY][0] = "S"
    mapaElegido[valorY][custom_Value + 1] = "C"
    displayMap(mapaElegido, custom_Value)
    movimiento(mapaElegido, posicion, custom_Value)

#------------------------------------------------------
