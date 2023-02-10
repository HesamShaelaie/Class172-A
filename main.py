def simple_print():
    print("Hello")
    print('*'*10)


#============================

def type_var():
    var_int = 10
    var_float = 2.9
    var_str = 'Test'
    var_bool = True

    print(type(var_int))
    print(type(var_float))
    print(type(var_str))
    print(type(var_bool))

#============================

def input_from_user():

    name = input("what is your name?")
    print('your name is ' + name)
    print('your name is %s'%(name))
    print('your name is %10s'%(name))


def print_index_str(Input):
    for x in range(len(Input)):
        print("%3s|"%(str(x)),end="")
    print()
    for x in range(len(Input)):
        print("%3s|"%(Input[x]),end="")
    print("\n\n\n")

def working_with_str():

    course = 'Python for beginners for'
    print(len(course))
    print_index_str(course)

    SearchW = 'P'
    result = course.find(SearchW)
    print("Search for (%10s) with the result at (%10d)"%(SearchW,result))

    SearchW = 'b'
    result = course.find(SearchW)
    print("Search for (%10s) with the result at (%10d)"%(SearchW,result))

    SearchW = 'B'
    result = course.find(SearchW)
    print("Search for (%10s) with the result at (%10d)"%(SearchW,result))

    SearchW = 'beginner'
    result = course.find(SearchW)
    print("Search for (%10s) with the result at (%10d)"%(SearchW,result))

    SearchW = 'for'
    result = course.find(SearchW)
    print("Search for (%10s) with the result at (%10d)"%(SearchW,result))
    print("====== end =======\n")

def Search_for_str(InputStr,SearchStr):
    course = InputStr
    SearchW = SearchStr
    result = course.find(SearchW)
    print("Search for (%10s) with the result at (%10d)"%(SearchW,result))

def working_with_str_with_function():
    course = 'Python for beginners for'
    print_index_str(course)

    SearchW = 'P'
    Search_for_str(course, SearchW)
    

    SearchW = 'b'
    Search_for_str(course, SearchW)

    SearchW = 'B'
    Search_for_str(course, SearchW)

    SearchW = 'beginner'
    Search_for_str(course, SearchW)

    SearchW = 'for'
    Search_for_str(course, SearchW)
    print("====== end =======\n")

def funstions_in_str():
    course = 'Python for beginners with Pycharm'
    print(course)

    print(course.replace('beginners', 'advance class'))
    print(course)

    print(course.replace('Py', 'py'))
    print(course)

    #course.upper()
    #course.upper ()
    #course.lower ()
    #course.title()
    #course.find()
    #course.replace()
    if 'for' in course:
        print("True")
    else:
        print("False")


def arithmetic_operations():
    A = 10
    print(A/3)
    print(A//3)
    print(A%3)
    print(A**2)
    A += 2
    A -= 5
    print(A)

    B = 2.9
    C = round(2.9)
    print(C)


    B = -2.9
    C = abs(2.9)
    print(C)

    import math

    B = 2.9
    C = math.ceil(2.9)
    print(C)

    B = 2.9
    C = math.floor(2.9)
    print(C)

    #https://docs.python.org/3/library/math.html



def conditions():


    








if __name__ == "__main__":
    #simple_print()
    #type_var()
    #input_from_user()
    #working_with_str()
    #working_with_str_with_function()
    #funstions_in_str()
    #arithmetic_operations()
    conditions()


