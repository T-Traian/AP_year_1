import numpy as np

colour_list=['r','g','b','y','m']

class MyVector:
    def __init__(self,name_id,colour,type,values):
        try:
            #name_id should be a string or an integer
            if isinstance(name_id, (int, str)):
                self.__name_id = name_id
            else:
                self.__name_id = 0
                raise TypeError("Name_id should be a int or a string.")
        except TypeError as k:
            print(f"The error is: {k}")

        try:
            #colour must be from the accepted list
            if colour in colour_list:
                self.__colour = colour
            else:
                self.__colour = 'r'
                raise ValueError("Invalid colour.")
        except ValueError as k:
            print(f"The error is: {k}")

        try:
            if isinstance(type, (int)) and type >= 1:
                self.__type = type
            else:
                self.__type = 1
                raise ValueError("Type should be an integer.")
        except TypeError as k:
            print(f"The error is: {k}")

        try:
            #we consider the vector values to be strictly positive
            if len(values)>0:
                ok = True
                for i in values:
                    if not isinstance(i, (int)):
                        ok = False
                if ok == True:
                    self.__value = values
                else:
                    self.__value=[1]
                    raise TypeError("Please enter a list of integers.")
            else:
                self.__value = [1]
                raise Error("Please enter a list of elements.")
        except (TypeError,Error) as k:
            print(f"The error is: {k}")

    def __str__(self):
        return f"Vector name/id: {self.__name_id}, Vector colour: {self.__colour}, Vector type: {self.__type}, Vector values: {self.__value}"

    def __eq__(self, other):
        #check to see if two vectors are equal
        if self.get_name_id()!=other.get_name_id():
            return False
        if self.get_colour()!=other.get_colour():
            return False
        if self.get_type()!=other.get_type():
            return False
        if self.get_values()!=other.get_values():
            return False
        return True

    def get_name_id(self):
            return self.__name_id

    def get_colour(self):
        return self.__colour

    def get_type(self):
        return self.__type

    def get_values(self):
        return self.__value

    def set_name_id(self,name_id):
        try:
            if isinstance(name_id, (int, str)):
                self.__name_id = name_id
            else:
                self.__name_id = 0
                raise TypeError("Name_id should be a int or a string.")
        except TypeError as k:
            print(f"The error is: {k}")

    def set_colour(self,colour):
        try:
            if colour in colour_list:
                self.__colour = colour
            else:
                self.__colour = 'r'
                raise InvalidValue("Invalid colour.")
        except InvalidValue as k:
            print(f"The error is: {k}")

    def set_type(self,type):
        try:
            if isinstance(type, (int)) and type >= 1:
                self.__type = type
            else:
                self.__type = 1
                raise ValueError("Type should be an integer.")
        except TypeError as k:
            print(f"The error is: {k}")

    def set_values(self,values):
        try:
            if len(values) > 0:
                ok = True
                for i in values:
                    if not isinstance(i, (int)):
                        ok = False
                if ok == True:
                    self.__value = values
                else:
                    self.__value = [1]
                    raise TypeError("Please enter a list of integers.")
            else:
                self.__value = [1]
                raise TypeError("Please enter a list of elements.")
        except TypeError as k:
            print(f"The error is: {k}")

    def add_scalar(self,scalar):
        try:
            if isinstance(scalar, (int)):
                vector_list=np.array(self.get_values())
                self.set_values((vector_list+scalar).tolist())
            else:
                raise TypeError("Scalar should be an integer.")
        except TypeError as k:
            print(f"The error is: {k}")

    def add_vectors(self,vector):
        try:
            if len(self.get_values())==len(vector.get_values()):
                first_vector=np.array(self.get_values())
                second_vector=np.array(vector.get_values())
                self.set_values((first_vector+second_vector).tolist())
            else:
                raise TypeError("The vectors should have the same dimension.")
        except TypeError as k:
            print(f"The error is: {k}")

    def subtract_vecotrs(self,vector):
        try:
            if len(self.get_values())==len(vector.get_values()):
                first_vector=np.array(self.get_values())
                second_vector=np.array(vector.get_values())
                self.set_values((first_vector-second_vector).tolist())
            else:
                raise TypeError("The vectors should have the same dimension.")
        except TypeError as k:
            print(f"The error is: {k}")

    def multiply_vectors(self,vector):
        product=0
        try:
            if len(self.get_values())==len(vector.get_values()):
                first_vector=np.array(self.get_values())
                second_vector=np.array(vector.get_values())
                prod_list=first_vector*second_vector
                return np.sum(prod_list)
            else:
                raise TypeError("The vectors should have the same dimension.")
        except TypeError as k:
            print(f"The error is: {k}")

    def sum_of_elements(self):
        list=np.array(self.get_values())
        return np.sum(list)

    def product_of_elements(self):
        list=np.array(self.get_values())
        return np.prod(list)

    def avg_of_elements(self):
        sum_list=np.array(self.get_values())
        return np.average(sum_list)

    def min_of_elements(self):
        list=np.array(self.get_values())
        return np.min(list)

    def max_of_elements(self):
        list=np.array(self.get_values())
        return np.max(list)

