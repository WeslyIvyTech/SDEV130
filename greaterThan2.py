# Define the function greaterThan that compares two numbers
def greaterThan(x, y):
    if x > y:
        return True
    else:
        return False


# Test with another set of values
a = 10
b = 6

# Call the function and store the result
result = greaterThan(a, b)

# Print the output
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result))

