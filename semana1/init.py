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
        self.velocidad_anterior_real = [0.0]

    def obtener_velocidad_aproximada(self, tiempo):
        return self.velocidad_anterior[-1] + ((constantes.GRAVEDAD-((self.resistencia/self.peso) * self.velocidad_anterior[-1]))*(tiempo - self.tiempo_anterior[-1]))

    def obtener_velocidad(self, tiempo):
        return ((constantes.GRAVEDAD * self.peso)/self.resistencia)*(1-math.exp(-(self.resistencia/self.peso)*tiempo))

    def obtener_resultado(self, min, max=None, interval=None, velocidad=None):
        if max == None:
            max = min
            min = 0

        tiempo_aproximado = None
        tiempo_real = None

        for tiempo in utils.frange(min, max, interval):
            self.velocidad_anterior.append(
                self.obtener_velocidad_aproximada(tiempo))
            self.velocidad_anterior_real.append(self.obtener_velocidad(tiempo))
            self.tiempo_anterior.append(tiempo)

            if utils.isclose(self.obtener_velocidad_aproximada(tiempo), velocidad, rel_tol=0.001) and tiempo_aproximado is None:
                tiempo_aproximado = tiempo

            if utils.isclose(self.obtener_velocidad(tiempo), velocidad, rel_tol=0.001) and tiempo_real is None:
                tiempo_real = tiempo

            if tiempo_real is not None and tiempo_aproximado is not None:
                return [tiempo_aproximado, tiempo_real]

    def obtener_tiempo_aproximado(self, velocidad):
        return self.obtener_resultado(min=1, max=20, interval=0.1, velocidad=velocidad)

    def imprimir_datos(self):
        print('|  Peso   |   Resistencia |')
        print('|  {0}    |   {1}         | \n'.format(
            self.peso, self.resistencia))

    def mostrar_grafica(self):
        fig, ax = plt.subplots()
        ax.plot(self.tiempo_anterior, self.velocidad_anterior, color='red')
        ax.set_xlabel("Tiempo")
        ax.set_ylabel("Velocidad Aproximada (roja)")
        ax2 = ax.twinx()
        ax2.plot(self.tiempo_anterior,
                 self.velocidad_anterior_real, color='blue')
        ax2.set_ylabel("Velocidad Real (azul)")
        plt.show()


print('Objecto Uno')
objeto_uno = CaidaLibre(70, 12)
print('Objecto Dos')
objeto_dos = CaidaLibre(75, 15)


print('tiempo aproximado {0}\ntiempo real {1}'.format(*objeto_dos.obtener_tiempo_aproximado(
    objeto_uno.obtener_velocidad(10))))

objeto_dos.mostrar_grafica()
