class Arista():
    def __init__(self, Origen, Destino, Peso, dirigido=False, obstruido=False):
        self.Origen=Origen
        self.Destino=Destino
        self.Peso=Peso
        self.Dirigido=dirigido
        self.Obstruido=obstruido

    def getOrigen(self):
        return self.Origen

    def getDestino(self):
        return self.Destino

    def getPeso(self):
        return self.Peso
    def setObstruido(self, obs):
        self.Obstruido=obs
    def setOrigen(self, origen):
        self.Origen=origen
    def setDestino(self, destino):
        self.Destino=destino
    def setDirigido(self):
        if self.Dirigido == True:
            self.Dirigido = False
        else:
            self.Dirigido = True
    def getDirigido(self):
        return self.Dirigido
    def getObstruido(self):
        return self.Obstruido