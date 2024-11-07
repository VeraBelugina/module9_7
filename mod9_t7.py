def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        for n in range(2, res // 2):
            if res % n == 0:
                print(f'Простое')
            else:
                print(f'Составное')
            return res
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
