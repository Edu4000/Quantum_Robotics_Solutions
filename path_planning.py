from math import atan, radians, sqrt
import math
import random as rand
import turtle as rover
import numpy as np
from tokenize import Double

print ("Path Planning Solution")

class Rover:
    def __init__(self, vel) -> None:
        self.x_cord = 0      # Coordenadas en m
        self.y_cord = 0      # Coordenadas en m
        self.rotation = 0    # Angulo en rads
        self.vel = vel       # Velocidad de movimiento

class Solution:
    # Class variables
    x_ArUco:Double
    y_ArUco:Double
    rotation:Double
    vel:Double

    def __init__(self, x_ArUco, y_ArUco) -> None:
        self.x_ArUco = x_ArUco      # Coordenadas en m
        self.y_ArUco = y_ArUco      # Coordenadas en m
        self.rotation = 0           # Angulo en rads
        self.vel = 1                # Velocidad de movimiento
        rover.speed(1)
        rover.radians()
        rover.dot(20)

    def redirect(self):
        # We can use trigonometry to find θ
        # *----*
        # |   /
        # |  /
        # |θ/
        # |/
        # *
        ca = rover.pos()[0] - self.x_ArUco
        co = rover.pos()[1] - self.y_ArUco

        dist = sqrt(pow((rover.pos()[0] - self.x_ArUco), 2) + pow((rover.pos()[1] - self.y_ArUco), 2))

        theta =  atan(co/ca)

        print(rover.heading())

        # Checando cuadrantes del circulo unitario
        if (ca > 0 and co > 0):     # 1er Cuadrante
            rover.left(theta)
        elif (ca < 0 and co < 0):   # 3er Cuadrante
            rover.left(-theta - math.pi/2)
        elif (ca < 0):              # 2do Cuadrante
            rover.left(-theta - math.pi/2)
        elif (co < 0):              # 4to Cuadrante
            rover.left(-theta - math.pi)
        
        
        print(rover.heading())

        rover.forward(dist)

    def run(self):
        self.redirect()
        print(rover.pos())

rover.begin_fill()

def direction (vect_origin, vect_goal) -> np.array:
    return vect_goal - vect_origin
        
def redirect (vect_direction):
    orientation = rover.heading()

    # Checking quadrant in unitary circle
    x = vect_direction[0]
    y = vect_direction[1]

    # Lokking for new direction
    if (y == 0):
        if (x > 0):
            turn = 0 - rover.heading()
        else:
            turn = math.pi - rover.heading()

    elif (x > 0 and y > 0): # First quadrant
        turn = atan(x/y)
    elif (y > 0): # Second quadrant
        turn = math.pi + atan(x/y)
    elif (x > 0): # Fourth quadrant
        turn = math.pi*2 + atan(x/y)
    else: # Third quadrant
        turn = math.pi + atan(x/y)

    turn -= orientation

    print("Orientation: ", orientation)
    print("Turning: ", turn)
    rover.left(turn)

def advance (vect_direction):
    rover.forward(sqrt(vect_direction.dot(vect_direction)))

def fill_interest_points(vect_goal:np.array, vect_interest_pts):
    num_interest = rand.randint(5,7)

    for i in range(num_interest):
        new_point = np.array([
            vect_goal[0] + rand.randint(-50, 50),   # x
            vect_goal[1] + rand.randint(-50, 50)    # y
        ])

        vect_interest_pts.append(new_point)


if __name__ == "__main__":
    rover.speed(2)
    print("Hello World!")
    # Randomly initializing x and y goal approximations
    x_ArUco = rand.randint(-200,200)
    y_ArUco = rand.randint(-200,200)

    print(atan(0/3))
    print(math.pi + atan(-1/3))
    print(math.pi + atan(-1/-3))
    print(math.pi*2 + atan(1/-3))



    vect_origin = np.array([1,0])
    vect_goal = np.array([x_ArUco, y_ArUco])
    print(vect_goal)

    vect_interest_pts = []

    fill_interest_points(vect_goal, vect_interest_pts)
    print(vect_interest_pts)

    redirect(vect_goal)
    advance(vect_goal)

    while True:
        rover.left(0.1)