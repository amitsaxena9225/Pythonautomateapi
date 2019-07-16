

class Even_odd:

    even=[]
    odd=[]

    def __init__(self,list1):

        self.list1 =[1,2,3,4,5,5,6,7,78,8]


    def even(self):

        for i in self.list1:
            if i%2==0:

                print(i,"num is even")
                even.append(i)

    def odd(self):

        for i in self.list1:
            if i % 2 != 0:
                even.append(i)
                print(i, "num is odd")
                even.append(i)


    def __str__(self):

        return cls.even



var =Even_odd([1,2,3,4,5,5,6,7,78,8])


print(var.even())

print(id(var.even))

print(var.odd)

