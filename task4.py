def elements(n):
    summ = 0
    ratio = 1
    for i in range(n):
        summ += ratio
        ratio /= -2
    return summ


number = int(input('Введите количество элементов: '))

print(elements(number))
