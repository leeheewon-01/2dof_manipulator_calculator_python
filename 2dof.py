import math
import matplotlib.pyplot as plt
import numpy as np

def dof2(a1, a2, px, py):
    rsul2 = (2*math.atan((math.sqrt(((((a1 + a2)**2) - (px**2 + py**2))/((px**2 + py**2)-((a1 - a2)**2))))))) # calculate theta2
    if rsul2 < 0: # if theta2 is negative
        theta2 = rsul2 # set theta2 to negative
    else: # if theta2 is positive
        theta2 = -rsul2 # set theta2 to positive

    theta1 = math.atan(py/px ) - math.atan(((a2*math.sin(theta2))/(a1 + a2*math.cos(theta2)))) # calculate theta1

    print("theta1:",math.degrees(theta1),"\n"+"theta2:", math.degrees(theta2)) # print theta1 and theta2

    x1 = a1*math.cos(theta1) # calculate x1
    y1 = a1*math.sin(theta1) # calculate y1
    x2 = x1 + a2*math.cos(theta1+theta2) # calculate x2
    y2 = y1 + a2*math.sin(theta1+theta2) # calculate y2

    plt.xlim(-30, 50) # set x axis limit
    plt.ylim(-30, 50) # set y axis limit
    plt.plot([0, x1, x2], [0, y1, y2], 'ro-') # plot the arm
    print("x1 = ", x1, "\ny1 = ", y1, "\nx2 = ", x2, "\ny2 = ", y2) # print x1, y1, x2, y2
    plt.plot(px, py, 'bo') # plot the point
    plt.show() # plot
dof2(12, 4.2, 6, 6) # (a1, a2, px, py)
