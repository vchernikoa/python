#Есть словарь dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
#Составить из него новый словарь, содержащий только те элементы, у которых значение больше или равно 3.

dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
ls = {}

for i in dict:
    if dict[i] >= 3:
        ls[i] = dict[i]

print(ls)