from Domain.Passenger import Passenger
from Infrastructure.Plane import Plane

class PlaneRepository:
    def __init__(self,planes):
        self.__planes=planes

    def get_planes(self):
        return self.__planes

    def set_planes(self,planes):
        self.__planes=planes

    def add_plane(self,plane):
        self.__planes.append(plane)

    def sort_passengers_by_lastName(self,name_number):
        #sort the passengers by their last name and update the passenger list
        for planes in self.get_planes():
            if planes.get_name_number() == name_number:
                planes.sort_passengers_by_lastName()

    def sort_planes_number_of_passengers(self):
        #Sort the planes by their number of passengers and update the repository
        plane_list=self.get_planes()
        for plane_1 in range (len(plane_list)):
            for plane_2 in range (plane_1+1, len(plane_list)):
                if len(plane_list[plane_1].get_passengers())>len(plane_list[plane_2].get_passengers()):
                    plane_list[plane_1],plane_list[plane_2]=plane_list[plane_2],plane_list[plane_1]

    def sort_planes_number_of_passengers_first_name(self,substring):
        #Sort planes according to the number of passengers with the first name starting with a given substring
        plane_list=self.get_planes()
        new_plane_list=list(filter(lambda plane: plane.substring_in_first_name(substring),plane_list))
        for plane_1 in range (len(new_plane_list)):
            for plane_2 in range (plane_1+1, len(new_plane_list)):
                if len(new_plane_list[plane_1].get_passengers())>len(new_plane_list[plane_2].get_passengers()):
                    new_plane_list[plane_1],new_plane_list[plane_2]=new_plane_list[plane_2],new_plane_list[plane_1]
        self.set_planes(new_plane_list)

    def sort_planes_concatenation(self):
        #Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
        plane_list=self.get_planes()
        for plane_1 in range (len(plane_list)):
            for plane_2 in range (plane_1+1, len(plane_list)):
                if plane_list[plane_1].concatenation() > plane_list[plane_2].concatenation():
                    plane_list[plane_1],plane_list[plane_2]=plane_list[plane_2],plane_list[plane_1]


    def identify_planes_passport_numbers(self):
        #Identify planes that have passengers with passport numbers starting with the same 3 letters
        try:
            plane_list = self.get_planes()
            new_plane_list = list(filter(lambda plane: plane.passengers_with_passport_numbers(), plane_list))
            if len(new_plane_list) != 0:
                return new_plane_list
            else:
                raise Exception("No planes found.")
        except Exception as e:
            print(e)

    def identify_passengers_from_plane(self,plane,string):
        #Identify passengers from a given plane for which the first name or last name contain a string given as parameter
        try:
            passenger_list = plane.get_passengers()
            new_passenger_list = list(filter(lambda passenger: passenger.string_in_first_or_last_name(string),passenger_list))
            if len(new_passenger_list) != 0:
                return new_passenger_list
            else:
                raise Exception("No passengers found.")
        except Exception as e:
            print(e)

    def identify_planes_passenger_given_name(self,first_name,last_name):
        #Identify plane/planes where there is a passenger with given name
        try:
            plane_list = self.get_planes()
            new_plane_list=list(filter(lambda plane: plane.find_passenger_with_name(first_name,last_name),plane_list))
            if len(new_plane_list) != 0:
                return new_plane_list
            else:
                raise Exception("No planes found.")
        except Exception as e:
            print(e)

    @staticmethod
    def init():
        return -1

    @staticmethod
    def getNext(solution,i):
        return solution[i]+1

    @staticmethod
    def isConsistent_diff_last_name(solution,i,passenger_list):
        for j in range (i):
            if solution[j]>=solution[i]:
                return False
            if passenger_list[solution[j]].get_last_name()==passenger_list[solution[i]].get_last_name():
                return False
        return True

    @staticmethod
    def isConsistent_planes(solution,i,plane_list):
        for j in range (i):
            if solution[j]>=solution[i]:
                return False
            if plane_list[solution[j]].get_destination()!=plane_list[solution[i]].get_destination():
                return False
            if plane_list[solution[j]].get_ar_company()==plane_list[solution[i]].get_ar_company():
                return False
        return True


    @staticmethod
    def isSolution(k,solution):
        if len(solution)==k:
            return True
        else:
            return False

    def identify_plane_by_name_number(self,name_number):
        for planes in self.get_planes():
            if planes.get_name_number() == name_number:
                return planes

    def BKT_diff_last_name(self,k,name_number):
        plane=self.identify_plane_by_name_number(name_number)
        passenger_list=plane.get_passengers()
        solution=[]
        solution.append(PlaneRepository.init())
        i=0
        while i>=0:
            isSelected=False
            while isSelected==False and solution[i]<len(passenger_list)-1:
                solution[i]=PlaneRepository.getNext(solution,i)
                isSelected=PlaneRepository.isConsistent_diff_last_name(solution,i,passenger_list)
            if isSelected:
                if PlaneRepository.isSolution(k,solution):
                    yield [passenger_list[solution[i]] for i in range (k)]
                else:
                    i+=1
                    solution.append(PlaneRepository.init())
            else:
                solution.pop()
                i-=1

    def callBKT_diff_last_name(self,k,name_number):
        i=1
        final_passenger_list=[]
        for p in self.BKT_diff_last_name(k,name_number):
            passenger_list=[f"{passenger.get_first_name()} {passenger.get_last_name()} {passenger.get_passport_number()}" for passenger in p]
            print("Group",i,'', end='')
            print (', '.join(passenger_list))
            i+=1
            final_passenger_list.append(p)
        return final_passenger_list

    def BKT_planes(self,k):
        plane_list=self.get_planes()
        i=0
        solution=[]
        solution.append(PlaneRepository.init())
        while i>=0:
            isSelected=False
            while isSelected==False and solution[i]<len(plane_list)-1:
                solution[i]=PlaneRepository.getNext(solution,i)
                isSelected=PlaneRepository.isConsistent_planes(solution,i,plane_list)
            if isSelected:
                if PlaneRepository.isSolution(k,solution):
                    yield [plane_list[solution[i]] for i in range (k)]
                else:
                    i+=1
                    solution.append(PlaneRepository.init())
            else:
                solution.pop()
                i-=1

    def callBKT_planes(self,k):
        final_plane_list=[]
        for p in self.BKT_planes(k):
            plane_list=[f"Plane {plane.get_name_number()}" for plane in p]
            print("Group of planes:",'', end='')
            print (', '.join(plane_list))
            final_plane_list.append(p)
        return final_plane_list





