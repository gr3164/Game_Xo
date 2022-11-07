import random

box = [['\u00B7','\u00B7','\u00B7'], ['\u00B7','\u00B7','\u00B7'], ['\u00B7','\u00B7','\u00B7']]
unique = [(x,y) for x in range(0,3) for y in range(0,3)]

# bot = random.choice(unique)

def check_win(box):
    win_comb = (((0,0),(0,1),(0,2)), ((1,0),(1,1),(1,2)), ((2,0),(2,1),(2,2)),
                ((0,0),(1,0),(2,0)), ((0,1),(1,1),(2,1)), ((0,2),(1,2),(2,2)),
                ((0,0),(1,1),(2,2)), ((0,2),(1,1),(2,0)))
    for i in win_comb:
        if box[i[0][0]][i[0][1]] == box[i[1][0]][i[1][1]] == box[i[2][0]][i[2][1]] != '\u00B7':
            return box[i[0][0]][i[0][1]]
    return False
    
    
def Print_box(box, key):
    if key == 'y':
        j = 1
        print('====================')
        print("   1 2 3")
        for i in box:
            print(f'{j}|',' '.join(i))
            j = j+1
    else:
        print('====================')
        for i in box:
            print(' '.join(i))

def Compare_unique(p, unique):
    if not p in unique:
        while not p in unique:
            print("Координата занята или несуществует. Выберите другую: ")
            p = int(input("Число по горизонтали(РЯД): "))-1, int(input("Число по вериткали (СТОЛБ): "))-1 
            if p in unique:
                break
        return p
    else: return p
#=======================================================



print_key = input("Отоброжать напровляющие(Ряд/Столб) Y/N: ").lower()
# choice = str(input("Будете ходить первым? y/n: ").lower())

while True:
    Print_box(box, print_key)
    if check_win(box) != False:
        print("Победа " + check_win(box))
        break 
    if 0 == len(unique):
        Print_box(box, print_key)
        print("Ничья")
        break

    #user Ввод пользователя + проверка на уникальность + удаление элемента из уникального списка
    user = int(input("Число по горизонтали(РЯД): "))-1, int(input("Число по вериткали (СТОЛБ): "))-1
    user = Compare_unique(user, unique)
    unique.remove(user)
    box[user[0]][user[1]] = 'x'

    if 0 == len(unique):
        Print_box(box, print_key)
        print("Ничья")
        break

    # bot Выбор рандомного уникального элемента + удаление элемента из уникального списка
    bot = random.choice(unique)
    unique.remove(bot)
    box[bot[0]][bot[1]] = 'o'
   