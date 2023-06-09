def fibonacci(n):

    if n <= 0:

        return "Invalid input. Please enter a positive integer."

    elif n == 1:

        return 0

    elif n == 2:

        return 1

    else:

        fib_sequence = [0, 1]

        for i in range(2, n):

            next_num = fib_sequence[i-1] + fib_sequence[i-2]

            fib_sequence.append(next_num)

        return fib_sequence[-1]

# Example usage

number = 10

fibonacci_number = fibonacci(number)

print(f"The Fibonacci number at position {number} is: {fibonacci_number}")

