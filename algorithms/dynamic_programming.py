def fibonacci_wrapper():
    cache = {}

    def fib(n):
        if n in cache:
            return cache[n]
        if n < 2:
            return n

        cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    return fib


def fibonacci_bottom_up(n):
    result = [0, 1]

    for i in range(2, n + 1):
        result.append(result[i - 2] + result[i - 1])

    return result[-1]


if __name__ == "__main__":
    fibonacci = fibonacci_wrapper()
    print(fibonacci(10))

    print(fibonacci_bottom_up(10))
