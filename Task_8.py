'''
Необходимо считать любой текстовый файл на вашем ПК (можно создать новый) и создать на его основе новый файл,
где содержимое будет записано в обратном порядке. В конце программы вывести на экран оба файла - старый в
неизменном виде и новый в обратном порядке.
'''

with open('calendar.txt', 'r') as f:
    text = f.readlines()
    for x in range(0, len(text)):
        text[x] = text[x].split()[::-1]

with open('new_file.txt','w') as new:
    for x in text:
        x = ' '.join(x)
        new.write(x)

with open('calendar.txt', 'r') as f:
    print(f.readlines())

with open('new_file.txt', 'r') as f:
    print(f.readlines())
