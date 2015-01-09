from sys import exit


def main():
    while True:
        miles = raw_input("\nPlease enter a speed in miles/hours: ")
        miles_org = int(miles)

        yards_mile = 1760
        meters_hour = miles_org * 1609.34
        feet_hour = miles_org * 5280

        meters_day = meters_hour * 24
        barleycorns_day = meters_day * 117.647

        yards_hour = yards_mile * miles_org
        furlongs_hour = yards_hour / 220
        furlongs_day = furlongs_hour * 24
        furlongs_week = furlongs_day * 7

        mach = (feet_hour / 60 / 60) / 1130

        psl = ((meters_hour / 60 / 60) / 299792458) * 100

        print "\nOriginal speed in mph:", (miles_org)
        print "Converted to barleycorn/day is:", (barleycorns_day)
        print "Converted to furlongs/fornight is:", (furlongs_week * 2)
        print "Converted to Mach number is:", (mach)
        print "Converted to the percentage of the speed of light is", (psl)
        print "Thanks for playing"

        again = raw_input("\nWould you like to determine using another number? Enter yes or no: ")

        if again == "no":
            print ("\nGoodbye.")
            exit()
        elif again == "yes":
            print ("\nLets retry with a new amount.")
        else:
            raw_input("\nYou should enter either yes or no. Try again: ")

if __name__ == "__main__":
    main()