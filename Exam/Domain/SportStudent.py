

class SportStudent:
    def __init__(self,sport=str,score=int,year=int):
        self.__sport=sport
        self.__score=score
        self.__year=year

    def getSport(self):
        return self.__sport         #returns the type of sport

    def getScore(self):
        return self.__score         #returns the score

    def getYear(self):
        return self.__year          #returns the year

    def setSport(self,sport):
        self.__sport=sport          #sets the type of sport

    def setScore(self,score):
        self.__score=score          #sets the score

    def setYear(self,year):
        self.__year=year            #sets the year

    def __repr__(self):
        return f"Sport: {self.__sport} Score: {self.__score} Year: {self.__year}"

    def __eq__(self,other):
        if self.getSport()==other.getSport():           #verifies if 2 students have the same sport, score and year
            if self.getScore()==other.getScore():
                if self.getYear()==other.getYear():
                    return True
        return False