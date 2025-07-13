
from Point import *

class PointRepository:

    def __init__(self,list):
        self.__points=list

    def get_points(self):
        return self.__points

    # get all points

    def set_points(self, list):
        self.__points=list

    def add_point(self,point):
        self.__points.append(point)

    # add point

    def get_point_at_index(self,index):
        try:
            if index >= 0 and index < len(self.__points):
                return self.__points[index]
            else:
                raise ValueError("Index out of range")
        except ValueError as e:
            print(f"The error is: {e}")

    # get a point at a given index

    def get_points_of_color(self,color):
        list=[]
        for point in self.__points:
            if point.get_color() == color:
                list.append(point)
        return list

    # get all points of a given color

    def get_points_inside_square(self,point,lenght):
        list=[]
        for i in self.__points:
            if i.get_coord_x()>=point.get_coord_x() and i.get_coord_x()<=point.get_coord_x()+lenght:
                if i.get_coord_y()<=point.get_coord_y() and i.get_coord_y()>=point.get_coord_y()-lenght:
                    list.append(i)
        return list

    # get all points inside a square

    def update_at_index(self,index,point):
        try:
            if index >= 0 and index < len(self.__points):
                self.__points[index] = point
            else:
                raise ValueError("Index out of range")
        except ValueError as e:
            print(f"The error is: {e}")

    # update a point at a given index

    def delete_at_index(self,index):
        try:
            if index >= 0 and index < len(self.__points):
                self.__points.remove(self.__points[index])
            else:
                raise ValueError("Index out of range")
        except ValueError as e:
            print(f"The error is: {e}")

    # delete a point at a given index

    def delete_points_inside_square(self,point,lenght):
        for i in self.__points[:]:
            if i.get_coord_x()>=point.get_coord_x() and i.get_coord_x()<=point.get_coord_x()+lenght:
                if i.get_coord_y()<=point.get_coord_y() and i.get_coord_y()>=point.get_coord_y()-lenght:
                    self.__points.remove(i)

    # delete all points inside a square

    def minimum_distance(self):
        try:
            if len(self.__points) < 2:
                raise ValueError("Need at least two points to compute distance.")
            min = float('inf')
            for i in range(len(self.__points)):
                for j in range(i + 1, len(self.__points)):
                    if self.__points[i].distance(self.__points[j]) < min:
                        min = self.__points[i].distance(self.__points[j])
            return min
        except ValueError as e:
            print(f"The error is: {e}")

    # get the minimum distance between two points

    def maximum_distance(self):
        try:
            if len(self.__points) < 2:
                raise ValueError("Need at least two points to compute distance.")
            max = -1
            for i in range(len(self.__points)):
                for j in range(i + 1, len(self.__points)):
                    if self.__points[i].distance(self.__points[j]) > max:
                        max = self.__points[i].distance(self.__points[j])
            return max
        except ValueError as e:
            print(f"The error is: {e}")

    # get the maximum distance between two points

    def shift_on_y(self):
        for i in self.__points:
            i.set_coord_x(0)

    # shift all points on the y axis

    def delete_all_points_within_distance(self,point,distance:float):
        for i in self.__points[:]:
            if i.distance(point)==distance:
                self.__points.remove(i)
    # delete all points within a certain distance
