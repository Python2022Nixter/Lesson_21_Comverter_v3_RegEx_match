num = int(input("Enter a number[1-20]: "))

match num :
    case x if x in range(10) :
        print("Number is between 1 and 10")
    case 10|11|12:
        print("Number is between 11 and 12")
    
    case _:
        print("Number is greater than 12")