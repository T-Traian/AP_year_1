from Domain.MyVector import *
import matplotlib.pyplot as plt

class VectorRepository:
    def __init__(self,vector_list):
        if isinstance(vector_list, list):
            self.__vectors = vector_list
        else:
            self.__vectors = []

    def get_vectors(self):
        return self.__vectors

    def set_vectors(self,vector_list):
        self.__vectors=vector_list[:]

    def add_vector(self,vector):
        self.__vectors.append(vector)

    def get_vector_at_index(self,index):
        try:
            if isinstance(index,int):
                if index>=0 and index<len(self.get_vectors()):
                    return self.__vectors[index]
                else:
                    raise IndexError('Index out of range')
            else:
                raise Exception('The index must be an integer')
        except (TypeError,Exception) as e:
            print (f"The error is: {e}")

    def update_vector_at_index(self,index,vector):
        try:
            if isinstance(index,int):
                if index>=0 and index<len(self.get_vectors()):
                    self.__vectors[index]=vector
                else:
                    raise IndexError('Index out of range')
            else:
                raise Exception('The index must be an integer')
        except (TypeError,Exception) as e:
            print (f"The error is: {e}")

    def update_vector_at_name_id(self,name_id,vector):
        try:
            if isinstance(name_id, (int, str)):
                for value in range(len(self.get_vectors())):
                    if self.get_vectors()[value].get_name_id() == name_id:
                        self.get_vectors()[value]=vector
            else:
                raise TypeError("Name_id should be a int or a string.")
        except TypeError as k:
            print(f"The error is: {k}")

    def delete_vector_at_index(self,index):
        try:
            if isinstance(index,int):
                if index>=0 and index<len(self.get_vectors()):
                    self.get_vectors().pop(index)
                else:
                    raise IndexError('Index out of range')
            else:
                raise Exception('The index must be an integer')
        except (TypeError,Exception) as e:
            print (f"The error is: {e}")

    def delete_vector_by_name_id(self,name_id):
        try:
            if isinstance(name_id, (int, str)):
                new_list=[]
                for value in range(len(self.get_vectors())):
                    if self.get_vectors()[value].get_name_id() != name_id:
                        new_list.append(self.get_vectors()[value])
                self.set_vectors(new_list)
            else:
                raise TypeError("Name_id should be a int or a string.")
        except TypeError as k:
            print(f"The error is: {k}")

    def plot_all_vectors(self):
        list = self.get_vectors()
        for i in range(len(list)):
            x_list = []
            nr = len(list[i].get_values())
            while nr != 0:
                x_list.append(i)
                nr -= 1
            if list[i].get_type()==1:
                type='o'
            else:
                if list[i].get_type()==2:
                    type='s'
                else:
                    if list[i].get_type()==3:
                        type='^'
                    else:
                        if list[i].get_type()>4:
                            type='D'
            plt.plot(x_list,list[i].get_values(),color=list[i].get_colour(),marker=type)
        plt.show()

    def vectors_with_given_sum(self,sum):
        vector_list=[]
        for vector in self.get_vectors():
            if vector.sum_of_elements()==sum:
                vector_list.append(vector)
        return vector_list

    def delete_vectors_between_indexes(self,index1,index2):
        try:
            vector_list = self.get_vectors()
            new_vector_list=[]
            if index1>=0 and index1<len(vector_list):
                if index2>=0 and index2<len(vector_list):
                    for vector in range(len(vector_list)):
                        if index1>vector or index2<vector:
                            new_vector_list.append(vector_list[vector])
                else:
                    raise IndexError('Index out of range')
            else:
                raise IndexError('Index out of range')
        except IndexError as k:
            print(f"The error is: {k}")
        self.set_vectors(new_vector_list)

    def update_by_adding_a_scalar(self,scalar):
        for vector in self.get_vectors():
            vector.add_scalar(scalar)


