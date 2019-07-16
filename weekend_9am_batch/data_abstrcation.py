class Myclass():


    __hiddenvariable = 1  # private varaible
    _hiddenvariable = 1  # protected varaible

    def add(self, increment):
        self.__hiddenvariable += increment

        return (self.__hiddenvariable)

    '''def __funct(self)

    def _fincu1(self)'''


object1 = Myclass()

object1.add(2)

# object1.add(10)

print(object1._Myclass__hiddenvariable)  #preivate

print(object1._hiddenvariable)  #protected
