from modules.Tad import ListaDobleEnlazada
from modules.Carta import Carta

class Mazo:
    def __init__(self):
        self.mazo = ListaDobleEnlazada() 
       
    def __str__(self):
        return str(self.mazo)
    
    def __repr__(self):
        return repr(self.mazo)
    
    def __iter__(self):
        return iter(self.mazo)
    
    def esta_vacia(self):
        return self.mazo.esta_vacia()
    
    def poner_arriba(self, Carta): 
        #este metodo agrega las cartas al mazo principal
        self.mazo.agregar_al_inicio(Carta)
            
    def sacar_arriba(self):
        #extraer una carta del dorso
        return self.mazo.extraer(0)
    
    def dar_vuelta(self):
        for i in self:
            i.carta.estado= True #pone todas las cartas boca abajo
    
    def __len__(self):
         return self.mazo.__len__()
    
    def poner_abajo(self, Carta): #pone abajo del mazo las cartas ganadas
         Carta.estado = False
         self.mazo.agregar_al_final(Carta)
         