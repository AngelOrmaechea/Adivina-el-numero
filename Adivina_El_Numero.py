from random import randint


print("Bienvenido a Adivina el numero.")

nombre = input("¿Como te llamas? ")

print(f"Hola {nombre}, estoy pensando en un numero entre 1 y 100...")

intentos = 0

intentos_restantes = 8

jugador = 0

numero = randint(1,100)

while intentos != 8:

    jugador = int(input("En que numero estoy pensando? "))

    if jugador not in range(1, 101):
        print(f"{jugador} NO esta permitido, tiene que ser entre 0 y 100.")
    elif jugador < numero:
        print("No, ese no es mi numero, es un numero mas ALTO.")
    elif jugador > numero:
        print("No, ese no es mi numero, es un numero mas BAJO.")
    else:
        print(f"Bien echo {nombre}, estaba pensando en {numero}, HAS GANADO.")
        break

    intentos += 1
    intentos_restantes -= 1
    print(f"----Numero de intentos: {intentos}, te quedan {intentos_restantes}----")

if jugador != numero:
    print(f"Se han acabado los intentos, perdiste. El numero en el que estaba pensando era {numero}.")

print("----------Fin Del Juego----------")