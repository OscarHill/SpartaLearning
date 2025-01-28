## Notes on the Sparta Global Python Fundamentals Course

### Why Python?
- Python is a flexible and easy programming language, great for beginners
- Used in many fields and industries
- Open-source and multi-platform

### Using Python
- Python can be downloaded [here](https://www.python.org/downloads/)
- And Pycharm (an IDE, where you actually write and run the Python code) [here](https://www.jetbrains.com/pycharm/download/?section=windows)
- Code in python can be commented (so it's just a message, not code that will run) using the hash ("#") symbol
  - As in: `#This is a python comment`

### Python Data Types
- Here are some of the data types in python:
  - Integers and Floats (different kinds of number)
  - Strings (text)
  - Booleans (True or False values)


- Python also has various common mathematical operators:
  - `+` can add two numbers
  - `-` for subtraction
  - `*` for multiplication (not `x`!)
  - `/` for division
  - `%` ("modulo") for finding the remainder
    - (usage: `x % y` gives you the remainder after x is divided by y)


- Strings are text, and they are defined by characters between quotation marks `'` or `"`
  - When we give a string value to python (as in `print("Hello, world")`) then what python "sees" is a list of characters
  - As such we can use the index of each character in a string to just give that character
    - Example: `print("Hello world"[1])` will print just the character "e" (remember indices start at 0 in Python)
  - Python also has methods like `len()` to find the length of a string
    - Example: `print(len("Hello!"))` would print out  `6`


- Booleans are `True` and `False` values, and are useful when doing logic
  - Python comes with various logical operators for comparing things:
    - `==` means "equal to", and checks if the left and right correspond
    - `!=` means "not equal to", and does the opposite
    - `>` and `<` are greater than and less than
    - `>=` and `<=` are greater than or equal to, and less than or equal to
  - Everything in Python is also "truthy" or "falsey", meaning they correspond to either true or false
    - For example, all numbers and strings are `True` apart from `0` and `""` (the empty string) which are `False`
  

### Python Variables
- Variables in Python are ways of organising your data - almost like putting them in boxes
  - The operator `=` is the way that we define a variable
```
a = 4
b = 3 
print(a+b)
```
- This code would output `7`, because we've added two variables that we defined as numbers
- The naming of our variables is important for increasing code readability and comprehensibility - for more look at the [PEP 8 style guide](https://pep8.org/)

### More on Strings
- Strings can be added! (known as "concatenation")
```
firstName = "Howard"
secondName = "Hamlin"
space = " "
print(firstName + space + secondName)
```
- This code would output ```Howard Hamlin```!
- Some other tips:
  - You can turn numbers into strings with the `str()` command - allowing you to concatenate them with other strings
  - In order to print a `"` without it ending the string, you can use the escape character `\` (as in `print("\"Hello there!\", he said.")`)
    - There's lots of methods you can do with strings. For example, `string_name.capitalize()` will capitalize the first letter of a string!
      - For more, have a look at the documentation: https://docs.python.org/3/library/stdtypes.html#string-methods


### Control Flow
- Control flow is the idea in programming languages that we might want to change what code runs based on certain conditions
  - For example, when coding a menu, we might want to program it so that the menu changes when you press a button
- We can implement this in python with `if` statements and logic. Here's a code example for a film rental site:
```python
customer_age = 0

if customer_age < 12:
    print('You can watch U and PG films')
elif customer_age < 15:
    print('You can watch U, PG, and 12 films')
else:
    print('You can watch any film')
```
- `if` sets up the first condition for our control flow. If the condition isn't satisfied, then it will go to the next line
- `elif` (short for "else if") gives an alternative `if` for when the first condition isn't met.
- `else` is a catch-all for all the other conditions
- Another thing Python has are the logical connectors `and` and `or`.
  - These are really useful to add extra conditions to `if` statements

### Collections
- Python has a few different collections, which are data types that store variables inside them
- We'll look at lists and dictionaries:
  - Lists are created with square brackets: `example_list = [1, True, "string"]`
    - Lists can be any length, store any data type, and can store different kinds of data all in the same list
  - We can access individual items in the list using the index: `print(example_list[2])` would print out `string`
  - Index tip: you can start counting from the end of the list with negative numbers. The index `[-1]` gives us the last item
  - There are lots of methods associated with lists! Click [here](https://docs.python.org/3/library/stdtypes.html#list) for more
    - `example_list.append(new_item)` adds a new item to the end of the list
    - `example_list.pop()` removes the last item from the list - or if you give it an index, it takes out that item
  - Dictionaries are a bit more complex - they store items using "key-value pairs"
    - You can think of them like a real dictionary - the "key" would be the word, and the "value" is the definition
    - You can't have two keys be the same, but you can have values as the same
    - The keys can only be a single data type like a string or a number, but the values can be lists or even other dictionaries!
    - Here's how you set up a dictionary: `phonebook = {"Howard": "230423074", "Jimmy": "239847897"}`
    - Dictionary methods include `dict.keys()` to print out all the keys, 'dict.values()' for the values, and `dict.pop()` to get rid of an item
  
    
### Loops
- Loops are a way to repeat your code a certain number of times!
  - The simplest loop type is `while`, formatted as so:
```python
a = 0
while a < 10:
    print(a)
    a = a + 1
```
- This is a simple loop which will count from 0 to 9. 
  - The `while` is always followed by some logical condition.
    - The program will check the condition, run the code, and then return to the top - if the condition is still met then it will go again
  - You can even write `while True` to make a loop that goes infinitely! 
  - This might not be a good thing though - usually in the `while` loop you put in a way for the program to stop, such as a counter that reaches a limit and stops the code
  - Don't forget the colon after the `while` statement!
- We also have the `for` loop
  - `for` loops are a way to iterate over some kind of series of things
  - for example, `for item in list` will repeat the code indented beneath it a number of times equal to the number of items in the list
- Let's look at an example:
```python
customers = {
  "name": "Howard",
  "age": "47",
  "workplace": "HHM"
}

for item in customers.values():
  print(item)
```
- This code goes through all the values in the `customers` dictionary, and prints them off one by one

### Functions
- Functions are a way of neatly bundling our code, useful for when we want to reference it later.
- Here's an example:
```python
def number_adding(a, b):
    return a + b

my_age = 45
your_age = 44

print(number_adding(my_age, your_age))
```
- This code will return `89`
- Functions are always created by typing `def <function_name>(parameters):`
  - You can call your function whatever you want, and give it as many parameters as you want - even none!
