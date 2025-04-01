#Uebung 3: Objektorientierung III
#Aufgabe 1: Vererbung
#Schreiben Sie die Klassen "Dreieck", "Rechteck", "Kreis" und "Polygon"
#Diese Klassen werden von folgender Python Klasse vererbt:

#Das Attribut "name" ist eine Zeichenkette welche den Namen des jeweiligen
#Objektes enthält.
#• Die Methode "Umfang" soll für die jeweilige Figur korrekt implementiert werden
#• Finden Sie geeignete Konstruktoren um die Figuren zu konstruieren
#• __str__ soll die Figur mit allen Koordinaten sinnvoll beschreiben, z.B:
#o "Kreis M=(2.3,4.2) r=3.4"
#o "Rechteck (0,0) – (10,15)"
#Hinweise:
#• Die Figuren sind 2D
#• Verwenden Sie eine Klasse Punkt („Point“) um die Koordinaten der Figuren zu verwalten.
#• Die Seiten bei Rechteck sind parallel zur jeweiligen Koordinaten-Achse.
#• Wählen Sie geeignete Konstruktoren, z.B. bei Polygon sollen beliebig viele Ecken unterstützt werden.

import math


class Figur:
    def __init__(self, name):
        self.name = name

    def Umfang(self):
        return 0
    
    def __str__(self):
        return self.name

class Point(Figur):
    def __init__(self, x, y):
        super().__init__(self, x, y)
        self.x = []
        self.y = []
    
    def koordDruck(self):
        return f"Die Figur hat die Koordinaten: {self.x, self.y}"


class Plane(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def PlaneScope(self):
        width = abs(self.x[0] - self.y[0])
        length = abs(self.y2 - self.y1)
        pScope = 2*width+2*length
        return f"Das Viereck hat einen Umfang von {pScope}"
    
class Triangle(Point):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__(x1, y1, x2, y2, x3, y3)

    def TriangleScope(self):
        side1 = math.sqrt((self.x1-self.x2)**2+(self.y1-self.y2)**2)
        return f"die erste seite ist {side1} lang"

class Circle(Point):
    def __init__(self,x1, y1, r):
        super().__init__(x1, y1)
        self.r =r
    def CircleScope(self):
        return 2*self.r*math.pi
       
class Polygone(Figur):
    def __init__(self):
        super().__init__("Polygone")


t = Triangle(1,2,3,4,1,1)
#print(t.TriangleScope())
p = Plane(2,2,1,1)
print(p.PlaneScope())
print(p.koordDruck())
c = Circle(2,2,1)
#print(c.CircleScope())