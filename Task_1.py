# Вывести на экран сумму четных чисел от 1 до 100 включительно, используя функцию range()

a = 0
for x in range(0, 101,2):
    a = a + x

print("Сумма четных чисел от 1 до 100 =", a)
