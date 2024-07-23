def calculate_x(x1, x2, x21, l, r21):
    return (x1 + x2 + (x21 / l) * r21) / 2

# Example usage
x1 = 10
x2 = 20
x21 = 30
l = 5
r21 = 2

x = calculate_x(x1, x2, x21, l, r21)
print("The value of x is:", x)
