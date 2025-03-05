class Vector3:
    def __init__ (self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def len(self):
        return ((self.x)**2+(self.y)**2+(self.z)**2)**0.5
    
    def ausgabe(self):
        print(f"der Vektor ist so lang: {self.laenge()}")


v0=Vector3(3,4,5)
v0.ausgabe()