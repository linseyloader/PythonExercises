def main():
    while True:
        miles = raw_input("Please enter a speed in miles/hours: ")
        miles_org = int(miles)

        barley = 117.647
        furlong = 220
        fortnight = 2
        mach = 1130
        light = 299792458

        print "Original speed in mph:", (miles_org)
        print "Converted to barleycorn/day is:", (miles_org)
        print "Converted to furlongs/fornight is:", (miles_org)
        print "Converted to Mach number is:", (miles_org)
        print "Converted to the percentage of the speed of light is", (miles_org)
        print "Thanks for playing"

        again = raw_input("Would you like to play again? Enter y/n: ")

        if again == "n":
            print ("Thanks for Playing!")
            return
        elif again == "y":
            print ("Lets play again..")
        else:
            print ("You should enter either \"y\" or \"n\".")

if __name__ == "__main__":
    main()