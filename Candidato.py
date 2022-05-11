class Candidato:
    def __init__(self, nome, numero, cargo, votos, partido):
        self.nome = nome
        self.numero = numero
        self.cargo = cargo
        self.votos = votos
        self.partido = partido

    def toString(self):
      print(self.nome, self.numero, self.cargo, self.votos, self.partido)

    def getNome(self):
      return self.nome

    def setNome(self, nome):
      self.nome = nome

    def getNumero(self):
        return self.numero

    def setNumero(self, numero):
      self.numero = numero

    def getCargo(self):
          return self.cargo

    def setCargo(self, cargo):
      self.cargo = cargo

    def getVotos(self):
          return self.votos

    def setVotos(self, votos):
      self.votos = votos

    def getPartido(self):
          return self.partido

    def setPartido(self, partido):
      self.partido = partido