
value=input("Enter a number:     ")

try:
    value = int(value)
    print(f"You entered the number: {value}")

    value= 10 // value
    print(f"Result of division: {value}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: tum 0 se divide nahi kar sakte.")



