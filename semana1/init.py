#!/usr/bin/python3
import math
import constantes
import utils
import matplotlib.pyplot as plt


class CaidaLibre:
    def __init__(self, peso, resistencia):
        self.peso = peso
        self.resistencia = resistencia
        self.imprimir_datos()
        self.velocidad_anterior = [0.0]
        self.tiempo_anterior = [0.0]

    def obtener_velocidad_aproximada(self, tiempo):
        return self.velocidad_anterior[-1] + ((constantes.GRAVEDAD-((self.resistencia/self.peso) * self.velocidad_anterior[-1]))*(tiempo - self.tiempo_anterior[-1]))

    def obtener_velocidad(self, tiempo):
        return ((constantes.GRAVEDAD * self.peso)/self.resistencia)*(1-math.exp(-(self.resistencia/self.peso)*tiempo))

    def obtener_velocidad_intervalos(self, min, max=None, interval=None, velocidad=None):
        if max == None:
            max = min
            min = 0

        for tiempo in utils.frange(min, max, interval):
            self.velocidad_anterior.append(
                self.obtener_velocidad_aproximada(tiempo))
            self.tiempo_anterior.append(tiempo)
            if utils.isclose(self.obtener_velocidad_aproximada(tiempo), velocidad, rel_tol=0.001):
                return tiempo

    def obtener_tiempo_aproximado(self, velocidad):
        return self.obtener_velocidad_intervalos(min=1, max=1000, interval=0.1, velocidad=velocidad)

    def imprimir_datos(self):
        print('|  Peso   |   Resistencia |')
        print('|  {0}    |   {1}         | \n'.format(
            self.peso, self.resistencia))

    def mostrar_grafica(self):
        plt.plot(self.tiempo_anterior, self.velocidad_anterior)
        plt.show()


print('Objecto Uno')
objeto_uno = CaidaLibre(70, 12)
print('Objecto Dos')
objeto_dos = CaidaLibre(75, 15)

print('tiempo aproximado {0}'.format(objeto_dos.obtener_tiempo_aproximado(
    objeto_uno.obtener_velocidad(10))))

objeto_dos.mostrar_grafica()
