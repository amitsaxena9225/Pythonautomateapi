

#i=[1,2,3,4,5,6,7]

#print(i)



my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

print(next(my_iter))

print(next(my_iter))

print(next(my_iter))

print(next(my_iter))

print(next(my_iter))






'''0 -object
    ,1\
    ,2\
    ,3\
    ,4,\
     5,6,7,8,9,10


object/iterable(0) ------>iter() --0------>iterator(object)----->next()----1
object/iterable(1) ------>iter() --1------>iterator(object)----->next()----2




object/iterable(1) ------>iter() --1------>iterator(object)----->next()----9
object/iterable(1) ------>iter() --1------>iterator(object)----->next()---- 0,9'''



