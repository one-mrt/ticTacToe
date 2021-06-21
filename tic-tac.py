def checkoutD(list = []):
    for i in range(len(list)):
        line = ''
        for j in range(len(list[i])):
            line += list[i][j]+' '
            #print(list[i][j])
        print(line)

list = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-'],
]

while True:
    answer = input(
        """
            Введите две координаты от нуля до двух цифрами через пробел
            куда хотите поставить крестик или нолик
            0 1 2
            0 - - -
            1 - - -
            2 - - -
        """
    )

print(answer.split())



checkoutD(list)

print(list)