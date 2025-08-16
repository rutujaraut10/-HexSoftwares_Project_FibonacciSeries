# Fibonacci Series using Recurrence Relation

def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example: First 10 Fibonacci numbers
n_terms = 100
print(f"First {n_terms} Fibonacci numbers:", fibonacci(n_terms))


