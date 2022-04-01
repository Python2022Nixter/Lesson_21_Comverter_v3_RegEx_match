# class matching

a = 4
a  = 4.1
a = "a"
a = [1, 2, 3]
a = ["1", "5", "4"]
match a :
    case int(a):
        print("a is an integer")
    case float(a):
        print("a is a float")
    case str(a):
        print("a is a string")
    case [int(_), *b]:
        print("a is a list of integers", b)
    case [str(_), *b]:
        print("a is a list of strings", b)
    case _:
        print("a is something else")