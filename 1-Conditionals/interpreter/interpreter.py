x, y, z = input("ask a math question: ").split()

x = int(x) # Convert the first part to an integer
z = int(z) # Convert the third part to an integer

# Perform the calculation based on the value
if y == "+":
    result = (x + z)
elif y == "-":
    result = (x - z)
elif y == "*":
    result = (x * z)
elif y == "/":
    result = (x / z)
else:
    print("Error")
# Print the result formatted to one decimal place .1 means one decimal place
print(f"{result:.1f}")