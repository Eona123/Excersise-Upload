class WGS84Coord:
    def __init__(self,longitude=0,latitude=0):
        self.setLongitude(longitude)
        self.setLatidude(latitude)

    def setLongitude (self, value):
        if value < -180:
            self._longitude = ((value + 180)%360)-180
        elif value > 180:
            self._longitude = ((value + 180)%360)-180
        
    def getLongitude (self):
        return self._longitude

    def setLatidude (self,value):
        if value < -90:
            self._latitude = ((value-90)%90)-90
        elif value > 90:
            self._latitude = ((value-90)%90)-90
    
    def getLatidude (self):
        return self._latitude
    
    def ausgabe(self):
        print(self._longitude)
        print(self._latitude)

w0=WGS84Coord(-200,180)
w0.ausgabe()