class Vertice():
    def __init__(self,dato):
        self.dato=dato
        self.ListaSalientes=[]
        self.ListaEntrantes=[]

    def getDato(self):
        return self.dato

    def setDato(self,dato):
        self.dato=dato

    def getListaSalientes(self):
        return self.ListaSalientes

    def setListaSalientes(self, dato):
        self.ListaSalientes.remove(dato)

    def setListaEntrantes(self, dato):
        self.ListaEntrantes.remove(dato)

    def getListaEntrantes(self):
        return self.ListaEntrantes

    def gradoentrada(self):
        return len(self.ListaEntrantes)

    def gradosalida(self):
        return len(self.ListaSalientes)