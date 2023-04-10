def count(n, even=0, odd=0):
    if n == 0:
        print(f"Количество четных и нечетных цифр в числе равно: ({even}, {odd})")
    else:
        cur_n = n % 10
        n = n // 10
        if cur_n % 2 == 0:
            even += 1
        else:
            odd += 1
        return count(n, even, odd)


n = int(input("Введите число: "))
count(n)
