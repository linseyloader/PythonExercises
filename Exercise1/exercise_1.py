nu = raw_input("Please enter the first integer: ")
while not nu.isdigit() or nu == "0":
    if nu == "0":
        nu = raw_input("Cannot determine using 0. Try another number: ")
    else:
        nu = raw_input("That's not a number. Try again: ")
nm = raw_input("Please enter the second integer: ")
while not nm.isdigit() or nm == "0":
    if nm == "0":
        nm = raw_input("Cannot determine using 0. Try another number: ")
    else:
        nm = raw_input("That's not a number. Try again: ")
nu_value = int(nu)
nm_value = int(nm)
print "The sum of", (nu_value), "and", (nm_value), "is:", (nu_value + nm_value)
print "The difference of", (nu_value), "and", (nm_value), "is:", (nu_value - nm_value)
print "The product", (nu_value), "and", (nm_value), "is:", (nu_value * nm_value)
print "The quotient", (nu_value), "and", (nm_value), "is:", (nu_value / nm_value), "with remainder:", (nm_value % nu_value)