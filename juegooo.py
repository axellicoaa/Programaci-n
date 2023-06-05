import random 
import time 
import os 

def dibujo(jugada): 
    if jugada == "Piedra": 
        print("                 @@")
        print("                @@@") 
    elif jugada == "Papel": 
        print("                ===")
        print("                ===") 
    elif jugada == "Tijeras": 
        print("                 //")
        print("                 OO") 
    
def panel_puntuacion (puntos_jugador, puntos_ordenador, numero_jugada): 
        
        os.system("cls") 
        
        print()
        print(" PIEDRA, PAPEL, TIJERAS: {} de 10".format(numero_jugada)) 
        print(" --------------------")  
        print(" Puntos tu: {} - {} : Ordenador".format(puntos_jugador,puntos_ordenador)) 
        print(" --------------------") 
        print() 

def comprobar_ganador(jugador,ordenador): 
        '''DEVUELVE EL GANADOR DE LA TIRADA ENTRE EL JUGADOR Y EL ORDENADOR''' 
        if jugador == "Piedra": 
            if ordenador == "Piedra": 
              ganador="ninguno" 
            elif ordenador == "Papel": 
              ganador="Ordenador" 
            else: 
              ganador= "Jugador" 

        elif jugador == "Papel":       
            if ordenador == "Piedra": 
              ganador="Humano" 
            elif ordenador == "Papel": 
              ganador="Ninguno" 
            else: 
              ganador= "Ordenador" 
        
        elif jugador == "Tijeras":       
            if ordenador == "Piedra": 
              ganador="ordenador" 
            elif ordenador == "Papel": 
              ganador="Jugador" 
            else: 
              ganador= "Ninguno"  
    
        return ganador 

def movimiento_jugador (): 
    '''DEVUELVE LA JUGADA QUE HACE EL JUGADOR''' 
    opciones_humano = ["Papel","Tijera","Piedra"] 
    jugada= "" 
    while jugada not in opciones_humano: 
        jugada=input("Haz tu jugada: ").capitalize() 
    else: 
        return jugada 
   
def movimiento_ordenador_con_ia(jugadas_humano,ultimo_resultado): 
     '''DEVUELVE LA JUGADA QUE HACE EL JUGADOR''' 

     if ultimo_resultado == 1:  
       if jugadas_humano [-1] == "Piedra":  
        jugada = random.choice(["Papel","Piedra"]) 
       elif jugadas_humano [-1] == "Papel": 
        jugada = random.choice(["Tijeras","Papel"])  
       elif jugadas_humano [-1] == "Tijeras": 
         jugada = random.choice(["Piedra","Tijeras"]) 
     elif ultimo_resultado==0: 
       if jugadas_humano [-1] == "Piedra": 
        jugada = random.choice(["Tijeras","Piedra"]) 
       elif jugadas_humano [-1] == "Papel": 
         jugada = random.choice(["Piedra","Papel"])  
       elif jugadas_humano [-1] == "Tijeras":  
        jugada = random.choice(["Papel","Tijeras"]) 

     return jugada

puntos_jugador=0 
puntos_ordenador=0 
numero_jugada = 1 
jugadas_humano=["Piedra"]
ultimo_resultado=1 

while True :  
    
    panel_puntuacion(puntos_jugador, puntos_ordenador, numero_jugada) 
        
    jugada_humano = movimiento_jugador () 
        
    jugada_ordenador=movimiento_ordenador_con_ia(jugadas_humano,ultimo_resultado) 
        
    ganador= comprobar_ganador(jugada_humano,jugada_ordenador) 
         
    print ( ) 
    dibujo(jugada_humano) 
    print() 
    dibujo(jugada_ordenador) 
    print() 
    print("El ordenador:",jugada_ordenador) 
    print () 
    numero_jugada+=1 
    jugadas_humano.append(jugada_humano) 

    if ganador == "Humano": 
        puntos_ordenador += 1 
        ultimo_resultado = 0 
        print("Ganas tu") 
        print () 
    elif ganador == "Ordenador": 
        puntos_ordenador += 1 
        ultimo_resultado = 0 
        print("Gana el ordenador") 
        print ()  
    elif ganador == "Ninguno":  
        print("Empate") 
        print ()  

    intput=("'Enter'para continuar") 

    if numero_jugada==10: 
        panel_puntuacion(puntos_jugador,puntos_ordenador,numero_jugada) 
        mensaje1="FIN DE PARTIDA" 
        if puntos_jugador > puntos_ordenador: 
            mensaje2="Has ganado" 
        elif puntos_jugador < puntos_ordenador: 
            mensaje2="Gana ordenador" 
        else: 
            mensaje2= "Empate" 

        print()
        print() 
        print("          {}".format(mensaje1))
        print("          {}".format(mensaje2))  
        print()
        print()
        print()
        
        