#If the number is a multiple of 3, print "Fizz"; 
# if 5, print "Buzz"; 
# if both, "FizzBuzz"; 
# otherwise, the number.
#Try writing just the skeleton of the loop for i in range(1, 51): and let the AI suggest the rest. Cursor probably knows this popular problem and will autocomplete much of it for you.



for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)