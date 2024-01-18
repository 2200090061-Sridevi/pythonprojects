def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


number_to_factorial = 5
result = factorial(number_to_factorial)
print(f"The factorial of {number_to_factorial} is: {result}")
