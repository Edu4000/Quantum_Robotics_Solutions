# Path Planning
# By: Eduardo Angeles

from inspect import _void
from typing import List 

import turtle as rover # For semantic use
import random as rand
import numpy as np
import math

def get_interest_points (target_vect:np.array, interest_point_list:List[np.array]) -> _void:
    interest_point_num = rand.randint(5,10)

    for i in range(interest_point_num):
        interest_point_list.append(
            np.array([
                target_vect[0] + rand.randint(-100, 100),    # x-coordinate
                target_vect[1] + rand.randint(-100, 100)     # y-coordinate
            ])
        )


def module (vect:np.array):
    return math.sqrt(vect.dot(vect))


def move_to_next_point(origin_vect:np.array, target_vect:np.array, step:int = 1) -> _void:
    direction_vect = target_vect - origin_vect

    # Setting the direction of movement or turning angle
    turning_angle = rover.heading()

    if (direction_vect[1] == 0):    # Special cases

        if (direction_vect[0] > 0):
            turning_angle = 0 - turning_angle   # Change direction to the right
        else:
            turning_angle = 0 - turning_angle   # Change direction to the left

    elif (direction_vect[0] >= 0 and direction_vect[1] > 0):    # First quadrant

        turning_angle = math.atan(direction_vect[1] / direction_vect[0]) - turning_angle

    elif (direction_vect[1] > 0):  # Second quadrant

        turning_angle = math.atan(direction_vect[1] / direction_vect[0]) - turning_angle + math.pi

    elif (direction_vect[0] >= 0):  # Fourth quadrant

        turning_angle = math.atan(direction_vect[1] / direction_vect[0]) - turning_angle + 2 * math.pi

    else: # Third quadrant

        turning_angle = math.atan(direction_vect[1] / direction_vect[0]) - turning_angle + math.pi

    # Rotating to correct direction
    if (turning_angle > 0):
        rover.left(turning_angle)
    else:
        rover.right(abs(turning_angle))
        
    
    # Moving towards the target
    for d in range(0, int(module(direction_vect)), step):
        print("Position: ", rover.pos())
        rover.forward(step)
    
    print("Position: ", rover.pos())
    rover.forward(module(direction_vect) - int(module(direction_vect)))
    print("Reached Goal Position: ", rover.pos())
    rover.dot(5)

# Adding the nearest point to the path list
def path_finder(target_list:List[np.array], origin_vect:np.array, current_path:List[np.array]) -> _void:

    if (len(target_list) == 1):
        current_path.append(target_list.pop(0))
        return

    smallest_distance = math.inf
    bestindex = 0

    for i in range(len(target_list)):
        if smallest_distance > distance_from_a_to_b(origin_vect, target_list[i]):
            smallest_distance = distance_from_a_to_b(origin_vect, target_list[i])
            bestindex = i

    current_path.append(target_list.pop(bestindex))
    path_finder(target_list, current_path[len(current_path)-1], current_path)


def distance_from_a_to_b (vect_start:np.array, vect_end:np.array) -> float:
    distance_vect = vect_start - vect_end
    return module(distance_vect)

def get_optimized_path(target_list:List[np.array], origin_vect:np.array) -> List[np.array]:

    current_path = [origin_vect]
    path_finder(target_list, origin_vect, current_path)
    return current_path

def solution_geometric():
    print("<----- Path Planning ----->")

    origin_vect = np.array([0, 0])

    # Initializing approximate coordinates as a 2D vector
    target_vect = np.array([
        rand.randint(-300, 300),    # x-coordinate
        rand.randint(-300, 300)     # y-coordinate
    ])

    # From target we create random interest points in a radius of n meters
    interest_point_list:List[np.array] = []
    get_interest_points(target_vect, interest_point_list)

    # Moving from starting point to approximate coordinates
    rover.begin_fill(); rover.speed(1); rover.radians(); rover.dot(5)

    move_to_next_point(origin_vect, target_vect)

    best_path = get_optimized_path(interest_point_list, np.array(rover.pos()))

    # Moving to the interest points
    for i in range(len(best_path) - 2):
        move_to_next_point(best_path[i], best_path[i + 1])

    for i in range (100):
        rover.left(0.1)


if __name__ == "__main__":
    solution_geometric()