# 1. Write a function that calculates the factorial of a given integer.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 2. Write a function that checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: ###n is divisible by i, its not prime i = 11, n = 11
            return False
    return i

# 3. Write a function that reverses a string.
def reverse_string(input_string):
    return input_string[::-1]

# 4. Write a function that finds the maximum of three numbers.
def find_max_of_three(num1, num2, num3):
    return max(num1, num2, num3)

# 5. Write a function that counts the number of words in a sentence.
def count_words(sentence):
    words = sentence.split()
    return len(words)

# 6. Write a function that calculates the area of a rectangle.
def calculate_rectangle_area(length, width):
    return length * width

# 7. Write a function that converts a temperature in Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 8. Write a function that generates a list of Fibonacci numbers up to n.
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# 9. Write a function that checks if a string is a palindrome.
def is_palindrome(input_string):
    clean_string = ''.join(input_string.split()).lower()
    print('this is the argument',clean_string)
    return clean_string == clean_string[::-1]

# 10. Write a function that calculates the mean of a list of numbers.
def calculate_mean(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# # Testing the functions
# print(factorial(5))
# print(is_prime(11))
# print(reverse_string("hello"))
# print(find_max_of_three(7, 3, 9))
# print(count_words("This is a sample sentence."))
# print(calculate_rectangle_area(4, 5))
# print(celsius_to_fahrenheit(25))
# print(generate_fibonacci(50))
print(is_palindrome("A P P L E"))
# print(calculate_mean([1, 2, 3, 4, 5]))
