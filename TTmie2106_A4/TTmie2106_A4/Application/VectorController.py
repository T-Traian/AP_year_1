from Infrastructure.VectorRepository import VectorRepository
from Domain.MyVector import MyVector

class VectorRepositoryController:

    def __init__(self,repo):
        self.__repo=VectorRepository(repo)

    def get_vectors_repo(self):
        return self.__repo.get_vectors()    #get all the vectors in the repository

    def set_vectors_repo(self,vector_list):
        self.__repo.set_vectors(vector_list)    #set the repository to a list

    def add_vector_repo(self,vector):
        self.__repo.add_vector(vector)      #add a vector

    def get_vector_at_index_repo(self,index):
        return self.__repo.get_vector_at_index(index)       #get a vector at an index

    def update_vector_at_index_repo(self,index,vector):
        self.__repo.update_vector_at_index(index,vector)        #update a vector at an index

    def update_vector_by_nameID_repo(self,name_id,vector):
        self.__repo.update_vector_at_name_id(name_id,vector)

    def delete_vector_at_index_repo(self,index):
        self.__repo.delete_vector_at_index(index)           #delete a vector at an index

    def delete_vector_by_nameID_repo(self,nameID):
        self.__repo.delete_vector_by_name_id(nameID)            #delete a vector by nameID

    def plot_all_vectors_repo(self):
        self.__repo.plot_all_vectors()

    def vector_with_given_sum_repo(self,sum):
        vector_list=[]
        vector_list=self.__repo.vectors_with_given_sum(sum)         #the list of vectors which have the given sum
        return vector_list

    def delete_vectors_between_two_indexes_repo(self,index1,index2):
        self.__repo.delete_vectors_between_indexes(index1,index2)

    def update_by_adding_scalar_repo(self,scalar):
        self.__repo.update_by_adding_a_scalar(scalar)