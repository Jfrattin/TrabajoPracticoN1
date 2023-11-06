class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
    
class ListaDobleEnlazada:
    
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
    
    def __len__(self):
        return self.tamanio
    
    def esta_vacia(self):
        return self.tamanio == 0
    
    def tamanio(self):
        return self.tamanio

    def agregar_al_inicio(self, item):
        nuevo_nodo = Nodo(item)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
            if self.cabeza.anterior != None:
                self.cabeza.anterior = None
        self.tamanio += 1

    def agregar_al_final(self, item):
        nuevo_nodo = Nodo(item)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
            if self.cabeza.anterior != None:
                self.cabeza.anterior = None
        self.tamanio += 1

    def insertar(self, item, posicion=None):
        nuevo_nodo = Nodo(item)
    
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        elif posicion is None or posicion >= self.tamanio:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        elif posicion == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            for _ in range(posicion - 1):
                nodo_actual = nodo_actual.siguiente
    
            nuevo_nodo.siguiente = nodo_actual.siguiente
            nuevo_nodo.anterior = nodo_actual
            nodo_actual.siguiente.anterior = nuevo_nodo
            nodo_actual.siguiente = nuevo_nodo
      
        self.tamanio += 1

    def extraer(self,posicion = None):
        if self.tamanio == 0:
            raise RuntimeError("Lista vacía")
        elif posicion == None and self.tamanio == 1 or posicion == 0 and self.tamanio == 1:
            dato = self.cabeza.dato
            self.cabeza = self.cola = None
            self.tamanio = 0
        elif posicion == 0 and self.tamanio > 1:
            dato = self.cabeza.dato
            nodo_segundo = self.cabeza.siguiente
            nodo_segundo.anterior = None
            self.cabeza = nodo_segundo
            self.tamanio -= 1
        elif (posicion == None or posicion == self.tamanio-1 or posicion == -1) and self.tamanio > 1:
            dato = self.cola.dato
            nodo_ante_ultimo = self.cola.anterior
            nodo_ante_ultimo.siguiente = None
            self.cola = nodo_ante_ultimo
            self.tamanio -= 1
        else:
            nodo_extraer = self.cabeza
            for _ in range(posicion):
                nodo_extraer = nodo_extraer.siguiente
            dato = nodo_extraer.dato

            nodo_extraer.anterior.siguiente = nodo_extraer.siguiente
            nodo_extraer.siguiente.anterior = nodo_extraer.anterior
            self.tamanio -= 1

        return dato

    def copiar(self):
        listacopia = ListaDobleEnlazada()
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            listacopia.agregar_al_final(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return listacopia

    def invertir(self):
        
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            siguiente_nodo = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_actual.anterior
            nodo_actual.anterior = siguiente_nodo
            nodo_actual = siguiente_nodo
        
        self.cabeza, self.cola = self.cola, self.cabeza
        return self

    def ordenar(self):
        # Si solo tiene un elemento o no tiene elementos, no es necesario ordenar.
        if self.tamanio <= 1:
            return self

        # Usamos un marcador para determinar si se realizaron intercambios en una pasada
        intercambio_realizado = True

        # Realizamos el bucle de ordenación hasta que no haya más intercambios
        while intercambio_realizado:
            intercambio_realizado = False
            nodo_actual = self.cabeza

            while nodo_actual.siguiente is not None:
                nodo_siguiente = nodo_actual.siguiente

                if nodo_actual.dato > nodo_siguiente.dato:
                    # Intercambiamos los datos de los nodos
                    nodo_actual.dato, nodo_siguiente.dato = nodo_siguiente.dato, nodo_actual.dato
                    intercambio_realizado = True  # Marcamos que se realizó un intercambio

                nodo_actual = nodo_siguiente  # Avanzamos al siguiente nodo

        return self

    def concatenar(self, lista):
        temp = lista.cabeza

        for i in range(lista.tamanio):
            self.agregar_al_final(temp.dato)
            temp = temp.siguiente 
        return self

    def __add__(self,lista):
        lista_retorno = self.copiar()
        return lista_retorno.concatenar(lista)
    
    def __iter__(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
            
    def __str__(self):
        return str([nodo for nodo in self])
    

if __name__ == "__main__":
    # Creo un objeto lista uno del tipo ListaDobleEnlazada
    listauno = ListaDobleEnlazada()
    
    listauno.agregar_al_inicio(1)
    listauno.agregar_al_inicio(9)
    listauno.agregar_al_inicio(4)
    listauno.agregar_al_final(-8)
    listauno.agregar_al_final(-100)
    ##lista1
    listauno.insertar(2,7)
    print("Imprimo lista uno")
    print(listauno)
    
    listados = ListaDobleEnlazada()
    listados.agregar_al_inicio(67)
    listados.agregar_al_inicio(7)
    listados.agregar_al_inicio(55)
    listados.agregar_al_final(-99)
    listados.agregar_al_final(-1)
    print("Imprimo lista dos")
    print(listados)
    print("Imprimo lista dos ordenada")
    listados = listados.ordenar()
    print(listados)
    listaconcat= listauno.concatenar(listados)
    print("Imprimo lista uno y dos concatenadas")
    print(listaconcat)
    print("Imprimo lista uno y dos concatenadas pero ordenada de menor a mayor")
    listaconcat= listaconcat.ordenar()
    print(listaconcat)
    print("Imprimo lista uno y dos concatenadas pero invertida")
    listaconcat = listaconcat.invertir()
    print(listaconcat)