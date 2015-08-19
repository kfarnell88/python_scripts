from time import sleep

grocery_list = ["apples", "strawberries", "bananas", "plums"]
grocery = {"apples" : 1.25, "strawberries" : 1.75, "plums" : 1.50, "bananas" : 2.00,}

print "You only have $5 and your grocery list is as follows:"
print grocery_list
sleep(4)
print "The prices of the items you need are as follows:"
print grocery
sleep(4)
print "Here is the order of the fruit from most expensive to least expensive:"
print grocery_list[2]
print grocery_list[1]
print grocery_list[3]
print grocery_list[0]
sleep(4)
print "You decide to buy the following apples, strawberries, and 2 plums. Your total is as follows:"
print grocery["apples"] + grocery["strawberries"] + grocery["plums"] * 2
sleep(4)
print "You are over budget, so you put one plum back. Your new total is:"
print grocery["apples"] + grocery["strawberries"] + grocery["plums"]
