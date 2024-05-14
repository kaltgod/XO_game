Win = None
line = None
column = None
draw = None


field = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]


def print_field():
    print(f"""-------------------
|  {field[0][0]}  |  {field[0][1]}  |  {field[0][2]}  |
-------------------
|  {field[1][0]}  |  {field[1][1]}  |  {field[1][2]}  |
-------------------
|  {field[2][0]}  |  {field[2][1]}  |  {field[2][2]}  |
-------------------""")


def victory_check(a):
    global draw
    if field[0][0] == a and field[1][1] == a and field[2][2] == a:
        return True
    elif field[2][0] == a and field[1][1] == a and field[0][2] == a:
        return True
    elif field[0][0] == a and field[0][1] == a and field[0][2] == a:
        return True
    elif field[1][0] == a and field[1][1] == a and field[1][2] == a:
        return True
    elif field[2][0] == a and field[2][1] == a and field[2][2] == a:
        return True
    elif field[0][0] == a and field[1][0] == a and field[2][0] == a:
        return True
    elif field[0][1] == a and field[1][1] == a and field[2][1] == a:
        return True
    elif field[0][2] == a and field[1][2] == a and field[2][2] == a:
        return True
    if '-' not in field[0]:
        if '-' not in field[1]:
            if '-' not in field[2]:
                print('Ничья')
                draw = 1



def recognition(z):
    global line
    global column
    a = input(f'Введите строку и столб в который хотите записать {z}:')
    a2 = a.replace(',', '').replace(' ', '')
    if len(a2) == 2:
        if not a2[0].isalpha() and not a2[1].isalpha():
            line, column = int(a2[0]) - 1, int(a2[1]) - 1
            if line >= 3 or column >= 3:
                print('Пожалуйста введите корректные значения')
                recognition(z)
        else:
            print('Пожалуйста введите корректные значения')
            recognition(z)
    else:
        print('Пожалуйста введите корректные значения')
        recognition(z)
    return line, column


def character_input(z):
    global field
    a, b = recognition(z)
    if field[a][b] != '-':
        print('Выберите место, где ещё нет вашего или вражеского символа')
        character_input(z)
    else:
        field[a][b] = z
        print_field()


def game():
    global field
    global draw
    draw = None
    field = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    print_field()
    while True:
        character_input('X')
        if victory_check('X'):
            print('Победа X!')
            break
        if draw == 1:
            break
        character_input('O')
        if victory_check('O'):
            print('Победа O!')
            break
    one_more = input('Если хотите сыграть ещё раз, введите "да". Если хотите закончить, введите "нет":')
    if one_more == 'да':
        game()
    elif one_more == 'нет':
        pass



if __name__ == '__main__':
    print('Добро пожаловать в игру крестики-нолики!')
    game()
