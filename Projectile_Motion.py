#! /usr/bin/python3

import math
import turtle
import csv
import os
import time
import sys

#args = sys.argsv

simulationvars = ["t_resolution","accuracy"]
settingvars = ["u","density","C","r","start_angle","start_height","m","g_acceleration"]
datavars = ["t","s","v","angle","v_vertical","v_horizontal","s_vertical","s_horizontal","air_resistance","air_resistance_vertical","air_resistance_horizontal","acceleration_vertical","acceleration_horizontal"]# The varibles which will be monitored

date_time = [time.strftime("%Y"),time.strftime("%m"),time.strftime("%d"),time.strftime("%H"),time.strftime("%M"),time.strftime("%S")]# Gets the time
datetime = "_".join(date_time[:3])+"_"+":".join(date_time[3:])
print(datetime)

t_resolution = 0.01# The frequency with which the motion is calculated
accuracy = 3# The number of decimal places that float values are rounded to
maxcount = 2000# The number of instances before the simulation automatically stops

sin = lambda x:round(math.sin(math.radians(x)),accuracy)# Setting up a shortcut for trig and square root functions
cos = lambda x:round(math.cos(math.radians(x)),accuracy)
tan = lambda x:round(math.tan(math.radians(x)),accuracy)
asin = lambda x:round(math.degrees(math.asin(x)),accuracy)
acos = lambda x:round(math.degrees(math.acos(x)),accuracy)
atan = lambda x:round(math.degrees(math.atan(x)),accuracy)
sqroot = lambda x:round(math.sqrt(x),accuracy)


u = 150.00# Initial velocity
density = 1.225# Density of fluid
C = 1.47# Drag coefficient
r = 0.0213# Radius of ball
start_angle = 45.00# Angle of launch
start_height = 1.00# Vertical start height
m = 2.000# Mass of the ball
g_acceleration = -9.8# Acceleration caused by gravity


g = g_acceleration*m# Force of gravity
A = math.pi*(r**2)# Area of ball
k = (1/2)*A*C*density# Drag constant

s = start_height# Vertical displacement from origin
t = 0# Time
v = u# Velocity
angle = start_angle# Direction of motion
v_vertical = sin(angle)*v# Vertical velocity
v_horizontal = cos(angle)*v# Horizontal velocity
s_vertical = 0.00# Vertical displacement from start point
s_horizontal = 0.00# Horizontal displacement from start point
air_resistance = "-"# Force of air resistance
air_resistance_vertical = "-"# Vertical force of air resistance
air_resistance_horizontal = "-"# Horizontal air resistance
acceleration_vertical = "-"# Vertical acceleration
acceleration_horizontal = "-"# Horizontal acceleration

screen = turtle.Screen()# Gets the dimensions of the screen
size = screen.screensize()
print(size)

turtle.up()# Moving the turtle to the start point
turtle.goto((-0.95)*size[0],(-1)*size[1]+s)
turtle.seth(angle)
turtle.down()


file_ = open("./Data/"+datetime+".dat","w")# Writes the headers to the data file
f = csv.writer(file_,delimiter="\t")
for i in [simulationvars,settingvars]:
    for x in i:
        f.writerow([x+" "*(40-len(x))+"- "+str(globals()[x])])
    f.writerow([])
f.writerow(datavars)
f = csv.DictWriter(file_,delimiter="\t",fieldnames=datavars)

count = 0

while s >= 0 and count <= maxcount:
    line = {}
    for i in datavars:# Prints all the variables
        print(i+" "*(40-len(i))+"- "+str(globals()[i]))
        line[i] = globals()[i]
    print()
    f.writerow(line)# Writes the variables to a data file

    turtle.seth(angle)# Moves the turtle
    turtle.forward(v*t_resolution)

    v_vertical = sin(angle)*v# Resolves the velocity
    v_horizontal = cos(angle)*v

    s_vertical += v_vertical*t_resolution# Calculates the new displacement
    s_horizontal += v_horizontal*t_resolution
    s += v_vertical*t_resolution

    air_resistance = (-1)*k*(v**2)# Calculates the force of air resistance
    air_resistance_vertical = air_resistance*sin(angle)
    air_resistance_horizontal = air_resistance*cos(angle)

    acceleration_vertical = (air_resistance_vertical+g)/m# Calculates the new acceleration in each direction
    acceleration_horizontal = (air_resistance_horizontal)/m

    v_horizontal += acceleration_horizontal*t_resolution# Calculates the new velocity in each direction
    v_vertical += acceleration_vertical*t_resolution

    v = sqroot(v_horizontal**2+v_vertical**2)# Combines the two velocities

    try:# Calculates the angle, while avoiding an error if the object is moving vertically
        angle = atan(v_vertical/v_horizontal)
    except ZeroDivisionError:
        if v_vertical >= 0:
            angle = 90
        else:
            angle = -90

    t += t_resolution# Increments the time

    for i in datavars:
        globals()[i] = round(globals()[i],accuracy)

    count += 1# Increments a count value to prevent an infinite loop
    print(count)
    print()

line = {}
for i in datavars:# Prints all the variables
    print(i+" "*(40-len(i))+"- "+str(globals()[i]))
    line[i] = globals()[i]
print()
f.writerow(line)# Writes the variables to a data file

file_.close()
input()
