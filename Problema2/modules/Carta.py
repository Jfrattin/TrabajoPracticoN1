class Carta:
    # creo un diccionario para las cartas
    valores_cartas = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,'K': 13, 'A': 14}

    # Constructor carta  defino false como boca abajo y true boca arriba
    def __init__(self, valor, palo, estado=False):
        self.valor = valor
        self.palo = palo
        self.estado = estado
        
    def __str__(self):
        if self.estado == False :
            return "-X"    #pregunta si la carta está boca abajo, no la muestra, caso contrario muestra el palo y el valor 
        else:
            return str(self.valor)+ str(self.palo)
        
    def __repr__(self):
        if self.estado == False:
            return "-X"    #pregunta si la carta está boca abajo, no la muestra, caso contrario muestra el palo y el valor 
        else:
            return str(self.valor) + str(self.palo)
     ## Remplazo metodo carta
    
    def __eq__(self, otro):
        return self.valores_cartas[self.valor] == self.valores_cartas[otro.valor]
    
    ## Remplazo metodo carta mayor
    def __gt__(self, otro):
        return self.valores_cartas[self.valor] > self.valores_cartas[otro.valor]
    ## Remplazo metodo carta mayor
    def __lt__(self, otro):
        return self.valores_cartas[self.valor] < self.valores_cartas[otro.valor]

    def valor(self):
        return self.valor
    
    def palo(self):
        return self.palo
    
    def estado(self):
        return self.estado
    
    def darvuelta(self):
        self.estado = not self.estado
        return
