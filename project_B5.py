play_field_XO = [['.' for j in range(3)] for i in range(3)]


def output_field():
    print()
    print(f'    0 | 1 | 2 | ')
    print('----------------')
    for elem in range(3):
        print(f'{elem} | {" | ".join(play_field_XO[elem])} |')
        print('----------------')


def input_value():
    while True:
        value = input('Введите координаты хода:').split()
        if len(value) != 2:
            print('Ошибка! Введите две координаты')
            continue
        if (not value[0].isdigit()) or (not value[1].isdigit()):
            print('Ошибка! Введите числа')
            continue
        a, b = map(int, value)
        if not (0 <= a < 3 and 0 <= b < 3):
            print('Ошибка! Вышли за границу поля')
            continue
        if play_field_XO[a][b] != '.':
            print('Ошибка! Клетка занята')
            continue
        else:
            return a, b


def win():
    win_comb = [[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]],
                [[0, 2], [1, 1], [2, 0]], [[0, 0], [1, 1], [2, 2]], [[0, 0], [1, 0], [2, 0]],
                [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]]]
    for elem in win_comb:
        win_win = []
        for i in elem:
            win_win.append(play_field_XO[i[0]][i[1]])
            if win_win == [val, val, val]:
                return True
    return False


count = 0
print('Добро пожаловать в игру крестики-нолики!!!')
choice = input('Выбирите сторону x или 0: ')
while True:
    if choice == 'x':
        if count == 9:
            print('Ничья!')
            break
        if count % 2 == 0:
            val = 'x'
        else:
            val = '0'
        output_field()
        x, y = input_value()
        play_field_XO[x][y] = val
        if win():
            print(f'Выиграл игрок {val}')
            output_field()
            break
        count += 1
    elif choice == '0':
        if count == 9:
            print('Ничья!')
            break
        if count % 2 == 0:
            val = '0'
        else:
            val = 'x'
        output_field()
        x, y = input_value()
        play_field_XO[x][y] = val
        if win():
            print(f'Выиграл игрок  {val}')
            output_field()
            break
        count += 1
    else:
        print('Вы выбрали темную сторону, одумайтесь!')
        break
