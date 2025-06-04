import cProfile  # профилировщик


def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        # Искусственный замедлитель.
        # sorted([a, b, a + b])
    return a


def main():
    n = 100000
    fib_iterative(n)


if __name__ == '__main__':
    cProfile.run('main()')