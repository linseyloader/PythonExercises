integer_one = raw_input("Please enter the first integer: ")
while not integer_one.isdigit():
    integer_one = raw_input ("That is not a number. Try again: ")

integer_two = raw_input("Please enter the second integer: ")
while not integer_two.isdigit() or integer_two == "0":
    if integer_two == "0":
        integer_two = raw_input("Cannot determine using 0. Try another number: ")
    else:
        integer_two = raw_input("That's not a number. Try again: ")

int_one = int(integer_one)
int_two = int(integer_two)

add = int_one + int_two
subtract = int_one - int_two
multiply = int_one ** int_two
divide = int_one / int_two
remainder = int_one % int_two

print "The sum of %s and %s is: %s" % (int_one, int_two, add)
print "The difference of %s and %s is: %s" % (int_one, int_two, subtract)
print "The product %s and %s is: %s" % (int_one, int_two, multiply)
print "The quotient %s and %s is: %s with remainder: %s" % (int_one, int_two, divide, remainder)