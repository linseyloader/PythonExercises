try:
    f = open("filename", "a")
    for line in f:
            print line
    f.close()
except IOError: