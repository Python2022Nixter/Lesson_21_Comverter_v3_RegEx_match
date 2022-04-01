person = {'name': 'John', 'age': 25}
person = {'name': 'Bob', 'age': 35}

def k(s: str) -> str:
    if s.isalpha():
        return "\"" + s + "\""
    return ""

match person:
    case {'name': 'John', 'age': v} :
        print("John is", v, "years old")
    case {} as d:
        print(f"john {k(w)}", d)