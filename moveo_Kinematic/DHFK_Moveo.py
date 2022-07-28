#!/usr/bin/env python3
from math import cos, sin, pi
from numpy import *

# Variables
joint_1 = 0
joint_2 = 0
joint_3 = 0
joint_4 = 0
joint_5 = 0

# Joints limits adjust
joint_1 += pi/2
joint_2 += pi/2

# Base height
l0 = 0.14695

# Links lengths
l1 = 0.1655
l2 = 0.22112
l3 = 0.12762
l4 = 0.095
l5 = 0.1

# Homogeneous Transformation Matrices
A0_1 = [[cos(joint_1), 0, sin(joint_1), 0],
        [sin(joint_1), 0, -cos(joint_1), 0],
        [0, 1, 0, l1],
        [0, 0, 0, 1]]

A1_2 = [[cos(joint_2), -sin(joint_2), 0, l2*cos(joint_2)],
        [sin(joint_2), cos(joint_2), 0, l2*sin(joint_2)],
        [0, 0 ,1, 0],
        [0, 0, 0, 1]]

A2_3 = [[cos(joint_3), -sin(joint_3), 0, l3*cos(joint_3)],
        [sin(joint_3), cos(joint_3), 0, l3*sin(joint_3)],
        [0, 0 ,1, 0],
        [0, 0, 0, 1]]

A3_4 = [[1, 0, 0, l4],
        [0, cos(joint_4), -sin(joint_4), 0],
        [0, sin(joint_4), cos(joint_4), 0],
        [0, 0, 0, 1]]

A4_5 = [[cos(joint_5), -sin(joint_5), 0, l5*cos(joint_5)],
        [sin(joint_5), cos(joint_5), 0, l5*sin(joint_5)],
        [0, 0 ,1, 0],
        [0, 0, 0, 1]]

T0_2 = dot(A0_1,A1_2)
T0_3 = dot(T0_2,A2_3)
T0_4 = dot(T0_3,A3_4)
T0_5 = dot(T0_4,A4_5)

print("\n-----------------------JOINTS POSITIONS------------------------")
print("  Joint_2", end="      ")
print("Joint_3", end="      ")
print("Joint_4", end="      ")
print("Joint_5", end="      ")
print("Joint_E")

print("X = {:0.5f}".format(A0_1[0][3]), end="  ")
print("X = {:0.5f}".format(T0_2[0][3]), end="  ")
print("X = {:0.5f}".format(T0_3[0][3]), end="  ")
print("X = {:0.5f}".format(T0_4[0][3]), end="  ")
print("X = {:0.5f}\n".format(T0_5[0][3]))

print("Y = {:0.5f}".format(A0_1[1][3]), end="  ")
print("Y = {:0.5f}".format(T0_2[1][3]), end="  ")
print("Y = {:0.5f}".format(T0_3[1][3]), end="  ")
print("Y = {:0.5f}".format(T0_4[1][3]), end="  ")
print("Y = {:0.5f}\n".format(T0_5[1][3]))

print("Z = {:0.5f}".format(A0_1[2][3] + l0), end="  ")
print("Z = {:0.5f}".format(T0_2[2][3] + l0), end="  ")
print("Z = {:0.5f}".format(T0_3[2][3] + l0), end="  ")
print("Z = {:0.5f}".format(T0_4[2][3] + l0), end="  ")
print("Z = {:0.5f}\n".format(T0_5[2][3] + l0))

#print(T0_5)