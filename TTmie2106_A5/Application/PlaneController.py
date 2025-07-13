from Infrastructure.PlaneRepository import PlaneRepository
from Infrastructure.Plane import Plane
from Domain.Passenger import Passenger

class PlaneController:
    def __init__(self,plane_repo):
        self.__plane_repo = plane_repo

    def get_planes_repo(self):
        return self.__plane_repo.get_planes()

    def set_planes_repo(self,planes):
        self.__plane_repo.set_planes(planes)

    def add_plane_repo(self,plane):
        self.__plane_repo.add_plane(plane)

    def sort_passengers_by_lastName_repo(self,name_number):
        self.__plane_repo.sort_passengers_by_lastName(name_number)

    def sort_planes_number_of_passengers_repo(self):
        self.__plane_repo.sort_planes_number_of_passengers()

    def sort_planes_number_of_passengers_first_name_repo(self,substring):
        self.__plane_repo.sort_planes_number_of_passengers_first_name(substring)

    def sort_planes_concatenation_repo(self):
        self.__plane_repo.sort_planes_concatenation()

    def identify_planes_passport_numbers_repo(self):
        return self.__plane_repo.identify_planes_passport_numbers()

    def identify_passengers_from_plane_repo(self,plane,string):
        return self.__plane_repo.identify_passengers_from_plane(plane,string)

    def identify_planes_passenger_given_name_repo(self,first_name,last_name):
        return self.__plane_repo.identify_planes_passenger_given_name(first_name,last_name)

    def callBKT_diff_last_name_repo(self,k,name_number):
        passenger_list=self.__plane_repo.callBKT_diff_last_name(k,name_number)
        return passenger_list

    def callBKT_planes(self,k):
        plane_list=self.__plane_repo.callBKT_planes(k)
        return plane_list
