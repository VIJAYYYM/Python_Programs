def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [num ** 2 for num in numbers if num % 2 == 0]

double = lambda x: x * 2
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(double, numbers))

person = {
    "name": "VIJAY",
    "age": 22,
    "occupation": "Software Engineer"
}

print(person.get("name", "Unknown"))

for key, value in person.items():
    print(f"{key}: {value}")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Working with file I/O
file_path = "data.txt"
with open(file_path, "r") as file:
    content = file.read()
    print(content)

# Using the datetime module to work with dates
from datetime import datetime

current_date = datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time:", formatted_date)
