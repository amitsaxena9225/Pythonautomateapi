
class Amit:

    def __init__(self,fname,lname):

        self.fname = fname
        self.lname = lname

    def fullname(self):

        return self.fname +' '+self.lname


var = Amit("Amit","Saxena")


print("First Name is :",var.fname)

print("Last Name:",var.lname)

print("Full Name is:",var.fullname())

