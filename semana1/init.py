import math
import constantes
import utils


class CaidaLibre:
    def __init__(self, peso, resistencia):
        self.peso = peso
        self.resistencia = resistencia
        self.imprimir_datos()

    def obtener_velocidad(self, tiempo):
        return ((constantes.GRAVEDAD * self.peso)/self.resistencia)*(1-math.exp(-(self.resistencia/self.peso)*tiempo))

    def obtener_velocidad_intervalos(self, min, max=None, interval=None, velocidad=None):
        if max == None:
            max = min
            min = 0

        for tiempo in utils.frange(min, max, interval):
            if utils.isclose(self.obtener_velocidad(tiempo), velocidad, rel_tol=0.001):
                return tiempo

    def obtener_tiempo_aproximado(self, velocidad):
        return self.obtener_velocidad_intervalos(min=1, max=1000, interval=0.1, velocidad=velocidad)

    def imprimir_datos(self):
        print('|  Peso   |   Resistencia |')
        print('|  {0}    |   {1}         | \n'.format(self.peso,self.resistencia))

print('Objecto Uno')
objeto_uno = CaidaLibre(70, 12)
print('Objecto Dos')
objeto_dos = CaidaLibre(75, 15)

print(objeto_dos.obtener_tiempo_aproximado(
    objeto_uno.obtener_velocidad(10)))
