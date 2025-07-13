sports_list=["tennis","football","basketball"]
from Domain.SportStudent import SportStudent


class SportCompetition:
    def __init__(self,students):
        self.__students=students

    def getStudents(self):
        return self.__students      #return the list of sport students

    def setStudents(self,students):
        self.__students=students

    def displayHowManyStudents(self):
        tennis_number=football_number=basketball_number=0       #display how many students there are for each sport
        for student in self.getStudents():
            if student.getSport()=="tennis":
                tennis_number+=1
            else:
                if student.getSport()=="football":
                    football_number+=1
                else:
                    if student.getSport()=="basketball":
                        basketball_number+=1
        print("tennis number:",tennis_number, end=' ')
        print("football number:",football_number, end=' ')
        print("basketball number:",basketball_number, end=' ')

    def displayItems(self):
        for student in self.getStudents():      #display every student with their sport, score and year of birth
            print(student)

    def addItem(self,SportStudent):
        try:
            if SportStudent.getSport() not in sports_list:                      #add a new item
                raise TypeError ("Please enter a valid sport.")
            else:
                if SportStudent.getScore()<0 or SportStudent.getScore()>100:
                    raise TypeError ("Please enter a valid score.")
                else:
                    if SportStudent.getYear()>2025:
                        raise TypeError ("Please enter a valid year.")
                    else:
                        self.__students.append(SportStudent)
        except TypeError as error:
            print(error)

    def increaseScore(self,sport):                  #increase the score of every student with the given sport with their age
        new_list=[]
        for student in self.getStudents():
            if student.getSport()==sport:
                new_score=2025-student.getYear()        #this is new score which is the old score + their age which is the current year - their birth
                if student.getScore()+new_score>100:
                    student.setScore(100)
                    new_list.append(student)
                else:
                    student.setScore(student.getScore()+new_score)
                    new_list.append(student)
        return new_list         #return the list of the affected students

    def deleteItems(self,sport,year):
        pos=0
        list=self.getStudents()
        while pos<len(list):
            if list[pos].getSport()==sport and list[pos].getYear()==year:       #delete students with the specified sport and year
                list.pop(pos)
                pos-=1          #pos needs to be lowered when we use pop because the index of the list also changes
            pos+=1              #if we do not use pos-=1 a possition will be skiped
