from modules.body import Body
import numpy as np
from scipy.integrate import odeint
import pandas as pd

#Initialize variables using the Nasa Fact Sheet of the Earth and Moon
period_earth = 2360594.88 #in seconds
mass_earth = 5.9723e+24 #in kilograms

period_moon = 2360594.88 #in seconds
mass_moon = 0.07346e+24 # in kilograms
G = 6.6726e-11 #1 N m^2 kg^−2
distance = 3.844e+8  #in meters


# Calculate the distance from the Moon and Earth to the barycenter (center of mass)

#For Earth
dis_earth = ( mass_moon / (mass_moon+mass_earth) )*distance

#For Moon
dis_moon = (mass_earth / (mass_moon+mass_earth) )*distance


#Create a object body with properties Orbital Period, Distance to Barycenter and Mass

#Create object Earth
earth = Body(period_earth,dis_earth,mass_earth)

#Create object Moon
moon = Body(period_moon,dis_moon,mass_moon)

#Create an array for time
time_max = 864000
epsilon = 100
steps = time_max / epsilon
time = np.linspace(0,time_max, int(steps) )

"""
    Function with the ODE using the Three body problem.
    See README for better understanding.
    
    x_s : position of the satellite in x
    y_s : position of the satellite in y
    vx_s: velocity of the satellite in x
    vy_s: velocity of the satellite in y

    z : new variable

    z[0] = x_s
    z[1] = vx_s
    z[2] = y_s
    z[3] = vy_s
    
    dz[0]/dt = dx_s/dt = vx_s = z[1]
    dz[1]/dt = d^2 x_s/dt^2 = -G *m_e / dis_e**3 * (x_s-x_e) - G *m_moon / dis_m**3 * (x_s-x_m) 
    dz[2]/dt = dy_s/dt = vy_s = z[3]
    dz[3]/dt = d^2 (y_s) /dt^2 = -G *m_earth / dis_e**3 * (y_s-y_earth) - G *m_moon / dis_m**3 * (y_s-y_moon) 
    
"""


def deriv(z, time):
    x_sat = z[0]
    y_sat = z[2]

    x_earth,y_earth = earth.calculatePosition(time)
    x_moon,y_moon = moon.calculatePosition(time)

    #Distance from the Satellite to Earth and Moon
    d_earth = np.sqrt( (x_sat-x_earth)**2 + (y_sat-y_earth)**2 )
    d_moon = np.sqrt( (x_sat-x_moon)**2 + (y_sat-y_moon)**2 )

    dzdt = [z[1], 
          -G * (mass_earth / d_earth**3) * (x_sat-x_earth) - G *mass_moon / d_moon**3 * (x_sat-x_moon),
            z[3],
           -G * (mass_earth / d_earth**3) * (y_sat-y_earth) - G *mass_moon / d_moon**3 * (y_sat-y_moon)   ]
    return dzdt
    
 #Import module to solve the ODE

from scipy.integrate import odeint

#Calculate the position of the Earth and Moon at time 0
posX_earth, posY_earth = earth.calculatePosition(0)

#Create array with the initials conditions of the satellite
# Position in X, Velocity in X, Position in Y, Velocity in Y

#First set of initial conditions where the velocity is smaller than the escape velocity of the Earth
z0 = [posX_earth+6800000, 0, posY_earth, np.sqrt(G*mass_earth/6800000)]
#Second set of initial conditions where the velocity is greater than the escape velocity of the Earth
z0_1 = [posX_earth+6800000, 0, posY_earth, 11186]

#Function to solve the ODE
sol_1 = odeint(deriv, z0, time)
sol_2 = odeint(deriv, z0_1, time)

#Save the results in a Data Frame using pandas
satelData_1 = pd.DataFrame()
satelData_2 = pd.DataFrame()

x_1=[] 
y_1=[]
x_2=[] 
y_2=[]
for i in range(len(time)):
    x_1.append(sol_1[i][0])
    y_1.append(sol_1[i][2])
    x_2.append(sol_2[i][0])
    y_2.append(sol_2[i][2])
satelData_1["x"] = x_1
satelData_1["y"] = y_1
satelData_2["x"] = x_2
satelData_2["y"] = y_2

#Save position of the Earth and Moon using pandas
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
