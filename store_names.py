f = open('document.txt', 'a')
f.write(raw_input("First Name: " + "\n"))
f.write(raw_input("LAST NAME: "))
f.write(raw_input("AGE: "))


with open("document.txt") as f:
    for line in f:
        print line + "\n"
