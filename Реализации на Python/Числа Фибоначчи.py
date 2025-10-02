def fibonacci_recursive(n):
    """Рекурсивное вычисление чисел Фибоначчи"""
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    """Итеративное вычисление чисел Фибоначчи"""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def fibonacci_sequence(n):
    """Генерация последовательности Фибоначчи"""
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:n]

# Пример использования
if __name__ == "__main__":
    print("Fibonacci Recursive(10):", fibonacci_recursive(10))
    print("Fibonacci Iterative(10):", fibonacci_iterative(10))
    print("Fibonacci Sequence(10):", fibonacci_sequence(10))
