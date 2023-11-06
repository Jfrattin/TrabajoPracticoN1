from modules.Carta import Carta
from modules.Mazo import Mazo
import random as rd
import sys

class JuegoGuerra:
    resultado_dict = { 0:"" , 1: "Ganador Jugador 1", 2: "Ganador Jugador 2" , 3: "Empate"}
    def __init__(self, random_seed):
        self.mazo_mesa = Mazo()
        self.mazo_jugador_1 = Mazo()
        self.mazo_jugador_2 = Mazo()
        self.semilla = random_seed
        self.turnos_jugados = 0
        self.resultado = 0

        r = ""
        self.empate = "empate"       

    def armar_mazo(self):
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        palos = ['♠', '♥', '♦', '♣']

        lista = []
        for valor in valores:
            for palo in palos:
                lista.append((Carta(valor, palo)))
        
        rd.seed(self.semilla)
        rd.shuffle(lista)

        for carta in lista:
            self.mazo_mesa.poner_arriba(carta)
        return self.mazo_mesa
    
    def repartir(self):
        for posicion, carta in enumerate(self.mazo_mesa):  
            
            # si el resto de posicion divido 2 es cero  agrego carta al maso del jugador uno sino al jugador 2:
            if posicion%2 == 0:                        
                self.mazo_jugador_1.poner_arriba(carta)
            else:                         
                self.mazo_jugador_2.poner_arriba(carta)   
                
        return "El mazo  se repartio completamente."

    def jugarGuerra(self,cartas_mesa : Mazo):
        #print("cartas que entraron a jugar guerra")
        #print(len(cartas_mesa))
        print("***GUERRA***")
        contador = 0
        while contador < 4 and self.mazo_jugador_1.esta_vacia() is False and self.mazo_jugador_2.esta_vacia() is False:
                cartas_mesa.poner_arriba(self.mazo_jugador_1.sacar_arriba())
                cartas_mesa.poner_arriba(self.mazo_jugador_2.sacar_arriba())
                contador += 1
        
        if contador == 4:
                carta_j2  = cartas_mesa.sacar_arriba()
                carta_j1  = cartas_mesa.sacar_arriba()
                carta_j1.darvuelta()
                carta_j2.darvuelta()
                cartas_mesa.poner_arriba(carta_j1)
                cartas_mesa.poner_arriba(carta_j2)
                for carta in cartas_mesa:
                    print(carta)
                
                # print("--carta_j1--")
                # print(carta_j1)
                # print("--carta_j2--")
                # print(carta_j2)


                if carta_j1 > carta_j2:
                    print("ganador de la guerra jugador 1")
                    for carta in cartas_mesa:
                        carta.estado=False
                        self.mazo_jugador_1.poner_abajo(carta)
                    return
                if  carta_j2 > carta_j1 :
                    print("ganador de la guerra jugador 2")
                    for carta in cartas_mesa:
                        carta.estado=False
                        self.mazo_jugador_2.poner_abajo(carta)
                    return
                elif carta_j1 == carta_j2:
                    self.jugarGuerra(cartas_mesa)

        else:
            if self.mazo_jugador_1.esta_vacia() is True and self.mazo_jugador_2.esta_vacia() is False:
                #gana el juego jugador 2, jugador 1 no podia poner mas cartas
                self.resultado = 2
                return
            if self.mazo_jugador_2.esta_vacia() is True and self.mazo_jugador_1.esta_vacia() is False:
                #gana el juego  jugador 1, jugador 2 no podia poner mas cartas
                self.resultado = 1
                return
            if self.mazo_jugador_2.esta_vacia() is True and self.mazo_jugador_1.esta_vacia() is True:
                #empateel juego  guerra ambos se quedaron sin cartas
                self.resultado = 3
                return

    def iniciar_juego(self):
        turnoslimites=10000 #Maximos 10000 mil turnos
        self.armar_mazo()
        sttr = self.repartir()
        print(sttr)
        print("-------------------------------------------------")
       
        while self.turnos_jugados < turnoslimites and self.resultado == 0 :    
                cartas_mesa = Mazo()
                print("********")
                print("Cartas Disponible del Jugador 1")
                print(len(obj.mazo_jugador_1))
                for carta in obj.mazo_jugador_1:
                        print(carta, end=" ")
                print("\nCartas Disponible del Jugador 2")
                print(len(obj.mazo_jugador_2))
                for carta in obj.mazo_jugador_2:
                        print(carta, end=" ")
                
                self.turnos_jugados += 1         
                ## agrego una carta de ambos jugadores para comparar mayor o menor
                if self.mazo_jugador_1.esta_vacia() is False and self.mazo_jugador_1.esta_vacia() is False:
                    if self.mazo_jugador_1.esta_vacia() is False:
                        carta_1 = self.mazo_jugador_1.sacar_arriba()
                        cartas_mesa.poner_arriba(carta_1)
                    else: 
                        if self.mazo_jugador_1.esta_vacia() is True and self.mazo_jugador_2.esta_vacia() is False :
                            self.resultado = 2
                            break

                    if self.mazo_jugador_2.esta_vacia() is False:
                        carta_2 = self.mazo_jugador_2.sacar_arriba() 
                        cartas_mesa.poner_arriba(carta_2)
                    else: 
                        if self.mazo_jugador_2.esta_vacia() is True and self.mazo_jugador_1.esta_vacia() is False :
                            self.resultado = 1
                            break  

                        
                        
               
                if self.mazo_jugador_1.esta_vacia() is False and self.mazo_jugador_2.esta_vacia() is False: 
                    cartamesa_j2 = cartas_mesa.sacar_arriba()
                    cartamesa_j1 = cartas_mesa.sacar_arriba()
                    
                    cartas_mesa.poner_arriba(cartamesa_j1)
                    cartas_mesa.poner_arriba(cartamesa_j2)
                    print("\n")
                    for carta in cartas_mesa:
                        #muestro las dos cartas 
                        carta.estado = True
                        print(carta, end=" ")
                        carta.estado = False
                    print("\n-------------------")
                    if cartamesa_j1 < cartamesa_j2:
                        ## si la carta del jugador 2 es menor se lleva todo jugador 1
                        self.mazo_jugador_1.poner_abajo(cartamesa_j1)
                        self.mazo_jugador_1.poner_abajo(cartamesa_j2)
                    elif cartamesa_j1 > cartamesa_j2:
                        ## si la carta del jugador 1 es menor se lleva todo jugador 2
                        self.mazo_jugador_2.poner_abajo(cartamesa_j1)
                        self.mazo_jugador_2.poner_abajo(cartamesa_j2)
                    elif cartamesa_j1 == cartamesa_j2:
                        #print("Cartas en la mesa antes de entrar en guerra ")
                        #print(len(cartas_mesa))
                        self.jugarGuerra(cartas_mesa)
                
                print ("\n Turno número:", self.turnos_jugados)       
                print("\n")
                print("\n********\n") 

        if self.turnos_jugados == turnoslimites:
            print("El juego ha terminado en empate.")
            return self.resultado_dict[3]
        else:
            return self.resultado_dict[self.resultado]


if __name__ == "__main__":
    
    obj = JuegoGuerra(random_seed= 3)
    # obj.armar_mazo() 
    # obj.repartir()
    #print(obj.mazo_jugador_1)
    # print("Los mazos empezaron asi")
    # print(len(obj.mazo_jugador_1))
    # print(len(obj.mazo_jugador_2))
    print("------------")
    print("---")
    print("Resultado del juego\n")
    print(obj.iniciar_juego())
    # print("Los mazos terminaron asi")
    # print(len(obj.mazo_jugador_1))
    # print(len(obj.mazo_jugador_2))

    