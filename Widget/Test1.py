

try:

    a=open("/Users/apple/PycharmProjects/Widget/Test2.txt",'t')

    a.read()




except Exception as e:

    print(e)


except:

    print("Something went wrong")

else:

    print("in try block everything is correct ")


finally:
    print("Always RUN !!!!!!!!!!!!!!!!!!!!!!!!")









'''

try:

    a=open("/Users/apple/PycharmProjects/Widget/Test2.txt",'6')

    a.read()


except Exception as e:

    print(e)

except:

    print("Something went wrong")

else:

    print("in try block everything is correct ")


finally:
    print("Always RUN !!!!!!!!!!!!!!!!!!!!!!!!")'''