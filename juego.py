 
import random

op = 1
# valor = 0

victorias = derrotas = empates = 0;

# 1 si gana el jugador
# 2 si gana la maquina
# 0 empate
def verificar_resultado(jugador, maquina):
    if jugador == maquina:
        return 0
    elif jugador == 1:
        if maquina == 2:
            return 2
        elif maquina == 3:
            return 1
    elif jugador == 2:
        if maquina == 1:
            return 1
        elif maquina == 3:
            return 2
    elif jugador == 3:
        if maquina == 1:
            return 2
        elif maquina == 2:
            return 1

def calcular_resultado(resultado):
    global victorias, derrotas, empates
    if resultado == 0:
        empates += 1
    elif resultado == 1:
        victorias += 1
    else:
        derrotas += 1

def mostrar_resultado():
    print('Empates:', empates)
    print('Victorias:', victorias)
    print('Derrotas:', derrotas)

def menu():
    print('<1> Jugar')
    print('<2> Resultados')
    print('<0> Salir')

def input_num():
    valor = 0
    while valor<1 or valor>3:
        valor = int(input('Ingrese valor: 1. piedra, 2. papel, 3. tijera: '))
    return valor

def jugar():
    op = -1
    while op != 0:
        menu()

        op = int(input('Ingrese opcion: '))

        if op == 1:
            valor = input_num()
            num = random.randint(1, 3)

            resultado = verificar_resultado(valor, num)
            calcular_resultado(resultado)
            
        elif op == 2:
            mostrar_resultado()

        valor = 0


jugar()