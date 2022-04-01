test_list = [1, 2, 3]
test_list = [1, 2, 3, 4]
test_list = [1, 2, 3, 4, 5]
test_list = [99, 2, 3, 4, 5, 6, 7, 8, 9, 10]

match test_list :
    case [a, b, c]:
        print("List is [a, b, c]", a, b, c)
    case [a, b, c, d]:
        print("List is [a, b, c, d]", a, b, c, d)
    # case [a, *sub_list]:
    #     print("List is [a, *sub_list]", a, sub_list)
    # case [99, *sub_list]:
    #     print("List is [99, *sub_list]",  sub_list)
    case [_, _, _, _, _]:
        print("List is [_, _, _, _, _]", test_list)
    
    case _:
        print("No match")