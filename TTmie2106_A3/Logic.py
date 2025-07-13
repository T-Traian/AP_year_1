
from PointRepository import *
list_color=['red','blue','green','yellow','orange','purple']

import matplotlib.pyplot as plt

def show_meniu():
    print()
    print("Select an option:")
    print("1.Enter a list of points to the repository:")
    print("2.Add a point to the repository:")
    print("3.Get all points:")
    print("4.Get a point at a given index:")
    print("5.Get all points of a given color:")
    print("6.Get all points that are inside a given square:")
    print("7.Get the minimum distance between two points:")
    print("8.Update a point at a given index:")
    print("9.Delete a point by index:")
    print("10.Delete all points that are inside a given square:")
    print("11.Get the maximum distance between two points:")
    print("12.Shift all points on the y axis:")
    print("13.Delete all points within a certain distance from a given point:")
    print("14.Plot all points in a chart:")
    choice=input()
    return choice

def read_point():
    print()
    x=int(input("Enter the x coordinate:"))
    y=int(input("Enter the y coordinate:"))
    color=input("Enter the color:")
    try:
        if x >= 0:
            if y >= 0:
                if color in list_color:
                    po = MyPoint(x, y, color)
                    return po
        else:
            raise ValueError("Invalid point.")
    except ValueError as e:
        print(f"The error is {e}")

def read_list(n):
    list=[]
    for i in range(n):
        po=read_point()
        if po!=None:
            list.append(po)
    return list


def read_index():
    print()
    try:
        x = int(input("Enter the desired index:"))
        if x>=0:
            return x
        else:
            raise ValueError("Invalid index.")
    except ValueError as e:
        print(f"The error is {e}")

def read_color():
    print()
    try:
        x=input("Enter the desired color:")
        if x in list_color:
            return x
        else:
            raise ValueError("Invalid color.")
    except ValueError as e:
        print(f"The error is {e}")

def read_lenght():
    print()
    try:
        x = int(input("Enter the desired length:"))
        if x>=0:
            return x
        else:
            raise ValueError("Invalid lenght.")
    except ValueError as e:
        print(f"The error is {e}")

def read_distance():
    print()
    try:
        x = float(input("Enter the desired distance:"))
        if x<0:
            raise ValueError("Please enter a positive value.")
        else:
            return x
    except ValueError as e:
        print(f"The error is {e}")

def plot_points(PointRep):
    x_list=[]
    y_list=[]
    color_list=[]
    # we put the x,y and color of all the points in 3 lists and plot them with scatter
    for point in PointRep.get_points():
        x_list.append(point.get_coord_x())
        y_list.append(point.get_coord_y())
        color_list.append(point.get_color())
    plt.scatter(x_list, y_list, color=color_list)
    plt.show()
