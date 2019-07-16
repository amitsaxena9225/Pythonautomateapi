try:

    with open("/Users/apple/PycharmProjects/weekend_11am batch/pavithra.txt","r") as filename:


        #print(filename.read())
        #print(filename.readline(5))
        print(filename.readlines(5))


except Exception as error:

    print(error)

except:

    print("Page Not Found Error")

#with open("/Users/apple/PycharmProjects/weekend_11am batch/p1.txt", "y") as filename:
    #filename.write("AMIT")


else:
    with open("/Users/apple/PycharmProjects/weekend_11am batch/xyz.txt", "w") as filename:

        a=["bcjkdhebfkebf","ewvhewbdh","efbhbccchb"]

        filename.writelines(a)

finally:

    print("It will run always does not matter you try block is working or not")

