import numpy as np
import matplotlib.pyplot as plt

class Regression:
    def __init__(self,x,y, degree):
        self.x = x
        self.y = y
        self.degree = degree

    def polynomial(self, xi):
        poly_fit = np.poly1d(np.polyfit(self.x,self.y, self.degree))

        return poly_fit(18)


regression = Regression([0,5,10,15,20,25,30], [12.9,11.3,10.1,9.03,8.17,7.46,6.85], 3)

print('Regresión Polinomial {0}'.format(regression.polynomial(18)))