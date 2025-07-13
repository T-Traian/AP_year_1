import logic

v=[]
undo_list=[]

def get_user_input():
    try:
        x1=int(input("Enter first number: "))
        x2=int(input("Enter second number: "))
        if x1>-1 and x2>-1:
            return x1,x2
        else:
            print("Invalid input!")
            return None,None
    except:
        print("Invalid input! Please enter valid numbers.")
        return None, None

def get_user_input_1():
    try:
        x1=int(input("Enter number: "))
        if x1>-1:
            return x1
        else:
            print ("Invalid input!")
            return None
    except:
        print("Invalid input!")
        return None

def show_meniu():
    print("\nMenu:")
    print ("1. Add a value to an array:")
    print ("2. Insert a value to an array:")
    print ("3. Delete the value at index:")
    print ("4. Delete the values between the two given index:")
    print ("5. Replace all instances of the first number with the seccond:")
    print ("6. Print all the prime numbers between the two given index:")
    print ("7. Print all the odd numbers between the two given index:")
    print ("8. Return the sum of elements between the two given index:")
    print ("9. Return the gcd of all the elements between the two given index:")
    print ("10. Return the maximum value between the two given index:")
    print ("11. Keep only prime numbers, remove the other elements:")
    print ("12. Keep only negative numbers, remove the other elements:")
    print ("13. Undo:")
    print ("14. Exit.")
    choice = input("Please select an option (1-14): ")
    return choice

def main():
    global undo_list,v
    while True:
        choice=show_meniu()
        if choice=="1":
            x1=get_user_input_1()
            if x1!=None:
                undo_list.append(v[:])
                logic.add_array(v,x1)
                print("The array is:",v)
        elif choice=="2":
            x1,x2=get_user_input()
            if x1!=None and x2!=None:
                    undo_list.append(v[:])
                    logic.insert_array(v, x1, x2)
                    print("The array is:", v)
        elif choice=="3":
            x1=get_user_input_1()
            if x1!=None:
                if x1<len(v) and x1>=0:
                    undo_list.append(v[:])
                    logic.remove_array(v, x1)
                    print("The array is:", v)
                else:
                    print("Invalid input!")
        elif choice=="4":
            x1,x2=get_user_input()
            if x1!=None and x2!=None:
                if x1<len(v) and x1>=0:
                    if x2<len(v) and x2>=0:
                        undo_list.append(v[:])
                        logic.remove_array_index(v, x1, x2)
                        print("The array is:", v)
                    else:
                        print("Invalid input!")
                else:
                    print("Invalid input!")
        elif choice=="5":
            x1,x2=get_user_input()
            if x1!=None and x2!=None:
                undo_list.append(v[:])
                logic.replace_array(v,x1,x2)
                print("The array is:",v)
        elif choice=="6":
            x1,x2=get_user_input()
            if x1!=None and x2!=None:
                if x1<len(v) and x1>=0:
                    if x2<len(v) and x2>=0:
                        undo_list.append(v[:])
                        print("The numbers are:", ' ', end='')
                        result=logic.prime_array(v, x1, x2)
                        print (result)
                        print()
                    else:
                        print("Invalid input!")
                else:
                    print("Invalid input!")
        elif choice=="7":
            x1,x2=get_user_input()
            if x1!=None and x2!=None:
                if x1<len(v) and x1>=0:
                    if x2<len(v) and x2>=0:
                        print("The numbers are:", ' ', end='')
                        undo_list.append(v[:])
                        result=logic.odd_array(v, x1, x2)
                        print (result)
                        print()
                    else:
                        print("Invalid input!")
                else:
                    print("Invalid input!")
        elif choice=="8":
            x1,x2=get_user_input()
            if x1!=None and x2!=None:
                if x1<len(v) and x1>=0:
                    if x2<len(v) and x2>=0:
                        undo_list.append(v[:])
                        result = logic.sum_array(v, x1, x2)
                        print("The sum is:", result)
                    else:
                        print("Invalid input!")
                else:
                    print("Invalid input!")
        elif choice=="9":
            x1,x2=get_user_input()
            if x1!=None and x2!=None:
                if x1<len(v) and x1>=0:
                    if x2<len(v) and x2>=0:
                        undo_list.append(v[:])
                        result = logic.gcd_array(v, x1, x2)
                        print("The gcd is:", result)
                    else:
                        print("Invalid input!")
                else:
                    print("Invalid input!")
        elif choice=="10":
            x1,x2=get_user_input()
            if x1!=None and x2!=None:
                if x1<len(v) and x1>=0:
                    if x2<len(v) and x2>=0:
                        undo_list.append(v[:])
                        result = logic.max_array(v, x1, x2)
                        print("The maximum is:", result)
                    else:
                        print("Invalid input!")
                else:
                    print("Invalid input!")
        elif choice=="11":
            undo_list.append(v[:])
            logic.filter_prime(v)
            print("The array is:",v)
        elif choice=="12":
            undo_list.append(v[:])
            logic.filter_negative(v)
            print("The array is:",v)
        elif choice=="13":
            logic.undo(undo_list,v)
        elif choice=="14":
            print("Goobbye!")
            break
        else:
            print("Invalid input entered!")



if __name__ == "__main__":
    main()