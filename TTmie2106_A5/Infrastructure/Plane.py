from Domain.Passenger import Passenger

class Plane:
    def __init__(self,name_number,ar_company,number_of_seats,destination,passengers=[]):
        try:
            if isinstance(name_number,(str,int)):
                self.__name_number=name_number
            else:
                raise TypeError("The name/number must be a string or an integer.")
        except TypeError as e:
            print(f"The error is: {e}")

        try:
            if isinstance(ar_company,(str)) and ar_company.isalpha():
                self.__ar_company=ar_company
            else:
                self.__ar_company="Unknown airline company"
                raise TypeError("The airline company must be a string.")
        except TypeError as e:
            print(f"The error is: {e}")

        try:
            if isinstance(number_of_seats,(int)):
                self.__number_of_seats=number_of_seats
            else:
                raise TypeError("The number of seats must be an integer.")
        except TypeError as e:
            print(f"The error is: {e}")

        try:
            if isinstance(destination,(str)) and destination.isalpha():
                self.__destination=destination
            else:
                self.__destination="Unknown destination"
                raise TypeError("The destination must be a string.")
        except TypeError as e:
            print(f"The error is: {e}")

        try:
            for passenger in passengers:
                if not isinstance(passenger,Passenger):
                    raise TypeError("The passenger must be a Passenger object.")
            self.__passengers=passengers
        except TypeError as e:
            print(f"The error is: {e}")

    def get_name_number(self):
        return self.__name_number

    def get_ar_company(self):
        return self.__ar_company

    def get_number_of_seats(self):
        return self.__number_of_seats

    def get_destination(self):
        return self.__destination

    def get_passengers(self):
        return self.__passengers

    def set_name_number(self,name_number):
        try:
            if isinstance(name_number,(str,int)):
                self.__name_number=name_number
            else:
                raise TypeError("The name/number must be a string or an integer.")
        except TypeError as e:
            print(f"The error is: {e}")

    def set_ar_company(self,ar_company):
        try:
            if isinstance(ar_company, (str)) and ar_company.isalpha():
                self.__ar_company = ar_company
            else:
                self.__ar_company = "Unknown airline company"
                raise TypeError("The airline company must be a string.")
        except TypeError as e:
            print(f"The error is: {e}")

    def set_number_of_seats(self,number_of_seats):
        try:
            if isinstance(number_of_seats,(int)):
                self.__number_of_seats=number_of_seats
            else:
                raise TypeError("The number of seats must be an integer.")
        except TypeError as e:
            print(f"The error is: {e}")

    def set_destination(self,destination):
        try:
            if isinstance(destination, (str)) and destination.isalpha():
                self.__destination = destination
            else:
                self.__destination = "Unknown destination"
                raise TypeError("The destination must be a string.")
        except TypeError as e:
            print(f"The error is: {e}")

    def set_passengers(self,passengers):
        try:
            for passenger in passengers:
                if not isinstance(passenger,Passenger):
                    raise TypeError("The passenger must be a Passenger object.")
            self.__passengers=passengers
        except TypeError as e:
            print(f"The error is: {e}")

    def delete_name_number(self):
        self.__name_number=None

    def delete_ar_company(self):
        self.__ar_company=None

    def delete_number_of_seats(self):
        self.__number_of_seats=None

    def delete_destination(self):
        self.__destination=None

    def delete_passengers(self):
        self.__passengers=None

    def __str__(self):
        if self.get_name_number() is None:
            name_number_str="Unknown name/number"
        else:
            name_number_str=self.get_name_number()
        if self.get_ar_company() is None:
            ar_company_str="Unknown airline company"
        else:
            ar_company_str=self.get_ar_company()
        if self.get_number_of_seats() is None:
            number_of_seats_str="Unknown number of seats"
        else:
            number_of_seats_str=self.get_number_of_seats()
        if self.get_destination() is None:
            destination_str="Unknown destination"
        else:
            destination_str=self.get_destination()
        if self.get_passengers() is None:
            passengers_str="Unknown passengers"
        else:
            passenger_str = '; '.join(str(passenger) for passenger in self.get_passengers())
        return f"The plane: {name_number_str}, owned by {ar_company_str} has {number_of_seats_str} seats, is headed to {destination_str}, passengers: {passenger_str}."

    def substring_in_first_name(self,substring):
        try:
            if isinstance(substring,str):
                passenger_list = self.get_passengers()
                for passenger in passenger_list:
                    first_name = passenger.get_first_name()
                    if not first_name.startswith(substring):
                        return False
                return True
            else:
                raise TypeError("The substring must be a string.")
        except TypeError as e:
            print(f"The error is: {e}")

    def concatenation(self):
        concatenated=str(len(self.get_passengers()))+self.get_destination()
        return concatenated

    def passengers_with_passport_numbers(self):
        #Identify if all the passengers passport numbers start with the exact same 3 numbers
        passengers_list=self.get_passengers()
        try:
            if len(passengers_list)==0:
                raise Exception("The passengers list cannot be empty.")
            else:
                number=passengers_list[0].get_passport_number()[:3]
                for passenger in passengers_list:
                    passport_number=passenger.get_passport_number()
                    if not passport_number.startswith(number):
                        return False
                return True
        except Exception as e:
            print(f"The error is: {e}")

    def find_passenger_with_name(self,first_name,last_name):
        try:
            passenger_list = self.get_passengers()
            if len(passenger_list)!=0:
                for passenger in passenger_list:
                    if passenger.get_first_name() == first_name and passenger.get_last_name() == last_name:
                        return True
                return False
            else:
                raise Exception("The passengers list cannot be empty.")
        except TypeError as e:
            print(f"The error is: {e}")

    def sort_passengers_by_lastName(self):
        #sort the passengers by their last name and update the passenger list
        passenger_list=self.get_passengers()
        for passenger_1 in range (len(passenger_list)):
            for passenger_2 in range (passenger_1+1, len(passenger_list)):
                if passenger_list[passenger_1].get_last_name()>passenger_list[passenger_2].get_last_name():
                    passenger_list[passenger_1],passenger_list[passenger_2]=passenger_list[passenger_2],passenger_list[passenger_1]




