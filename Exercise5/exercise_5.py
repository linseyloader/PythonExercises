import random
import string

max_length_of_string = 8
# max_length_of_string = int(raw_input("What is the maximum length of the 10 lines of random letters?"))
characters = []


file_5 = open("project_5.dat", 'w')
for count in range(0,10):
    length = random.randint(2,max_length_of_string)
    random_string = ''.join([random.choice(string.ascii_letters) for n in xrange(length)])
    # characters.append(random_string)
    characters[:0]=random_string
    file_5.write(random_string)


file_5.close()
file_5 = open('project_5.dat', 'r')


def letter_counter(case):

    if case == "upper":
        all_the_letters = string.ascii_uppercase
    else:
        all_the_letters = string.ascii_lowercase
        letter_on_counter = 0
    for alphabet in all_the_letters:
        for letter in characters:
            if letter == alphabet:
                letter_on_counter = letter_on_counter + 1
        if letter_on_counter == 1:
            print "There is %s %s" %(letter_on_counter, alphabet)
        elif letter_on_counter >1:
            print "There are %s %s's" %(letter_on_counter, alphabet)

        letter_on_counter = 0

letter_counter("upper")

letter_counter("lower")

print file_5
file_5.close()