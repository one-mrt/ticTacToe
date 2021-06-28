
# Вывод поля игры в консоль
def output_result(list = []):
    for i in range(len(list)):
        line = ' '
        print(line.join(list[i]))

# Ввод данных - Ход игрока
def inputData(gamer):
    answer = input(f'Ход игрока {gamer} ')
    return answer

# Проверка по горизонтали
def is_horizontal(result):
    x = len(result)

    for i in range(x):
        y = len(result[i])
        victory = 1

        for j in range(y):
            if j < (y-1):
                if result[i][j] == result[i][j+1]:
                    if result[i][j] != '-' and result[i][j+1] != '-':
                        victory += 1

        if victory == y:
            return result[i][j]

        victory = 1

    return False

# Проверка по вертикали
def is_vertical(result):
    x = len(result)

    for i in range(x):

        y = len(result[i])
        victory = 1

        for j in range(y):
            if j < (y-1):
                if result[j][i] == result[j+1][i]:
                    if result[j][i] != '-':
                        if result[j+1][i] != '-':
                            victory += 1
        
        if victory == y:
            return result[j][i]

        victory = 1

    return False

# Проверка по левой диагонали
def is_diagonal_left(result):
    x = len(result)
    victory = 1

    for i in range(x):
        if i < (x-1):
            if result[i][i] == result[i+1][i+1]:
                if result[i][i] != '-':
                    if result[i+1][i+1] != '-':
                        victory += 1

    if victory == x:
        return result[i][i]

    return False

# Проверка по правой диагонали
def is_diagonal_right(result):
    x = len(result)
    victory = 1

    for i in range(x):
        y = len(result[i]) - 1 - i;

        if i < (x-1):
            if result[i][y] == result[i+1][y-1]:
                if result[i][y] != '-':
                    if result[i+1][y-1] != '-':
                        victory += 1
    
    if victory == x:
        return result[i][y]

    return False

# Вывод подсказки
def help():
    print(
        """
            Введите две координаты от нуля до двух цифрами через пробел
            куда хотите поставить крестик или нолик
            --0 1 2
            0 - - -
            1 - - -
            2 - - -
        """
    )

# Сгенерировать игровое поле
def generateField():
    return [
        ['-','-','-'],
        ['-','-','-'],
        ['-','-','-'],
    ]

# Проверка игры на ничью
def is_empty_cage(result):
    x = len(result)
    empty = 0

    for i in range(x):
        y = len(result[i])
        for j in range(y):
            if(result[i][j] == '-'):
                empty += 1

    if empty == 1:
        return True
    else:
        return False

# Повторить или закончить игру
def nextGame(ind, field):
    next = input('Повторить? Y-Да, N-Нет - ')
    if next.upper != 'Y':
        return False;
    elif next.upper == 'Y':
        ind = 1
        field = generateField()
        help()

field = [   # Игровое поле
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-'],
]

ind = 1 # Счетчик ходов
# Игроки
gamer = {
    'x' : 'Крестик',
    'o' : 'Нолик'
}
currentGamer = gamer['x'] # Игрок
move = 'x'          # Ход


# Отформатировать входные данные
def formatData(string, listS):
    gapString = ''
    for k in range(len(listS)):
        if len(string) > 0:
            print(k, string, gapString)
            for i in range(len(string)):
                if(k != string[i]):
                    gapString = string.replace(string[i], '')

    return gapString


field = generateField()
help()

while True:
    if ind % 2 == 1:
        currentGamer = gamer['x']
        move = 'x'
    elif ind % 2 == 0:
        currentGamer = gamer['o']
        move = 'o'

    answer = inputData(currentGamer)
    answer = formatData(answer, field)
    if len(answer) == 2:
        answer[0] = int(answer[0])
        answer[1] = int(answer[1])
        coordinate = field[answer[0]][answer[1]]

        if coordinate == '-':
            field[answer[0]][answer[1]] = move
            ind += 1
        else:
            print('Это поле занято повторите ход')

        output_result(field)

        horizontal = is_horizontal(field)
        vertical = is_vertical(field)
        diagonal_left = is_diagonal_left(field)
        diagonal_right = is_diagonal_right(field)
        draw = is_empty_cage(field)
        victory = horizontal or vertical or diagonal_left or diagonal_right

        if victory:
            print("Победил игрок", gamer[victory])
            if not nextGame(ind,field):
                break
        elif draw:
            print('Победитель не выявлен!')
            if not nextGame(ind,field):
                break
    else:
        print('Повторите ввод!')