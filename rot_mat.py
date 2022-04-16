# Contents: rotation matrices wrt to each orientation
# Functions: Rx, Ry, Rz
# Author: Simran Suresh
# Date: 16.04.2022
# SRC: https://en.wikipedia.org/wiki/Rotation_matrix


import numpy as np


def Rx(ang):
    ang = np.deg2rad(ang)
    return np.array([
        [1, 0, 0],
        [0, np.cos(ang), -np.sin(ang)],
        [0, np.sin(ang), np.cos(ang)]
    ])

def Ry(ang):
    ang = np.deg2rad(ang)
    return np.array([
        [np.cos(ang), 0, np.sin(ang)],
        [0, 1, 0],
        [-np.sin(ang), 0, np.cos(ang)]
    ])

def Rz(ang):
    ang = np.deg2rad(ang)
    return np.array([
        [np.cos(ang), -np.sin(ang), 0],
        [np.sin(ang), np.cos(ang), 0],
        [0, 0, 1]
    ])
