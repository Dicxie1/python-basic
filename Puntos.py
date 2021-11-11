import cmath
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getx(self):
        return  self.x

    def setx(self, x):
        self.x = x

    def gety(self):
        return self.y

    def sety(self, y):
        self.y = y


p1 = Punto(2, 1)
p2 = Punto(1, 5)
distantia = cmath.sqrt((p1.x - p2.x)**2 +(p1.y - p2.y)**2 )
print("la distancia entre los dos puntos es %s" %(distantia))