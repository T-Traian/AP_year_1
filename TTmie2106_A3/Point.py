import math

list_color=['red','blue','green','yellow','orange','purple']

class MyPoint:
    def __init__(self, coord_x=0,coord_y=0,color='red'):
        try:
            if isinstance(coord_x,(int,float)) and coord_x>=0:
                self.__x=coord_x
            else:
                self.__x=0
                raise ValueError("Invalid coordinate for x.")
        except ValueError as e:
            print(f"The error is: {e}")

        try:
            if isinstance(coord_y,(int,float)) and coord_y>=0:
                self.__y=coord_y
            else:
                self.__y=0
                raise ValueError("Invalid coordinate for y.")
        except ValueError as e:
            print(f"The error is: {e}")

        try:
            if color in list_color:
                self.__color=color
            else:
                raise ValueError("Invalid color.")
        except ValueError as e:
            print(f"The error is: {e}")

    def __str__(self):
        return f"Point ({self.get_coord_x()},{self.get_coord_y()}) of color {self.get_color()}"

    def get_coord_x(self):
        return self.__x

    def get_coord_y(self):
        return self.__y

    def get_color(self):
        return self.__color

    def set_coord_x(self,x):
        try:
            if isinstance(x,(int,float)) and x>=0:
                self.__x=x
            else:
                raise ValueError("Invalid coordinate for x.")
        except ValueError as e:
            print(f"The error is: {e}")

    def set_coord_y(self,y):
        try:
            if isinstance(y,(int,float)) and y>=0:
                self.__y=y
            else:
                raise ValueError("Invalid coordinate for y.")
        except ValueError as e:
            print(f"The error is: {e}")

    def set_color(self,color):
        try:
            if color in list_color:
                self.__color=color
            else:
                raise ValueError("Invalid color.")
        except ValueError as e:
            print(f"The error is: {e}")

    def distance(self,other):
         return math.sqrt((other.get_coord_x()-self.get_coord_x())**2+(other.get_coord_y()-self.get_coord_y())**2)


