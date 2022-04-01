# Structual Pattern Matching
# match - switch on any languages

action = input("Enter action[read, write, print]: ")

match action :
    case "read" :
        print("Reading file...")
    case "write" :
        print("Writing file...")
    case "print" :
        print("Printing file...")
    case _:
        print("Invalid action")