# Есть список numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
# Вывести все нечетные числа больше 50, используя функцию filter().

numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]


def odd_numb(x):
    if x > 50:
        if (x % 2) != 0: return 1
    else:
        return 0


print(list(filter(odd_numb, numbers)))
