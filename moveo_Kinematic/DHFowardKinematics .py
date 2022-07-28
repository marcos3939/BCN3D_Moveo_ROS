#!/usr/bin/env python3
from math import cos, pi, sin
from pickle import LONG1
from numpy import *

# Variables
joint_1 = 0
joint_2 = 0
joint_3 = 0
joint_4 = 0
joint_5 = 0

# Base height
l0 = 0.14695

# Links lengths
l1 = 0.1655
l2 = 0.22112
l3 = 0.12762
l4 = 0.095
l5 = 0.1

# a
a1 = 0
a2 = l2
a3 = l3
a4 = l4
a5 = l5

# d
d1 = l1
d2 = 0
d3 = 0
d4 = 0
d5 = 0

# Angles (radians)
theta_1 = joint_1
theta_2 = joint_2
theta_3 = joint_3
theta_4 = 0
theta_5 = joint_5

# Alpha (radians)
alpha_1 = pi/2
alpha_2 = 0
alpha_3 = 0
alpha_4 = joint_4
alpha_5 = 0

# Alpha (radians)
#alpha_1 = (alpha_1/180)*pi
#alpha_2 = (alpha_2/180)*pi
#alpha_3 = (alpha_3/180)*pi
#alpha_4 = (alpha_4/180)*pi
#alpha_5 = (alpha_5/180)*pi

# DH Parameter Table
DH = [[theta_1, alpha_1, a1, d1],
      [theta_2, alpha_2, a2, d2],
      [theta_3, alpha_3, a3, d3],
      [theta_4, alpha_4, a4, d4],
      [theta_5, alpha_5, a5, d5]]

# Homogeneous Transformation Matrices
i = 0
A0_1 = [[cos(DH[i][0]), -sin(DH[i][0])*cos(DH[i][1]), sin(DH[i][0])*sin(DH[i][1]), DH[i][2]*cos(DH[i][0])],
        [sin(DH[i][0]), cos(DH[i][0])*cos(DH[i][1]), -cos(DH[i][0])*sin(DH[i][1]), DH[i][2]*sin(DH[i][0])],
        [0, sin(DH[i][1]), cos(DH[i][1]), DH[i][3]],
        [0, 0, 0, 1]]

i = 1
A1_2 = [[cos(DH[i][0]), -sin(DH[i][0])*cos(DH[i][1]), sin(DH[i][0])*sin(DH[i][1]), DH[i][2]*cos(DH[i][0])],
        [sin(DH[i][0]), cos(DH[i][0])*cos(DH[i][1]), -cos(DH[i][0])*sin(DH[i][1]), DH[i][2]*sin(DH[i][0])],
        [0, sin(DH[i][1]), cos(DH[i][1]), DH[i][3]],
        [0, 0, 0, 1]]

i = 2
A2_3 = [[cos(DH[i][0]), -sin(DH[i][0])*cos(DH[i][1]), sin(DH[i][0])*sin(DH[i][1]), DH[i][2]*cos(DH[i][0])],
        [sin(DH[i][0]), cos(DH[i][0])*cos(DH[i][1]), -cos(DH[i][0])*sin(DH[i][1]), DH[i][2]*sin(DH[i][0])],
        [0, sin(DH[i][1]), cos(DH[i][1]), DH[i][3]],
        [0, 0, 0, 1]]

i = 3
A3_4 = [[cos(DH[i][0]), -sin(DH[i][0])*cos(DH[i][1]), sin(DH[i][0])*sin(DH[i][1]), DH[i][2]*cos(DH[i][0])],
        [sin(DH[i][0]), cos(DH[i][0])*cos(DH[i][1]), -cos(DH[i][0])*sin(DH[i][1]), DH[i][2]*sin(DH[i][0])],
        [0, sin(DH[i][1]), cos(DH[i][1]), DH[i][3]],
        [0, 0, 0, 1]]

i = 4
A4_5 = [[cos(DH[i][0]), -sin(DH[i][0])*cos(DH[i][1]), sin(DH[i][0])*sin(DH[i][1]), DH[i][2]*cos(DH[i][0])],
        [sin(DH[i][0]), cos(DH[i][0])*cos(DH[i][1]), -cos(DH[i][0])*sin(DH[i][1]), DH[i][2]*sin(DH[i][0])],
        [0, sin(DH[i][1]), cos(DH[i][1]), DH[i][3]],
        [0, 0, 0, 1]] 

T0_2 = dot(A0_1,A1_2)
T0_3 = dot(T0_2,A2_3)
T0_4 = dot(T0_3,A3_4)
T0_5 = dot(T0_4,A4_5)


#print("A0_5 =")
#print(matrix(A0_5))
#print("X =", A0_5[0][3], "Y =", A0_5[1][3], "Z =", A0_5[2][3])

print("\nJoint_2 position")
print("X = {:0.5f}".format(A0_1[0][3]), end=" ")
print("Y = {:0.5f}".format(A0_1[1][3]), end=" ")
print("Z = {:0.5f}\n".format(A0_1[2][3] + l0))
print("Joint_3 position")
print("X = {:0.5f}".format(T0_2[0][3]), end=" ")
print("Y = {:0.5f}".format(T0_2[1][3]), end=" ")
print("Z = {:0.5f}\n".format(T0_2[2][3] + l0))
print("Joint_4 position")
print("X = {:0.5f}".format(T0_3[0][3]), end=" ")
print("Y = {:0.5f}".format(T0_3[1][3]), end=" ")
print("Z = {:0.5f}\n".format(T0_3[2][3] + l0))
print("Joint_5 position")
print("X = {:0.5f}".format(T0_4[0][3]), end=" ")
print("Y = {:0.5f}".format(T0_4[1][3]), end=" ")
print("Z = {:0.5f}\n".format(T0_4[2][3] + l0))
print("Joint_6 position")
print("X = {:0.5f}".format(T0_5[0][3]), end=" ")
print("Y = {:0.5f}".format(T0_5[1][3]), end=" ")
print("Z = {:0.5f}\n".format(T0_5[2][3] + l0))