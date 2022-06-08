class Node:
    def __init__(self, numero = None):
        self.numero = numero
        self.previo = self
        self.siguiente = self

class lista:
    def __init__(self):
        self.inicio = None
        self.contador = 0
     
    def __repr__(self):
        texto = ""
          
        if(self.inicio == None):
            texto += "Lista vacia"
            return texto
          
        texto += f"Lista circular doblemente enlazada:\n{self.inicio.numero}"      
        temp = self.inicio.siguiente
        while(temp != self.inicio):
            texto += f"  {temp.numero}"
            temp = temp.siguiente
        return texto
    
    def agregar(self, data):
        self.insertar(data, self.contador)
        return
     
     
    def insertar(self, numero, indice):
        if (indice > self.contador) | (indice < 0):
            raise ValueError(f"Indice fuera de rango: {indice}, size: {self.contador}")
         
        if self.inicio == None:
            self.inicio = Node(numero)
            self.contador = 1
            return
         
        temp = self.inicio
        if(indice == 0):
            temp = temp.previo
        else:
            for _ in range(indice - 1):
                temp = temp.siguiente
         
        temp.siguiente.previo = Node(numero)
        temp.siguiente.previo.siguiente, temp.siguiente.previo.previo = temp.siguiente, temp
        temp.siguiente = temp.siguiente.previo
        if(indice == 0):
            self.inicio = self.inicio.previo
        self.contador += 1
        return
     
         
    def indice(self, numero):
        temp = self.inicio
        for i in range(self.contador):
            if(temp.numero == numero):
                return i
            temp = temp.siguiente
        return None
     
    def conseguir(self, indice):
        if (indice >= self.contador) | (indice < 0):
            raise ValueError(f"indice out of range: {indice}, size: {self.contador}")
             
        temp = self.inicio
        for _ in range(indice):
            temp = temp.siguiente
        return temp.numero

    def buscar(self,numero_buscado):
        pivote=self.inicio
        while(pivote!=None):
            if (pivote.numero==numero_buscado):
                print("Previo: ", pivote.previo.numero)
                print("Actual: ", pivote.numero)
                print("Siguiente: ", pivote.siguiente.numero)

            if (pivote.siguiente==self.inicio):
                return
            pivote=pivote.siguiente
     
     
    def imprimir(self):
        print(self)