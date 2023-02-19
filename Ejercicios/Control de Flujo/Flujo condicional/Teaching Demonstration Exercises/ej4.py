# Challenge exercise.

#-------------------------------------------------------------------------------------

# In this exercise you will encounter nested conditions which we will
# study next class. Can you figure out how it works?
# Remember you can always look for more information on the internet about this topic.
# I would recommend you checking this link
# https://www.geeksforgeeks.org/nested-if-statement-in-python/

#-------------------------------------------------------------------------------------

# The following code ask for a number and classifies it according to this criteria:
#  0 <= x <= 20 --- low
#  20 < x <= 40 --- mid low
#  40 < x <= 60 --- mid
#  60 < x <= 80 --- mid high
#  80 < x <= 100 --- high
#  100 < x --- Invalid
#  x < 0 --- Invalid

# Add to this code so it fulfills the conditions above

num = input("Input a number: ")
if 0 <= num <= 100:
    if num <= 20:
        print("low")
    else:
        if num <= 40:
            print("mid low")

else:
    print("The number you entered is not valid.")