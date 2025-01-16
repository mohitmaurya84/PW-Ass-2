### 1. **Print "Hello, World!"**
print("Hello, World!")

### 2. **Display name and age**
name = "John"
age = 25
print("Name:", name)
print("Age:", age)

### 3. **Print all pre-defined keywords in Python using the `keyword` library**
import keyword
print(keyword.kwlist)

### 4. **Check if a given word is a Python keyword**
import keyword

word = input("Enter a word: ")
if keyword.iskeyword(word):
    print(f"{word} is a Python keyword.")
else:
    print(f"{word} is not a Python keyword.")

### 5. **Create a list and tuple in Python, demonstrate immutability and mutability**
# List (mutable)
my_list = [1, 2, 3]
my_list[0] = 10  # Changing an element
print("Modified List:", my_list)

# Tuple (immutable)
my_tuple = (1, 2, 3)
try:
    my_tuple[0] = 10 # Trying to change an element
except TypeError:
    print("Cannot modify a tuple!")

### 6. **Function to demonstrate mutable and immutable arguments**
def modify_elements(mutable_arg, immutable_arg):
    mutable_arg.append(4)  # Modifies the mutable object
    immutable_arg += 1  # Doesn't modify the immutable object, creates a new one
    print("Modified mutable argument:", mutable_arg)
    print("Modified immutable argument:", immutable_arg)

# Calling the function
my_list = [1, 2, 3]
my_number = 10
modify_elements(my_list, my_number)

### 7. **Use of logical operators**
x = True
y = False

# AND operator
print(x and y)

# OR operator
print(x or y)

# NOT operator
print(not x)

### 8. **Convert user input from string to integer, float, and boolean**
user_input = input("Enter a value: ")

# Convert to integer, float, and boolean
int_value = int(user_input)
float_value = float(user_input)
bool_value = bool(user_input)

print("Integer:", int_value)
print("Float:", float_value)
print("Boolean:", bool_value)

### 9. **Demonstrate type casting with list elements**
my_list = [1, 2.5, "3"]
casted_list = [int(x) if isinstance(x, float) else x for x in my_list]
print("Casted list:", casted_list)

### 10. **Check if a number is positive, negative, or zero**
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

### 11. **Print numbers from 1 to 100 using a for loop**
for i in range(1, 101):
    print(i)

### 12. **Sum of all even numbers between 1 and 500**
sum_even = sum([num for num in range(1, 501) if num % 2 == 0])
print("Sum of even numbers between 1 and 500:", sum_even)

### 13. **Reverse a string using a while loop**
string = input("Enter a string: ")
reversed_string = ""
i = len(string) - 1
while i >= 0:
    reversed_string += string[i]
    i -= 1
print("Reversed string:", reversed_string)

### 14. **Calculate the factorial of a number using a while loop**
num = int(input("Enter a number to calculate factorial: "))
factorial = 1
while num > 1:
    factorial *= num
    num -= 1
print("Factorial:", factorial)
