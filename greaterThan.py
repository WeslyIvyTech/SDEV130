# Define the function greaterThan that compares two numbers
def greaterThan(x, y):
    if x > y:
        return True
    else:
        return False

# Main section of the program
a = 2
b = 3

# Call the function and store the result
result = greaterThan(a, b)

# Print the output
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))



