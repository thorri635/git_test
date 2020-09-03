num_int_prev = 0
num_int = 1
while num_int >= 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int > num_int_prev:
        max_int = num_int
    num_int_prev = num_int

# Fill in the missing code
print("The maximum is", max_int)    # Do not change this line
