from collections import deque
from modelos.Planeta import *
from modelos.Arista import *
from copy import copy


class Grafo():

    def __init__(self):
        self.pozos = 0
        self.fuentes = 0
        self.ListaVertices = []
        self.ListaAristas = []
        self.ListaVisitados = []

    #1.B
    def ingresarvertice(self, dato):
        if self.obtenervertice(dato) == None:
            self.ListaVertices.append(Vertice(dato))

    def obtenervertice(self, dato):
        for vertice in self.ListaVertices:
            if vertice.getDato() == dato:
                return vertice
        return None

    def obtenerarista(self, origen, destino):
        for Arista in self.ListaAristas:
            if Arista.getOrigen() == origen and Arista.getDestino() == destino:
                return Arista
        return None

    #1.C
    def ingresararista(self, origen, destino, peso, dirigido):
        if self.verificararista(origen, destino) == None: # Verifica si ya existe
            if self.obtenervertice(origen) != None and self.obtenervertice(destino) != None:# Si existe el origen y el destino...

                self.ListaAristas.append(Arista(origen, destino, peso, dirigido)) #Agrega arista a su lista
                if(dirigido==True):
                    self.obtenervertice(origen).getListaSalientes().append(destino) #Agrega adyacencia al origen
                    self.obtenervertice(destino).getListaEntrantes().append(origen)#Agrega hacia qué es ady. el origen
                else: # Sino, lo hace doble dir.
                    self.obtenervertice(origen).getListaSalientes().append(destino)
                    self.obtenervertice(destino).getListaEntrantes().append(origen)
                    self.obtenervertice(destino).getListaSalientes().append(destino)
                    self.obtenervertice(origen).getListaEntrantes().append(origen)



    def verificararista(self, origen, destino):
        for Arista in self.ListaAristas:
            if Arista.getOrigen() == origen and Arista.getDestino() == destino:
                return Arista #Si  existe la retorna
        return None

    #1.D
    def esConexo(self): #Si hay planeta aislado no es conexo
        cont=0
        for p in self.ListaVertices:
            if p.gradoentrada()==0 and p.gradosalida()==0:
                cont=cont+1
        if cont<1:
            return True
        else:
            return False
        ##------------------------------##

    #1.E
    def Pozo(self):
        lista=[]
        for planeta in self.ListaVertices:
            if planeta.gradosalida()==0:
                lista.append(planeta)

        return lista

    def mostrarArista(self):
        for i in range(len(self.ListaAristas)):
            print("-------------------------------")
            print("Origen: ", self.ListaAristas[i].getOrigen())
            print("Destino: ", self.ListaAristas[i].getDestino())
            print("Peso: ", self.ListaAristas[i].getPeso())
            print("-------------------------------")

    def obstruirCamino(self, origen, destino):
        for Camino in self.ListaAristas:
            if (Camino.getOrigen() == origen and Camino.getDestino() == destino) or (
                    Camino.getOrigen() == destino and Camino.getDestino() == origen):
                if (Camino.getObstruido() == False):
                    Camino.setObstruido(True)
                    return Camino
        return None

    # Guarda aristas obstruidas y retorna lista
    def caminoObstruido(self):
        listado = []
        for camino in self.ListaAristas:
            if camino.getObstruido() == True:
                listado.append(camino)
        return listado

    def obtenerPlanetas(self):
        listado = []
        for planeta in self.ListaVertices:
            listado.append(planeta)
        return listado

    ''' def cambiarSentido(self, origen, destino):
            self.mostrarArista()
            #copia == self.ListaAristas
            for aux  in range(len(self.ListaAristas)):
                if self.ListaAristas[aux].getOrigen() == origen and self.ListaAristas[aux].getDestino() == destino:
                    if self.ListaAristas[aux].getDirigido == False:
                        self.ListaAristas[aux].setOrigen(destino)
                        self.ListaAristas[aux].setDestino(origen)
                        self.ListaAristas[aux].setDirigido()
                        self.obtenervertice(origen).setListaSalientes(destino)
                        self.obtenervertice(destino).setListaEntrantes(origen)
                        self.obtenervertice(origen).getListaEntrantes().append(destino)
                        self.obtenervertice(destino).getListaSalientes().append(origen)
                        print("------")
                    else:
        
                        print("Hola")
        
                        self.ListaAristas[aux].setOrigen(destino)
                        self.ListaAristas[aux].setDestino(origen)
                        self.mostrarArista()
                        self.obtenervertice(origen).setListaSalientes(destino)
                        self.obtenervertice(destino).setListaEntrantes(origen)
                        self.obtenervertice(origen).getListaEntrantes().append(destino)
                        self.obtenervertice(destino).getListaSalientes().append(origen)
                    return self.ListaAristas[aux]
                    ##############################
            def Prim(self):
            CopiaAristas = copy(self.ListaAristas)  # copia de las aristas
            Conjunto = []
            AristaPrim = []  # creo una lista con las aristas
            AristasTemp = []  # Todas las adyacencias
    
            self.Dobles(CopiaAristas)
    
            self.ordenamiento(CopiaAristas)  # ordeno las aristas
            # self.Repetidas(CopiaAristas)#elimino los caminos dobles, ya que no nos interesan las dobles conexiones
    
            menor = CopiaAristas[0]
            Conjunto.append(menor.getOrigen())
            pos = True
            while (pos):  # nuevo
                for Vertice in Conjunto:
                    self.Algoritmo(CopiaAristas, AristaPrim, Conjunto, Vertice, AristasTemp, pos)
                if len(Conjunto) == len(self.ListaVertices):  # nuevo
                    pos = False  # nuevo
            print("los vertices visitados fueron: {0} ".format(Conjunto))
    
            for dato in AristasTemp:
                print("temporal | Origen: {0} -----> destino: {1} peso: {2}".format(dato.getOrigen(), dato.getDestino(),
                                                                                    dato.getPeso()))
    
            for dato in AristaPrim:
                print(
                    "Origen: {0} -----> destino: {1} peso: {2}".format(dato.getOrigen(), dato.getDestino(), dato.getPeso()))
    
        def Algoritmo(self, CopiaAristas, AristaPrim, Conjunto, Vertice, AristasTemp, pos):
            ciclo = False
            # lo debo buscar en la lista de arista en ambas direcciones
            self.AgregarAristasTemp(CopiaAristas, Vertice, Conjunto, AristasTemp)
            menor = self.BuscarmenorTemp(AristasTemp, AristaPrim,
                                         CopiaAristas)  # obtengo la arista menor de los nodos que he visitado
            if menor != None:
                if menor.getOrigen() in Conjunto and menor.getDestino() in Conjunto:  # es porque cierra un ciclo
                    ciclo = True
    
                if ciclo == False:  # si es falso es porq puede ingresar
                    if not menor.getDestino() in Conjunto:
                        Conjunto.append(menor.getDestino())
                    AristaPrim.append(menor)
    
        def AgregarAristasTemp(self, CopiaAristas, Vertice, Conjunto, AristasTemp):
            for Aristas in CopiaAristas:
                if Vertice == Aristas.getOrigen():
                    if self.verificarTemp(Aristas, AristasTemp):  # si no esta
                        AristasTemp.append(Aristas)  # Agrego todas las aristas
    
        def BuscarmenorTemp(self, AristasTemp, AristaPrim, CopiaAristas):
            menor = CopiaAristas[len(CopiaAristas) - 1]  # el mayor como esta ordenado, es el ultimo
            for i in range(len(AristasTemp)):
                if AristasTemp[i].getPeso() <= menor.getPeso():
                    if self.BuscarPrim(AristaPrim, AristasTemp[i]) == False:
                        menor = AristasTemp[i]
    
            AristasTemp.pop(AristasTemp.index(menor))
            return menor
    
        def BuscarPrim(self, AristaPrim, menor):
            for Aristap in AristaPrim:
                if Aristap.getOrigen() == menor.getOrigen() and Aristap.getDestino() == menor.getDestino():
                    return True
                if Aristap.getOrigen() == menor.getDestino() and Aristap.getDestino() == menor.getOrigen():
                    return True
    
            return False
    
        def verificarTemp(self, Aristan, AristasTemp):
            for Arista in AristasTemp:
                if Arista.getOrigen() == Aristan.getOrigen() and Arista.getDestino() == Aristan.getDestino():
                    return False
    
            return True
            
            #Elimina los repetidos porque en prim no toma en cuenta las direcciones del grafo, por consiguiente con un enlace es mas que suficiente'''


    def Repetidas(self, CopiaAristas):
        for elemento in CopiaAristas:
            for i in range(len(CopiaAristas)):
                if elemento.getOrigen() == CopiaAristas[i].getDestino() and elemento.getDestino() == CopiaAristas[
                    i].getOrigen():
                    CopiaAristas.pop(i)  # elimino
                    break

    '''def Dobles(self, CopiaAristas):
        doble = False
        for elemento in CopiaAristas:
            for i in range(len(CopiaAristas)):
                if elemento.getOrigen() == CopiaAristas[i].getDestino() and elemento.getDestino() == CopiaAristas[
                    i].getOrigen():
                    doble = True
            if doble == False:
                CopiaAristas.append(Arista(elemento.getDestino(), elemento.getOrigen(), elemento.getPeso()))
            doble = False'''

    def verificarvertice(self, dato):
        for vertice in self.ListaVertices:
            if vertice.getDato() == dato:
                return True
        return False

    def ordenamiento(self, CopiaAristas):  # Ordeno de menor a mayor
        for i in range(len(CopiaAristas)):
            for j in range(len(CopiaAristas)):
                if CopiaAristas[i].getPeso() < CopiaAristas[j].getPeso():
                    temp = CopiaAristas[i]
                    CopiaAristas[i] = CopiaAristas[j]
                    CopiaAristas[j] = temp

