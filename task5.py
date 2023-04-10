def first(n):
    if n == 1:
        return n
    elif n > 0:
        return n + first(n-1)

number = int(input('Введите натуральное число n: '))

print('1+2+...+n = ', first(number))
second = number * (number + 1) / 2
print('n * (n + 1) / 2 =', second)