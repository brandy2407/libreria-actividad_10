#from particula import Particula 

class Administrar:
    def __init__(self):
        self.administrar = []

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.administrar
        )
    def agregar_inicio(self,particula):
        self.administrar.insert(0,particula)

    def agregar_final(self,particula):
        self.administrar.append(particula)

    def mostrar(self):
        for particula in self.administrar:
         print(particula)
    
