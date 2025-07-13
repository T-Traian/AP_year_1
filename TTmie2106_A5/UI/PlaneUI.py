from types import NoneType

from Application.PlaneController import PlaneController
from Domain.Passenger import Passenger
from Infrastructure.PlaneRepository import PlaneRepository
from Infrastructure.Plane import Plane

class PlaneUI:
    def __init__(self,plane_controller):
        self.__plane_controller = plane_controller

    @staticmethod
    def show_meniu():
        print()
        print("1.Index a list of planes.")
        print("2.Get all the planes.")
        print("3.Add a plane.")
        print("4.Sort the passengers in a plane given by name/number by last name.")
        print("5.Sort planes according to the number of passengers.")
        print("6.Sort planes according to the number of passengers with the first name starting with a given substring.")
        print("7.Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination.")
        print("8.Identify planes that have passengers with passport numbers starting with the same 3 letters.")
        print("9.Identify passengers from a given plane for which the first name or last name contain a string given as parameter.")
        print("10.Identify plane/planes where there is a passenger with given name.")
        print("11.Form groups of k passengers from the same plane but with different last names.")
        print("12.Form groups of k planes with the same destination but belonging to different airline companies.")
        print("13.Exit.")

    @staticmethod
    def read_passenger():
        first_name=input("Enter first name: ")
        last_name=input("Enter last name: ")
        passport_number=input("Enter passport number: ")
        passenger=Passenger(first_name,last_name,passport_number)
        return passenger

    @staticmethod
    def read_plane():
        name_number=input("Enter the name/number of the plane: ")
        ar_company=input("Enter the name of the company: ")
        number_of_seats=int(input("Enter the number of seats: "))
        destination=input("Enter the destination: ")
        nr=int(input("How many passengers are expected? Enter response: "))
        passenger_list=[]
        while nr!=0:
            passenger=PlaneUI.read_passenger()
            passenger_list.append(passenger)
            nr-=1
        plane=Plane(name_number,ar_company,number_of_seats,destination,passenger_list)
        return plane

    @staticmethod
    def read_name_number():
        try:
            name_number=input("Enter the name/number of the plane: ")
            if isinstance(name_number,(str,int)):
                return name_number
            else:
                raise Exception ("Name/number must be of type str or int.")
        except Exception as e:
            print({e})

    def main_meniu(self):
        while True:
            self.show_meniu()
            option=(input("Please select an option from the above list: "))
            if option=="1":
                print()
                try:
                    if len(self.__plane_controller.get_planes_repo())!=0:
                        raise Exception("There are already planes that are due.")
                    else:
                        nr = int(input("How many planes are due to fly? Enter response: "))
                        plane_list = []
                        while nr != 0:
                            plane = self.read_plane()
                            plane_list.append(plane)
                            nr -= 1
                        self.__plane_controller.set_planes_repo(plane_list)
                except Exception as e:
                    print(e)
            elif option=='2':
                print()
                try:
                    plane_list=self.__plane_controller.get_planes_repo()
                    if len(plane_list)!=0:
                        for plane in plane_list:
                            print(plane)
                    else:
                        raise Exception("No planes found.")
                except Exception as e:
                    print(e)
            elif option=='3':
                print()
                plane=PlaneUI.read_plane()
                self.__plane_controller.add_plane_repo(plane)
            elif option=='4':
                try:
                    if len(self.__plane_controller.get_planes_repo())!=0:
                        try:
                            print()
                            name_number=input("Enter the name/number of the desired plane: ")
                            if isinstance(name_number, (str, int)):
                                self.__plane_controller.sort_passengers_by_lastName_repo(name_number)
                                print("Sorted successfully.")
                            else:
                                raise TypeError("The name/number must be a string or an integer.")
                        except TypeError as e:
                            print(f"The error is: {e}")
                    else:
                        raise Exception("No planes found.")
                except Exception as e:
                    print(e)
            elif option=='5':
                try:
                    if len(self.__plane_controller.get_planes_repo())!=0:
                        print()
                        self.__plane_controller.sort_planes_number_of_passengers_repo()
                        print("Planes sorted successfully.")
                    else:
                        print()
                        raise Exception("There are no planes to sort.")
                except Exception as e:
                    print(e)
            elif option=='6':
                try:
                    if len(self.__plane_controller.get_planes_repo())!=0:
                        print()
                        substring=input("Enter the substring: ")
                        self.__plane_controller.sort_planes_number_of_passengers_first_name_repo(substring)
                        print("Planes sorted successfully.")
                    else:
                        print()
                        raise Exception("There are no planes to sort.")
                except Exception as e:
                    print(e)
            elif option=='7':
                try:
                    if len(self.__plane_controller.get_planes_repo())!=0:
                        print()
                        self.__plane_controller.sort_planes_concatenation_repo()
                        print("Planes sorted successfully.")
                    else:
                        print()
                        raise Exception("There are no planes to sort.")
                except Exception as e:
                    print(e)
            elif option=='8':
                print()
                plane_list = self.__plane_controller.identify_planes_passport_numbers_repo()
                if plane_list is not None:
                    for plane in plane_list:
                        print(plane)
            elif option=='9':
                print()
                plane=PlaneUI.read_plane()
                print()
                string=input("Enter the string: ")
                plane_list=self.__plane_controller.identify_passengers_from_plane_repo(plane,string)
                if plane_list is not None:
                    for plane in plane_list:
                        print(plane)
            elif option=='10':
                print()
                try:
                    first_name = input("Enter the first name: ")
                    last_name = input("Enter the last name: ")
                    print()
                    if isinstance(first_name, str) and first_name.isalpha():
                        if isinstance(last_name, str) and last_name.isalpha():
                            plane_list = self.__plane_controller.identify_planes_passenger_given_name_repo(first_name, last_name)
                            if plane_list is not None:
                                for plane in plane_list:
                                    print(plane)

                        else: raise Exception("Name must be valid.")
                    else: raise Exception("Name must be valid.")
                except Exception as e:
                    print(e)
            elif option=="11":
                try:
                    if len(self.__plane_controller.get_planes_repo())!=0:
                        name_number=PlaneUI.read_name_number()
                        k=int(input("Enter how many passengers there are in a group: "))
                        passenger_list=self.__plane_controller.callBKT_diff_last_name_repo(k,name_number)
                    else:
                        print()
                        raise Exception("There are no planes.")
                except Exception as e:
                    print(e)
            elif option=="12":
                try:
                    if len(self.__plane_controller.get_planes_repo())!=0:
                        k=int(input("Enter how many planes there are in a group: "))
                        plane_list=self.__plane_controller.callBKT_planes(k)
                    else:
                        print()
                        raise Exception("There are no planes.")
                except Exception as e:
                    print(e)
            elif option=="13":
                exit()





