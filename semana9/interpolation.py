import numpy as np
class Interpolation():
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def newton(self, x):
        def coeficient(x, y):
            m = len(x)

            x = np.copy(x)
            a = np.copy(y)
            for k in range(1, m):
                a[k:m] = (a[k:m] - a[k - 1])/(x[k:m] - x[k - 1])

            return a

        a = coeficient(self.x,self.y)
        n = len(self.x) - 1
        p = a[n]

        for k in range(1, n + 1):
            p = a[n - k] + (x - self.x[n - k])*p

        return p
        
    def lagrange(self, x):
        n = len(self.x)
        def basis(x, j):
            b = [(x - self.x[m]) / (self.x[j] - self.x[m])
                for m in range(n) if m != j]
            return np.prod(b, axis=0) * self.y[j]

        b = [basis(x, j) for j in range(n)]
        return np.sum(b, axis=0)

interpolation = Interpolation([0,5,10,15,20,25,30], [12.9,11.3,10.1,9.03,8.17,7.46,6.85])

print('Newton regresion: {0}, Lagrange regresion: {1}'.format(interpolation.newton(18), interpolation.lagrange(18)))