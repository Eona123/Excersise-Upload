#Aufgabe	1:	Magische	Methoden
#Implementieren	Sie	eine	Klasse	Vector3,	welche	einen	3D	Vektor	repräsentiert.
#Dabei	sollen	Magische	Methoden	implementiert	werden:
#• Konversion	zu	Zeichenkette
#• Addition
#• Subtraktion
#• komponentenweise	Multiplikation (Vector3	*	Vector3)
#• Multiplikation	mit	Skalar	
#(float	*	Vector3)	oder	(int	*	Vector3)	oder
#(Vector3	*	float)	oder	(Vector3	*	int)

class Vector3:
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self._x = x
        self._y = y
        self._z = z
    
    def setX(self, x):
        self._x = x

    def getX(self):
        return self._x
    
    def setY(self, y):
        self._y = y

    def getY(self):
        return self._y
    
    def setZ(self, z):
        self._z = z

    def getZ(self):
        return self._z
    
    XX = property(getX, setX)        #abkürzung um an die seter und getter zu gelangen
    y = property(getY, setY)
    z = property(getZ, setZ)

    def __str__(self):
        return f"x: {self.XX} y: {self.y} z: {self.z}"
    
    def __add__(self, addVector):
        return Vector3(self.XX + addVector.XX, self.y + addVector.y, self.z + addVector.z)    #hiermit wird mit addVector definiert, dass die Vektoren addiert werden müssen. Ohne dass würde es nicht verstehen, wie die Vektoren zusammen gerechnet werden können, da es nicht einfache "normale" Zahlen sind

    def __mul__(self, multiplicator):
        return Vector3(self.XX * multiplicator.XX, self.y * multiplicator.y, self.z * multiplicator.z)
        
    def __sub__(self, subVector):
        return Vector3(self.XX - subVector.XX, self.y - subVector.y, self.z - subVector.z)  
    
    def __iadd__(self, addVector):
        return self.__add__(addVector)      #damit eine ganze return funktion nicht doppelt geschreiben werden muss, kann hiermit auf eine frühere funktion zurückgegriffen werden

    def __invert__(self):
        return self * -1
    
    def dot (self, skal):
        return self.XX * skal.XX + self.y * skal.y + self.z * skal.z
    
    def cross (self, cro):
        return Vector3(self.y * cro.z - self.z * cro.y, self.z * cro.XX - self.XX * cro.z, self.XX * cro.y - self.y * cro.XX)
    
    def normalize (self, norm):
        w = (self.XX**2 + self.y**2 + self.z**2)**0.5
        return Vector3(self.XX / w, self.y / w, self.z / w)
    
a = Vector3(3,4,2)
b = Vector3(2,1,0)
c = a * b # Komponentenweise Multiplikation
d = a.dot(b)
print(d)
e = a.cross(b)
print(e)
f = a.normalize(b)
print(f)
#d = a.dot(b) # Skalarprodukt