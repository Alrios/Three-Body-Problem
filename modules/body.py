import math
import numpy as np

class Body:
    


    """Create an celestial body (which is positioned in the sky)

    Args:
        t_orbital (float): Orbital Period of the body. With the Kepler's Law this value is known as T
        r_CoM (float): Distance from the body to the (C)enter (o)f (M)ass in meters
        mass (float) : Mass of the body in kilogramms 

    Attributes:
        t_orbital (float): Orbital Period of the body. With the Kepler's Law this value is known as T
        r_CoM (float): Distance from the body to the (C)enter (o)f (M)ass in meters
        mass (float): Mass of the body in kilogramms
    """
    def __init__(self, t_orbital, r_CoM, mass):
        self.t_orbital = t_orbital
        self.r_CoM = r_CoM
        self.mass = mass
    
    def calculatePosition(self,time):
        w = 2*math.pi /self.t_orbital
        posX = self.r_CoM*math.cos(w*time)
        posY = self.r_CoM*math.sin(w*time)
        return posX, posY

        



    






    

