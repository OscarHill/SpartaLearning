print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def find_divisors(num):
    res = []
    for i in range(1,num+1):
        if num % i == 0:
            res.append(i)
    return res

print(find_divisors(6))


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def is_a_factor(x, y):
    x_factors = find_divisors(x)
    y_factors = find_divisors(y)
    if x in y_factors or y in x_factors:
        return True
    else:
        return False

print(is_a_factor(4,187))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
def pos_in_alphabet(letter):
    return alphabet.index(letter) + 1

print(pos_in_alphabet('e'))


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def id_gen(name):
    res = ""
    for i in name.lower():
        res = res + str(pos_in_alphabet(i))
    return res

print(id_gen("Howard"))

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

def turn_id_to_pass(id):
    id_value = 0
    for i in id:
        id_value += int(i)
    return int(id) - id_value

print(turn_id_to_pass(id_gen("Howard")))

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def is_prime(number):
    if len(find_divisors(number)) == 2:
        return True
    else:
        return False

print(is_prime(2707))


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
def is_prime_better(number):
    if type(number) != int:
        return "That's not a number!"
    elif len(find_divisors(number)) == 2:
        return True
    else:
        return False

print(is_prime_better("Hello!"))

# -------------------------------------------------------------------------------------- #






