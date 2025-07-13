
class Passenger:
    def __init__(self,first_name,last_name,passport_number):
        try:
            if isinstance(first_name,str) and first_name.isalpha():
                self.__first_name = first_name
            else:
                self.__first_name = 'Unknown first name'
                raise TypeError('First Name must be a string.')
        except TypeError as e:
            print(f"The error is: {e}")

        try:
            if isinstance(last_name,str) and last_name.isalpha():
                self.__last_name = last_name
            else:
                self.__last_name = 'Unknown last name'
                raise TypeError('Last Name must be a string.')
        except TypeError as e:
            print(f"The error is: {e}")

        try:
            if isinstance(passport_number,str):
                self.__passport_number = passport_number
            else:
                raise TypeError('Passport_number must be a string.')
        except TypeError as e:
            print(f"The error is: {e}")

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_passport_number(self):
        return self.__passport_number

    def set_first_name(self,first_name):
        try:
            if isinstance(first_name, str) and first_name.isalpha():
                self.__first_name = first_name
            else:
                self.__first_name = 'Unknown first name'
                raise TypeError('First Name must be a string.')
        except TypeError as e:
            print(f"The error is: {e}")

    def set_last_name(self,last_name):
        try:
            if isinstance(last_name, str) and last_name.isalpha():
                self.__last_name = last_name
            else:
                self.__last_name = 'Unknown last name'
                raise TypeError('Last Name must be a string.')
        except TypeError as e:
            print(f"The error is: {e}")

    def set_passport_number(self,passport_number):
        try:
            if isinstance(passport_number,str):
                self.__passport_number = passport_number
            else:
                raise TypeError('Passport_number must be a string.')
        except TypeError as e:
            print(f"The error is: {e}")

    def delete_first_name(self):
        self.__first_name = None

    def delete_last_name(self):
        self.__last_name = None

    def delete_passport_number(self):
        self.__passport_number = None

    def string_in_first_or_last_name(self,string):
        if string in self.get_first_name() or string in self.get_last_name():
            return True
        else:
            return False

    def __str__(self):
        if self.get_first_name() ==None:
            first_name_str="Unknown First Name"
        else:
            first_name_str=self.get_first_name()

        if self.get_last_name() ==None:
            last_name_str="Unknown Last Name"
        else:
            last_name_str=self.get_last_name()

        if self.get_passport_number() ==None:
            passport_number_str="Unknown Passport Number"
        else:
            passport_number_str=self.get_passport_number()
        return f"{first_name_str}, {last_name_str}, ID {passport_number_str}"


