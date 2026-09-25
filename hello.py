print("Hello, World!")


def add_numbers(x, y):
    return x + y

result = add_numbers(5, 3)
print(result)

def sayHello(name):
    return f"Hello, {name}!"

print(sayHello("Alice"))


def multiply_numbers(a,  b):
    return a * b

result = multiply_numbers(4, 6)
print(result)

age= 25
print(type(age))

str="Hello"
print(type(str))

messages ="""This is a multi-line string.
It can span multiple lines.
This is the end of the multi-line string."""

print(messages)

isMale = True
print(type(isMale))

if(isMale):
    print("You are male.")
else:
    print("You are not male.")



# numbers=[1, 2, 3, 4, 3,  5]
# numbers.append(6)
# numbers.insert(2, 10)
# numbers.remove(3)
# for num in numbers:
#     print(num)
# print(numbers)


objects = {"name": "Alice", "age": 30, "city": "New York"}
print(objects.get("name"))


cordinates = (10.0, 20.0)
# cordinates[0] = 15.0  # This will raise an error because tuples are immutable
print(cordinates[0])


input_string = input("Enter your age: ")
if input_string.isdigit():
    age = int(input_string)
    age >= 18
    print("You are an adult.")
else:
    print("Invalid input. Please enter a valid age.")    




# filter_odd_numbers = [num for num in nums if num % 2 == 0]

# print(filter_odd_numbers)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#  covert into {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81}
squared_nums = {num: num**2 for num in nums}
print(squared_nums)

student = {"name": "Farhan", "age": 25, "city": "Hyderabad"}

# print all keys and values in the dictionary
for key, value in student.items():
    print(f"{key}: {value}")