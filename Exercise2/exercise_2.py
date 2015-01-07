def main():
    while True:
        gas_amount = raw_input("Please enter the number of gallons of gasoline: ")
        while not gas_amount.isdigit() or gas_amount == "0":
                if gas_amount == "0":
                        gas_amount = raw_input("Cannot determine using 0. Try another number: ")
                else:
                        gas_amount = raw_input("That's not a number. Try again: ")

        org_gas = int(gas_amount)
        equiv = org_gas * 3.7654
        barrel = org_gas / 19.5
        co2 = org_gas ** 20.0

        print "Original number of gallons is: ", org_gas
        print "%s gallons is the equivalent of %s liters" % (org_gas, equiv)
        print "%s gallons of gasoline requires %s barrels of oil" % (org_gas, barrel)
        print "%s gallons of gasoline produces %s pounds of CO2" % (org_gas, co2)
        print (org_gas), "gallons of gasoline is energy equivalent to", (co2), "gallons of ethanol"
        print (org_gas), "gallons of gasoline requires", (co2), "US dollars"

        again = raw_input("Would you like to calculate again? Enter y/n: ")

        if again == "n":
            print ("Thanks for Playing!")
            return
        elif again == "y":
            print ("Lets start over.")
        else:
            print ("You should enter either \"y\" or \"n\".")

if __name__ == "__main__":
    main()