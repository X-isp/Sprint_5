# import sys
import time


def fib_recursion(n):
    if n <= 1:
        return n
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)


def recursive_function(n):
    if n == 0:
        return 0
    else:
        return recursive_function(n-1) + 1


def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    n = 36

    start_time = time.time()
    print(fib_recursion(n))
    print('Время рекурсивного решения:', time.time() - start_time)

    start_time = time.time()
    print(fib_iterative(n))
    print('Время итеративного решения:', time.time() - start_time)

    # print(recursive_function(1000 - 1))

    # print(sys.getrecursionlimit())
    # # принудительно задать макс. значение глубины рекурсии:
    # # (нужно применять аккуратно, т.к. может произойти переполнение
    # # стека вызовов)
    # sys.setrecursionlimit(10000)
    # print(sys.getrecursionlimit())

    
