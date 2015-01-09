from sys import exit


def main():
    while True:
        gas_amount = raw_input("\nPlease enter the number of gallons of gasoline: ")
        while not gas_amount.isdigit() or gas_amount == "0":
                if gas_amount == "0":
                        gas_amount = raw_input("Cannot determine using 0. Try another number: ")
                else:
                        gas_amount = raw_input("That's not a number. Try again: ")

        org_gas = int(gas_amount)
        equiv = org_gas * 3.7654
        barrel = org_gas / 19.5
        co2 = org_gas * 20.0
        btu_from_gas = org_gas * 115000
        btu_from_ethanol = 75700.
        ethanol_gas_equivalent = btu_from_gas / btu_from_ethanol
        dollars = org_gas * 4.00

        print "\nOriginal number of gallons is: %s" % org_gas
        print "%s gallons is the equivalent of %s liters" % (org_gas, equiv)
        print "%s gallons of gasoline requires %s barrels of oil" % (org_gas, barrel)
        print "%s gallons of gasoline produces %s pounds of CO2" % (org_gas, co2)
        print "%s gallons of gasoline is energy equivalent to %s gallons of ethanol" % (org_gas, ethanol_gas_equivalent)
        print "%s gallons of gasoline requires %s US dollars" % (org_gas, dollars)

        again = raw_input("\nWould you like to calculate again? Enter yes or no: ")

        if again == "no":
            print ("\nThanks for calculating! It's been mathematical!\n")
            exit()
        elif again == "yes":
            print ("\nLets retry with a new amount.")
        else:
            raw_input("\nYou should enter either yes or no. Would you like to calculate again?: ")

if __name__ == "__main__":
    main()