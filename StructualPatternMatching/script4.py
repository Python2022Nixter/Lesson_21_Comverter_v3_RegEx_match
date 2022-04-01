# match against a pattern

action = input("Enter action, file name[ACTION FILE_NAME]: ")

match action.split(): 
    case ["read", file_name] :
        print("Reading file...", file_name)
    case ["write", file_name] :
        print("Writing file...", file_name)
    case ["print", file_name] :
        print("Printing file...", file_name)