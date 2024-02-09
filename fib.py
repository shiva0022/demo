code = """from functools import lru_cache
from time import perf_counter


@lru_cache(maxsize=3, typed=None)
def fib(num: int) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fib(num-1) + fib(num-2)


try:
    number = int(input('Enter a number : '))

    if number < 0:
        raise ValueError

    start = perf_counter()
    fib_series = [fib(i) for i in range(number)]
    end = perf_counter()
    print(f'Fibonacci series for given number {number} is : {fib_series}')
    print(f'Time taken : {(end-start) * 1000: .2f}ms')
    print(fib.cache_info())

except ValueError as ve:

    print('fibonacci series for negative numbers does not exist')
"""

exec(code)
