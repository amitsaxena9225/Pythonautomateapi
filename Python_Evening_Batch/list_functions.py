
# list is hetrogeneous data type means it can store different types of value.

# list is mutable data type

# a = [1,10.5,2+3j,"Amit" ,{1:2,4:5} ,(1,2,3,4), [1,2,23,

# a ="python"


# print(type(a))

# print(a)

# list supports indexing and silicing

''' print("Total number of elements:", len(a))  # length starts from 1


print(a[0])

print(a[1])

print(a[2])
print(a[3])
print(a[4])
print(a[5])'''

# print(a[1:6]) # a[start:end] end value will be excluded ,range

# print(a[1:-2]) # a[1:4]


# print(a[-1:-5]) # we will follow Left to Right approach not right toi left

# print(len(a))

# print(a[0:5:2]) #start:end:diff


# formula--->len(str) + (negative value)  ---> 6 +(-6) --> 0


# a1= dir(list)

# print(len(a1))

# b = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# print(len(b))

a = [1, 2, 3, 4, 51, 51, 7, 8, 9, 51]

print("before", a)

# print(len(a))

# print(a.count(51))

# print(a.remove(51))

# a.pop(5)
# a.insert(5, 6)

# print(a)
# print(len(a))

# print(a.append(("amit","saxena")))

print('\n')  # new line character

# a.clear()

# a.extend("amit")

# a.extend({1: 2})
;;
# a.reverse()
a.sort(reverse=True)

print("after", a)









