def checkoutD(list = []):
    for i in range(len(list)):
        line = ''
        for j in range(len(list[i])):
            line += list[i][j]+' '
            #print(list[i][j])
        print(line, '\n')

list = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-'],
]


ind = 1
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
    if ind % 2 == 0: # Крестик
        list[answer[0]][answer[1]] = 'x'
    elif ind % 2 == 1 # Нолик
        list[answer[0]][answer[1]] = '0'

    ind += 1

print(answer.split())



checkoutD(list)

#print(list)