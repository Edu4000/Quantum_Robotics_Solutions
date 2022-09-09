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
    rover.left(turning_angle)
    
    # Moving towards the target
    for d in range(0, int(module(direction_vect)), step):
        print("Position: ", rover.pos())
        rover.forward(step)
    
    print("Position: ", rover.pos())
    rover.forward(module(direction_vect) - int(module(direction_vect)))
    print("Reached Goal Position: ", rover.pos())
    rover.dot(5)


def path_finder(target_list:List[np.array], origin_vect:np.array, current_path:List[np.array], posible_paths:List[List[np.array]]) -> _void:

    if (len(target_list) == 1):
        current_path.append(target_list[0])
        posible_paths.append(current_path.copy())
        current_path.pop()

    for i in range(len(target_list)):

        current_path.append(target_list.pop(i))

        path_finder(target_list, origin_vect, current_path, posible_paths)

        target_list.insert(i, current_path.pop())


def path_length (current_path:List[np.array]) -> float:

    distance = 0

    for i in range(len(current_path) - 2):
        distance_vect = current_path[i] - current_path[i+1]
        distance += module(distance_vect)

    return distance


def get_optimized_path(target_list:List[np.array], origin_vect:np.array) -> List[np.array]:

    posible_paths = []
    current_path = [origin_vect]
    path_finder(target_list, origin_vect, current_path, posible_paths)

    optimized_distance = math.inf
    optimized_path = []

    for path in posible_paths:
        if (path_length(path) < optimized_distance):
            optimized_distance = path_length(path)
            optimized_path = path

    return optimized_path


if __name__ == "__main__":
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

    while True:
        rover.left(0.1)