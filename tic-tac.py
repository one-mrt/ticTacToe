def output_result(list_field = []):
    """
        Вывод поля игры в консоль
    """
    for i in range(len(list_field)):
        line = ' '
        print(line.join(list_field[i]))


def input_data(gamer):
    """
        Ввод данных - Ход игрока
    """
    answer = input(f'Ход игрока {gamer} ')
    return answer


def is_horizontal(result):
    """
        Выполняет проверку возможности победы по горизонтали
    """
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


def is_vertical(result,probability):
    """
        Выполняет проверку возможности победы по вертикали
    """
    x = len(result)
    empty = 0

    for i in range(x):

        y = len(result[i])
        victory = 1

        for j in range(y):
            if j < (y-1):
                if result[j][i] == result[j+1][i]:
                    if result[j][i] != '-':
                        if result[j+1][i] != '-':
                            victory += 1
                elif result[j][i] == '-':
                    empty += 1
        
        if victory == y:
            return result[j][i]
        elif victory == (y-1) and empty == 1:
            probability['victory'] = True

    return False


def is_diagonal_left(result):
    """
        Выполняет проверку возможности победы по левой диагонали
    """
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


def is_diagonal_right(result):
    """
        Выполняет проверку возможности победы по правой диагонали
    """
    x = len(result)
    victory = 1

    for i in range(x):
        y = len(result[i]) - 1 - i

        if i < (x-1):
            if result[i][y] == result[i+1][y-1]:
                if result[i][y] != '-':
                    if result[i+1][y-1] != '-':
                        victory += 1
    
    if victory == x:
        return result[i][y]

    return False


def is_empty_cage(result):
    """
        Выполняет проверку игры на ничью
    """
    x = len(result)
    empty = 0

    for i in range(x):
        y = len(result[i])

        for j in range(y):
            if result[i][j] == '-':
                empty += 1

    if empty == 1:
        return True
    else:
        return False


def format_data(string, list_field):
    """
        Выполняет обработку ввода пользователя
    """
    gap_string = []
    x = len(string)

    for i in range(x):
        for k in range(len(list_field)):
            if len(string) > 0:
                if string[i].isdigit():
                    if k == int(string[i]):
                        gap_string.append(k)

    string.replace(' ', '') # Удаляем пробелы

    return gap_string


def help_game():
    """
        Выполняет вывод посказки пользователю о правилах игры
    """
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


def generate_field():
    """
        Выполняет очистку игрового поля
    """
    return [
        ['-','-','-'],
        ['-','-','-'],
        ['-','-','-'],
    ]


def next_game(ind, field):
    """
        Выполняет завершение или продолжение игры в зависимости
        от выбора пользователя
    """
    next = input('Повторить? Y-Да, N-Нет - ')
    next = next.upper()

    if next != 'Y':
        return False
    elif next == 'Y':
        ind = 1
        field = generate_field()
        help_game()
        return True


def tic_tac_toe(field):
    """
        Выполняет запуск игры крестики-нолики
    """

    # Игроки
    gamer = {
        'x' : 'Крестик',
        'o' : 'Нолик'
    }
    ind             = 1             # Счетчик ходов
    current_gamer   = gamer['x']    # Игрок
    move            = 'x'           # Ход
    probability     = {'victory':False} # Вероятность выйгрыша

    field = generate_field()
    help_game()

    while True:
        probability['victory'] = False

        # Очередность игрока - Чей ход
        if ind % 2 == 1:
            current_gamer = gamer['x']
            move = 'x'
        elif ind % 2 == 0:
            current_gamer = gamer['o']
            move = 'o'

        answer = input_data(current_gamer)
        answer = format_data(answer, field)

        if len(answer) == 2:
            coordinate = field[answer[0]][answer[1]]

            if coordinate == '-':
                field[answer[0]][answer[1]] = move
                ind += 1
            else:
                print('Это поле занято повторите ход')

            output_result(field)

            horizontal      = is_horizontal(field)
            vertical        = is_vertical(field,probability)
            diagonal_left   = is_diagonal_left(field)
            diagonal_right  = is_diagonal_right(field)
            draw            = is_empty_cage(field)
            victory         = horizontal or vertical or diagonal_left or diagonal_right

            if victory:
                print("Победил игрок", gamer[victory])
                if not next_game(ind,field):
                    break
            elif draw and not probability['victory']:
                print('Победитель не выявлен!')
                if not next_game(ind,field):
                    break
        else:
            print('Неверный формат, повторите ввод!')


# Игровое поле
field = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-'],
]

tic_tac_toe(field)