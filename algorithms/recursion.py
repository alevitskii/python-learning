def find_factorial_recursive(number):
    return number * find_factorial_recursive(number - 1) if number > 1 else number


def find_factorial_iterative(number):
    result = 1
    for n in range(2, number + 1):
        result *= n
    return result


def fibonacci_iterative(n):
    if n < 2:
        return n
    first, second = 1, 1
    counter = 2
    while counter < n:
        first, second = second, first + second
        counter += 1

    return second


def fibonacci_recursive(n):
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2) if n >= 2 else n


if __name__ == "__main__":
    # print(find_factorial_recursive(3))
    # print(find_factorial_iterative(3))

    print(fibonacci_iterative(10))
    print(fibonacci_recursive(10))
