number = int(input("Enter a number[1-20]: "))

match number :
    case n if n in range(10) :
        match n :
            case n if n % 2 == 0 :
                print("Number is even")
            case _:
                print("Number is odd")
        print("Number is between 1 and 10")
    case 10|11|12:
        print("Number is between 11 and 12")
    
    case n if n % 2 == 0 :
        print("Number is even")
    case n if n % 2 == 1 :
        print("Number is odd")
    
    case _:
        print("Number is greater than 12")
    
    