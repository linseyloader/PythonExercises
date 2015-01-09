import sys
ans = True
while ans:
    print ("""
    1. Write user data to a file.
    2. Print user data.
    3. Quit
    """)
    ans = raw_input("What would you like to do? ")
    if ans == "1":
        f = open("/Users/linseyloader/Documents/dev/CodingCampus/PythonExercises/Exercise4/file4.txt", "w")
        data_one = raw_input("Enter a phrase: ")
        f.write(data_one)
        print "You entered: " + data_one
        f.close()
    elif ans == "2":
        f = open("/Users/linseyloader/Documents/dev/CodingCampus/PythonExercises/Exercise4/file4.txt", "rb").read()
        data_two = text_file.write("Enter as phrase: ")
        text_file.write(data_two)
        print "You entered: " + data_two
    elif ans == "3":
        print("\n Goodbye.")
        sys.exit()
    else:
        print("\n Not an option, try again.")