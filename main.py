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

    is_hot = False
    is_cold = False

    if is_hot:
        print("It's a hot day")
        print ("Drink plenty of water")
    elif is_cold:
        print("It's a cold day")
        print ("Wear warm clothes")
    else:
        print ("It's a lovely day")
    

    A = False
    B = False
    if A and B:
        print("AND-> True")
    else:
        print("AND-> False")

    A = False
    B = False
    if A & B:
        print("AND-> True")
    else:
        print("AND-> False")

    

    A = False
    B = False
    if A or B:
        print("OR-> True")
    else:
        print("OR-> False")

    A = False
    B = False
    if A | B:
        print("OR-> True")
    else:
        print("OR-> False")

    A = False
    if not A:
        print("NOT-> True")
    else:
        print("NOT-> False")

    A = False
    if ~A:
        print("NOT-> True")
    else:
        print("NOT-> False")


    a = True
    b = False

    # Finding XOR of boolean values using ^ operator
    p = a ^ a
    q = a ^ b
    r = b ^ a
    s = b ^ b

    # Printing the XOR value of every boolean combination
    print(a, "XOR", a, "=", p)
    print(a, "XOR", b, "=", q)
    print(b, "XOR", a, "=", r)
    print(b, "XOR", b, "=", s)

    # == for equality
    # >= greater than
    # >  greater
    # <= less than
    # <  less


def loops():
    i = 1
    while i <= 5:
        print('*' * i)
        i += 1

    for x in range(1,6):
        print('*' * x)


def try_your_luck():
    secret_number = 9
    guess_count = 0
    guess_limit = 3

    while guess_count < guess_limit:
        guess = int (input( 'Guess: '))
        guess_count += 1
        if guess == secret_number:
            print ( "You won!")
            break
    else:
        print('Sorry, you failed!!')

def lists():
    var_str = "python"
    for x in var_str:
        print(x)

    list_name = ["Mosh","John","Sarah", "Mary", "Hesam", "Amanda"]
    for x in list_name:
        print(x)

    print(list_name[3])
    print(list_name[-1])
    print(list_name[2:3])
    
    for x in [1,2,3,4,5,6]:
        print(x)

    for x in range(1,6,2):
        print(x)
    
    total = 0
    prices = [10,20,30]
    for x in prices:
        total += x
    print(f"Total:{total}") 

    for x in range (4):
        for y in range(3):
            print (f"({x}, {y})")

    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    print(matrix[0][1])

    for row in matrix:
        for clm in row:
            print(clm)

    numbers = [5,6,3,7,10, 5, 7]
    numbers.append(312)
    print(numbers) 

    numbers.insert(0,221)
    print(numbers) 

    
    numbers.remove(5)
    print(numbers)

    numbers.remove(5)
    print(numbers)

    #numbers.remove(5)
    #print(numbers)

    tmp = numbers.pop()
    print(tmp)
    print(numbers)

    tmp = numbers.index(7)
    print(tmp)

    #tmp = numbers.index(74)
    #print(tmp)

    print(50 in numbers)

    print(numbers.count(7))

    numbers.sort()
    print(numbers)

    numbers.reverse()
    print(numbers)

    numbers_A = numbers
    numbers_B = numbers.copy()

    numbers[0] = 1000
    print(numbers)
    print(numbers_A)
    print(numbers_B)

    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    import copy
    matrix_A = matrix
    matrix_B = matrix.copy()
    matrix_C = copy.deepcopy(matrix)
    matrix[0][0] = 1000

    print(matrix)
    print(matrix_A)
    print(matrix_B)
    print(matrix_C)

    matrix_B.append([5,5,5])
    print(matrix)
    print(matrix_A)
    print(matrix_B)
    print(matrix_C)


def find_uniques():
    numbers = 12, 2, 4, 6, 3, 4, 6, 11
    uniques = []
    for number in numbers:
        if number not in uniques:
            uniques .append (number)
    print (uniques)

def List_Set_Dictionary_Tuple():
    text = "Hello World!"
    print(list(text))
    print(set(text))

    list_a = list(text)
    set_a = set(text)
    print(list_a[:2])
    #print(set_a[:2])


    list_a = [1,2,3,4]
    list_a.append(5)
    print(list_a)
    
    tuple_a = (1,2,3,4)
    #tuple_a.append(5)
    

    tuple_a = ([1,3], 'a', 'b', 8)
    tuple_a[0][0] = 99
    print(tuple_a)


    list_a = ['a','b',3,6]
    list_a.remove('a')
    print(list_a)
    
    set_a = {'a','b',3,6}
    set_a.remove('a')
    print(set_a)

    a = {1,2,3}
    #a.remove(5)

    a = {1,2,3}
    a.discard(5)
    print(a)

    list_a = ['a','b',3,6,4]
    item = list_a.pop()
    print(list_a)
    print(item)

    
    set_a =  {'a','b',3, 6, 4}
    item2 = set_a.pop()
    print(set_a)
    print(item2)

    a = [1,2,3]
    a.append(4)
    print(a)

    b = {1,2,3}
    b.add(4)
    print(b)

    a = {1,2,3,4}
    b = {1,5,6}
    print(a.union(b))
    
    a = {'x', 1, 4}
    b = [3, 4, 1]
    c = ('x', 'y', 'z')
    a.update(b,c)
    print(a)


    print("=============")
    s = {'H', 'I', 'J', 'K', 1,2,3}
    t = { 'o', 'p', 'e', 'n', 1,2,3}

    print(s - t)
    print(s)
    print(s.difference(t))
    print(s)

    #s & t 
    #s.intersection(t)

    #s | t
    #s.union(t)
    print("=============")

    








if __name__ == "__main__":
    #simple_print()
    #type_var()
    #input_from_user()
    #working_with_str()
    #working_with_str_with_function()
    #funstions_in_str()
    #arithmetic_operations()
    #conditions()
    #loops()
    #try_your_luck()
    #lists()
    List_Set_Dictionary_Tuple()




