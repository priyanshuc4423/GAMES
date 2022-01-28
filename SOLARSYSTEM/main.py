from ursina import *
import numpy as np

def update():
    global t
    t =t+0.02
    angle = np.pi * 40 /180
    radius_1 = 1
    mercury.x = np.cos(t)*radius_1
    mercury.z = np.sin(t)*radius_1

    radius_2 = 1.4
    venus.x = np.cos(t+angle)*radius_2
    venus.z = np.sin(t+angle)*radius_2

    radius_3 = 1.8
    earth.x = np.cos(t+angle*2)*radius_3
    earth.z = np.sin(t+angle*2)*radius_3

    radius_4 = 2.2
    mars.x = np.cos(t+angle*3)*radius_4
    mars.z = np.sin(t+angle*3)*radius_4

    radius_5 = 2.6
    jupiter.x = np.cos(t+angle*4)*radius_5
    jupiter.z = np.sin(t+angle*4)*radius_5

    radius_6 = 3
    saturn.x = np.cos(t+angle*5)*radius_6
    saturn.z = np.sin(t+angle*5)*radius_6

    radius_7 = 3.4
    uranus.x = np.cos(t+angle*6)*radius_7
    uranus.z = np.sin(t+angle*6)*radius_7

    radius_8 = 3.8
    neputne.x = np.cos(t)*radius_8
    neputne.z = np.sin(t)*radius_8


app = Ursina()
sun = Entity(model='sphere',color = color.yellow,scale = 1.5)
mercury = Entity(model='sphere',color = color.gray,scale = .2)
venus = Entity(model='sphere',color = color.orange,scale = .3)
earth = Entity(model='sphere',color = color.blue,scale = .4)
mars = Entity(model='sphere',color = color.violet,scale = .3)
jupiter = Entity(model='sphere',color = color.red,scale = .8)
saturn = Entity(model='sphere',color = color.white,scale = .5)
uranus = Entity(model='sphere',color = color.cyan,scale = .5)
neputne = Entity(model='sphere',color = color.gold,scale =.55)
t = -np.pi


app.run()