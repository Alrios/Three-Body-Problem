from modules.body import Body, Vector
import numpy as np
from scipy.integrate import odeint
import pandas as pd

#Initialize variables using the Nasa Fact Sheet of the Earth and Moon
period_earth = 2360594.88 #in seconds
#period_earth = 31558118 #in seconds
mass_earth = 5.9723e+24 #in kilograms

period_moon = 2360594.88 #in seconds
mass_moon = 0.07346e+24 # in kilograms
G = 6.6726e-11 #1 N m^2 kg^−2
distance = 3.844e+8  #in meters

#Calculate the distance to the center of mass for Earth and Moon
#The size of the orbit Moon-Earth (semi major axis) is the sum of the distance to the center of mass
# Or in other words, the distance between two bodies
#  distance = dis_earth + dis_moon


# The center the mass fulfills the relation r_1*m_1 = r_2*m_2, where r is the distance and m is the mass

#For Earth

dis_earth = ( mass_moon / (mass_moon+mass_earth) )*distance
#Create object Earth
earth = Body(period_earth,dis_earth,mass_earth)

#For Moon

dis_moon = (mass_earth / (mass_moon+mass_earth) )*distance

#Create object Moon
moon = Body(period_moon,dis_moon,mass_moon)

time_max = 864000
epsilon = 100
steps = time_max / epsilon
time = np.linspace(0,time_max, int(steps) )

""""
posX_earth, posY_earth = earth.calculatePosition(time)
earthData = pd.DataFrame()
earthData.index.name = "Iterations"

earthData["x"] = posX_earth
earthData["y"] = posY_earth

posX_moon, posY_moon = moon.calculatePosition(time)
moonData = pd.DataFrame()
moonData["x"] = posX_moon
moonData["y"] = posY_moon
"""

"""
    Three body problem.
    We add a third body, this body has a initial position and velocity, but we dont know his trayectory.
    The Newtonian Force is equal to the gravitation force. The gravitational force of the new body is equal to
    the sum of the forces from the earth and moon on the new body. (The force is negativ, because is an atractive force)

    m_s*a = -G * m_s*m_e / dis_e**3 * (x_s-x_e) - G * m_s*m_moon / dis_m**3 * (x_s-x_m)
    
    The acceleration varies in time:

    a = d^2 x_s / dt^2 = -G *m_e / dis_e**3 * (x_s-x_e) - G *m_moon / dis_m**3 * (x_s-x_m) 

    We have a EDO of second order, we need to transform it to first order:

    z[0] = x_s
    z[1] = dx_s/dt
    dz[0]/dt = dx_s/dt = vx_s = z[1]

    z[2] = y_s
    z[3] = dy_s/dt
    dz[2]/dt = dy_s/dt = vy_s = z[3]

    dz[3,4]/dt = d^2 (x_s, y_s) /dt^2 = -G *m_e / dis_e**3 * (x_s-x_e) - G *m_moon / dis_m**3 * (x_s-x_m) 
"""


def deriv(z, time):
    x_sat = z[0]
    y_sat = z[2]

    x_earth,y_earth = earth.calculatePosition(time)
    x_moon,y_moon = moon.calculatePosition(time)

    d_earth = np.sqrt( (x_sat-x_earth)**2 + (y_sat-y_earth)**2 )
    d_moon = np.sqrt( (x_sat-x_moon)**2 + (y_sat-y_moon)**2 )

    dzdt = [z[1], 
          -G * (mass_earth / d_earth**3) * (x_sat-x_earth) - G *mass_moon / d_moon**3 * (x_sat-x_moon),
            z[3],
           -G * (mass_earth / d_earth**3) * (y_sat-y_earth) - G *mass_moon / d_moon**3 * (y_sat-y_moon)   ]
    return dzdt
    
 
from scipy.integrate import odeint
posX_earth, posY_earth = earth.calculatePosition(0)
z0 = [posX_earth+6800000, 0, posY_earth, np.sqrt(G*mass_earth/6800000)]
sol = odeint(deriv, z0, time)
satelData = pd.DataFrame()
x=[]
y=[]
for i in range(len(time)):
    x.append(sol[i][0])
    y.append(sol[i][2])
satelData["x"] = x
satelData["y"] = y
x_e = []
y_e = []
x_m = []
y_m = []
for t in time:
    _x, _y = earth.calculatePosition(t)
    _xm, _ym = moon.calculatePosition(t)
    x_e.append(_x)
    y_e.append(_y)

    x_m.append(_xm)
    y_m.append(_ym)

earthData = pd.DataFrame()
earthData["x"] = x_e
earthData["y"] = y_e

moonData = pd.DataFrame()
moonData["x"] = x_m
moonData["y"] = y_m
