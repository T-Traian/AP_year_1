from Domain.MyVector import MyVector
from Infrastructure.VectorRepository import VectorRepository

class VectorUI:
    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def show_meniu():
        print()
        print("1.Add a vector to the repository:")
        print("2.Get all vectors and print them:")
        print("3.Get a vector at a given index:")
        print("4.Update a vector at a given index:")
        print("5.Update a vector identified by name_id:")
        print("6.Delete a vector by index:")
        print("7.Delete a vector by name_id:")
        print("8.Plot all vectors in a chart based on the type and colour of each vector:")
        print("9.Get the list of vectors having a given sum of elements:")
        print("10.Delete all vectors that are between two given indexes:")
        print("11.Update all vectors by adding a given scalar to each element:")
        print("12.Exit.")

    @staticmethod
    def read_vector():
        try:
            values = []
            name_id = input("Enter the name/id of the vector: ")
            colour = input("Enter the colour of the vector: ")
            type = int(input("Enter the type of the vector: "))
            nr = int(input("Enter the number of elements in the vector: "))
            while nr != 0:
                element = int(input("Enter an element in the vector: "))
                values.append(element)
                nr -= 1
            vector = MyVector(name_id, colour, type, values)
            return vector
        except ValueError:
            print("Please make sure you enter integers for type,nr and the vector elements.")

    @staticmethod
    def read_index():
        try:
            index = int(input("Enter the index: "))
            return index
        except ValueError as e:
            pass

    @staticmethod
    def read_sum():
        try:
            sum = int(input("Enter the sum: "))
            return sum
        except ValueError as e:
            print("The sum should be an integer.")

    @staticmethod
    def read_scalar():
        try:
            scalar = int(input("Enter the scalar: "))
            return scalar
        except ValueError as e:
            pass

    @staticmethod
    def read_nameID():
        try:
            name_id = input("Enter the name/id of the vector: ")
            if isinstance(name_id, (int, str)):
                return name_id
            else:
                raise TypeError("NameID should be an integer or a string.")
        except ValueError as e:
            print("The error is: {e}")

    def main_meniu(self):
        while True:
            self.show_meniu()
            option=input("Please select an option from above: ")
            print()
            if option=="1":
                vector=self.read_vector()
                self.__controller.add_vector_repo(vector)
            elif option=="2":
                try:
                    vectors = self.__controller.get_vectors_repo()
                    if len(vectors)!=0:
                        for vector in vectors:
                            print(vector)
                    else:
                        raise Exception("No vectors were found.")
                except Exception as e:
                    print(f"It seems like: {e}")
            elif option=="3":
                vector=self.__controller.get_vector_at_index_repo(self.read_index())
                if vector!=None:
                    print(vector)
            elif option=="4":
                try:
                    if len(self.__controller.get_vectors_repo())!=0:
                        self.__controller.update_vector_at_index_repo(self.read_index(),self.read_vector())
                    else:
                        raise Exception("No vectors were found.")
                except Exception as e:
                    print(f"It seems like: {e}")
            elif option=="5":
                try:
                    if len(self.__controller.get_vectors_repo())!=0:
                        self.__controller.update_vector_by_nameID_repo(self.read_nameID(), self.read_vector())
                    else:
                        raise Exception("No vectors were found.")
                except Exception as e:
                    print(f"It seems like: {e}")
            elif option=="6":
                try:
                    if len(self.__controller.get_vectors_repo())!=0:
                        self.__controller.delete_vector_at_index_repo(self.read_index())
                    else:
                        raise Exception("No vectors were found.")
                except Exception as e:
                    print(f"It seems like: {e}")
            elif option=="7":
                try:
                    if len(self.__controller.get_vectors_repo())!=0:
                        self.__controller.delete_vector_by_nameID_repo(self.read_nameID())
                    else:
                        raise Exception("No vectors were found.")
                except Exception as e:
                    print(f"It seems like: {e}")
            elif option=="8":
                try:
                    if len(self.__controller.get_vectors_repo())!=0:
                        self.__controller.plot_all_vectors_repo()
                    else:
                        raise Exception("No vectors were found.")
                except Exception as e:
                    print(f"It seems like: {e}")
            elif option=="9":
                vector_list=self.__controller.vector_with_given_sum_repo(self.read_sum())
                try:
                    if len(vector_list)!=0:
                        for vector in vector_list:
                            print(vector)
                    else:
                        raise Exception("The list of vectors is empty.")
                except Exception as e:
                    print(f"It seems like: {e}")
            elif option=="10":
                try:
                    if len(self.__controller.get_vectors_repo())!=0:
                        self.__controller.delete_vectors_between_two_indexes_repo(self.read_index(),self.read_index())
                    else:
                        raise Exception("The vector list is empty.")
                except Exception as e:
                    print(f"It seems like: {e}")
            elif option=="11":
                try:
                    if len(self.__controller.get_vectors_repo())!=0:
                        self.__controller.update_by_adding_scalar_repo(self.read_scalar())
                    else:
                        raise Exception("The vector list is empty.")
                except Exception as e:
                    print(f"It seems like: {e}")
            elif option=="12":
                return





