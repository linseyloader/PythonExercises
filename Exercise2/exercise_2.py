gas = input("Please enter the number of gallons of gasoline: ")
org_gas = int(gas)
equiv = 3.7654
barrel = 19.5
co = 20.0
print "Original number of gallons is:", (gas)
print (org_gas), "gallons is the equivalent of", (org_gas * equiv), "liters"
print (org_gas), "gallons of gasoline requires", (org_gas / barrel), "barrels of oil"
print (org_gas), "gallons of gasoline produces", (org_gas * co), "pounds of CO2"
print (org_gas), "gallons of gasoline is energy equivalent to", (org_gas * co), "gallons of ethanol"
print (org_gas), "gallons of gasoline requires", (org_gas * co), "US dollars"
print "Thanks for playing"
