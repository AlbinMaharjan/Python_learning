a = float(input("Enter a number1: "))
b = float(input("Enter a number2: "))

print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")
print("Enter 5 for modulo")
c = int(input("Enter choice: "))

def switch_case(c):
    if c == 1:
        return a + b
    elif c == 2:
        return a - b
    elif c == 3:
        return a * b
    elif c == 4:
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif c == 5:
        return a % b
    else:
        return "Invalid choice"

result = switch_case(c)
print(result)