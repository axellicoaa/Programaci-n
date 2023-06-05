import random
op = 1
valor = 0
victorias = 0; derrotas = 0; empates = 0 
def verificar_resultado(jugador, maquina): #Función 1
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

def calcular_resultado(resultado): #Función 2
    global victorias, derrotas, empates
    if resultado == 0:
        empates += 1
    elif resultado == 1:
        victorias += 1
    else:
        derrotas += 1 

def mostrar_resultado(): #Función 3
    print("Victorias:", victorias)
    print("Derrotas:", derrotas)
    print("Empates:", empates)

def menu():#Función 4
    print("<1>Jugar")
    print("<2>Resultados")
    print("<0>Salir")

def quit(): #Función 5
    print("Gracias por jugar")

print("<<<JUEGO DE PIEDRA, PAPEL O TIJERA>>>")
while op != 0:
    menu()
    op = int(input("Ingrese opción: "))
    if op == 1 :
            valor = int(input("Ingrese valor: <1.Piedra>, <2.Papel>, <3.Tijera>: "))
            num = random.randint(1,3)
            if valor == 1:
                if num == 2:
                    print("Pierdes: ", "piedra", "vs", "papel")
                    derrotas += 1
                elif num == 3:
                    print("Ganas: ", "piedra", "vs", "tijera")
                    victorias += 1
                elif valor == num:
                     print("Empatan: ", "piedra", "vs", "piedra")
                     empates += 1    
            if valor == 2:
                if num == 1:
                    print("Ganas: ", "papel", "vs", "piedra")
                    victorias += 1
                elif num == 3:
                    print("Pierdes: ", "papel", "vs", "tijera")
                    derrotas += 1
                elif valor == num:
                     print("Empatan: ", "papel", "vs", "papel")
                     empates += 1
            if valor == 3:
                if num == 1:
                    print("Pierdes: ", "tijera", "vs", "piedra")
                    derrotas += 1
                elif num == 2:
                     print("Ganas: ", "tijera", "vs", "papel")
                     victorias += 1
                elif valor == num:
                     print("Empatan: ", "tijera", "vs", "tijera")
                     empates += 1
            if valor >3:
                print("Error")
    elif op == 2:
        mostrar_resultado()
    elif op == 0:
        quit()
    else: 
        print("Ingresaste valor erroneo")
resultado = verificar_resultado(valor, num)
calcular_resultado(resultado)