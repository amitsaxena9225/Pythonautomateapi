

class Test1():

    def __init__(self,name,address):

        self.name = name

        self.address = address


    def setaddress(self,address):
        self.address = address


    def getaddress(self):

        return self.address


test1  = Test1("Jayanti","INDIA")

test2  = Test1("AMIT","bharat")

print(test1.address)

test1.setaddress("Australia")

print(test1.getaddress())
print(test1.address)



#print(test1.name)
#print(test2.name)

#print(test1.address)
#print(test2.address)

#test1.setaddress("US")

#print (test1.getaddress())
