from sys import exit

ans = True
while ans:
    print ("""
    1. Write and save a phrase.
    2. Print previous phrases.
    3. Quit
    """)

    ans = raw_input("What would you like to do? ")

    if ans == "1":
        phrase_one = raw_input("Enter a phrase: ")
        f = open("file4.txt", "a")
        f.write("\n" + phrase_one)
        print "You entered: " + phrase_one
        f.close()
    elif ans == "2":
        f = open("file4.txt", "rb")
        for line in f:
            print line
        f.close()
    elif ans == "3":
        print("\nGoodbye.\n")
        exit()
    else:
        print("\nNot an option, try again.")