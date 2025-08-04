operations = ["+" , "-" , "*" , "/"]

while True:
    try:
        num_1 = float(input("\nEnter first number: ")); num_2 = float(input("\nEnter second number: ")); operation = input("\nEnter a operation(+ , - , * , /): ")
        if operation not in operations:
            raise ValueError()
        break
    except ValueError:
        print("Enter a valid number/operation!")
        pass

if operation == "+": print("\n",num_1 + num_2)
elif operation == "-": print("\n",num_1 - num_2)
elif operation == "*": print("\n",num_1 * num_2)
elif operation == "/" and num_2 != 0: print("\n", num_1 / num_2)


