from time import sleep

def my_story():
    enter_room_1()
def enter_room_1():
    print "Welcome to room 1"
    sleep(1)
    print "You've found the weapons cache!"
    sleep(3)
    print "Which weapon would you like?"
    sleep(3)
    print "Select a number: "
    print "  1. Machete" + " 2.Grenade" + " 3. AR-15"
    print "  4. 9mm pistol" + " 5. Flame thrower"

    answer = int(raw_input("Your answer "))

    if answer == 1:
        print "Machete don't text"
    elif answer == 2:
        print "We ride at dawn!"
    elif answer == 3:
        print "Those will be illegal soon."
    elif answer == 4:
        print "You'll shoot your eye out, kid"
    elif answer == 5:
        print "Do you know how to use that thing?"
        sleep(4)
        print "..."
        print "nevermind."
    else:
        print "Invalid response. Please type a number."

    leave_room()

def leave_room():
    sleep(2)
    print "You've now entered the garage."
    sleep(2)
    print " 1. Tank" + " 2. Bicycle" + " 3. Dodge Charger"

    answer = int(raw_input("Select a vehicle "))

    if answer == 1:
        print "There are no keys."
    elif answer == 2:
        print "The tires are flat."
    elif answer == 3:
        print "You left your license at home."
    else:
        print "Invalid response. Please type a number."

    leave_room2()


def leave_room2():
    answer = raw_input("Do you turn left or right out of the garage? (right or left) ")

    if answer == "left":
        print "You hit a land mine."
        sleep(2)
        print "The end."
    elif answer == "right":
        print "There are miles to go before we sleep."
        sleep(2)
        print "byeeee"
    else:
        print "Invalid response."


my_story()
