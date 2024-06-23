def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        print("Not divisible by zero")
    else:
        return a / b

print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")

while True:
    choice = input("Enter your choice: ")
    if choice in ('1', '2', '3', '4'):
        n1 = float(input("First number: "))
        n2 = float(input("Second number: "))
        if choice == '1':
            print(n1, "+", n2, "=", add(n1, n2))
        elif choice == '2':
            print(n1, "-", n2, "=", sub(n1, n2))
        elif choice == '3':
            print(n1, "*", n2, "=", mul(n1, n2))
        elif choice == '4':
            print(n1, "/", n2, "=", div(n1, n2))
    else:
        print("Invalid input")
    
    again = input("Do you want to continue? (y/n): ")
    if again.lower() != 'y':
        break