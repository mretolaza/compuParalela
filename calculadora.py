import math 

class WS: 

    # constructor 

    def __init__(self): 
        self.n = 0  
        self.p = 0 
        self.secuencial = 0
        self.tiempoSerial = 0 

    
    def tiempoSerial( self, n, p): 
        result  = n/p + math.log2(p) 
        return result 

    def calculateOneSequence(self, p): 
        for x in range (10, 320, 10): 
            print(self.tiemposerial(x,p))

    

    