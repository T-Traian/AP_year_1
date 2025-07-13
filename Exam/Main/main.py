from Domain.SportStudent import SportStudent
from Infrastructure.SportCompetition import SportCompetition

def showMeniu():
    print()
    print("1.Display how many students want to participate in each sport:")
    print("2.Display the list of items:")
    print("3.Add a new student:")
    print("4.Increase the score of every student registered for a given sport with their age:")
    print("5.Delete all items which have a given sport and a given birth year:")
    print("6.Exit:")
    choice=input("Enter your choice: ")
    return choice

def main():
    student1=SportStudent("tennis",23,2000)
    student2=SportStudent("basketball",72,2005)
    student3=SportStudent("football",44,2008)
    student4=SportStudent("tennis",82,2004)
    students=[student1,student2,student3,student4]
    competition=SportCompetition(students)

    while True:     #the meniu will be shown as long as the user does not exit
        choice=showMeniu()      #based on the users choice we call each function in the repository
        if choice=="1":
            print()
            competition.displayHowManyStudents()
            print()
        elif choice=="2":
            print()
            competition.displayItems()
            print()
        elif choice=="3":
            sport=input("Enter the sport of the student: ")
            score=int(input("Enter the score of the student: "))
            year=int(input("Enter the year of the student: "))
            student=SportStudent(sport,score,year)
            competition.addItem(student)
        elif choice=="4":
            sport=input("Enter the sport of the students which need score modifications: ")
            list=competition.increaseScore(sport)
            print()
            for student in list:
                print(student)
        elif choice=="5":
            sport=input("Enter the sport which needs to be deleted: ")
            year=int(input("Enter the year of the student: "))
            competition.deleteItems(sport,year)
        elif choice=="6":
            break

if __name__=="__main__":
    main()
