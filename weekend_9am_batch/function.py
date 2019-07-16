

#User defined fucntion

'''def add ():  # definition

    print("SDLC")  #  body


add() # calling function

def add1(a,b): # parameters

    c = a+b

    c1 = a-b

    c2 = a*b

    c3 = a/b


    return c,c1,c2,c3

print(add1(4,5))  # arguments


# 1.requried Arguments

def add1(a,b): # parameters

    c = a+b

    c1 = a-b

    c2 = a*b

    c3 = a/b


    return c,c1,c2,c3

print(add1(4,5))  # arguments

# Keyword Arguments:'''

def add (*args):

    for i in args:

        print(type(i))

        for j in i:

            print(type(j))


            if j%2==0:
                print(j,"even")
            else:
                print(j,"odd")



add([1,2,3,4,5,6,6,7,88])






