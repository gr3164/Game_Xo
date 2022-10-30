from itertools import groupby
import random


box = [['\u00B7','\u00B7','\u00B7'], ['\u00B7','\u00B7','\u00B7'], ['\u00B7','\u00B7','\u00B7']]
win = [[[0, 0],[0, 1],[0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]], 
        [[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]], [[0, 2], [2, 2], [2, 0]]]
unique = [(x,y) for x in range(0,3) for y in range(0,3)]
bot = random.choice(unique)

def Print_box(box, key):
    if key == 'y':
        j = 1
        print("   1 2 3")
        for i in box:
            print(f'{j}|',' '.join(i))
            j = j+1
    if key == 'n':
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
          

def Win_g(box):
    for i in range(0,3):
        for x in box:
            if len(x) == x.count(x[i]) and not '\u00B7' in x:
                return True
            else:
                False
        

def Win_v(box):
    mylist = [ i[x][0] for x in range(0,3) for i in box]
    mylist = [mylist[i:i + 3] for i in range(0, len(mylist), 3)]

    for i in range(0,3):
        if len(mylist[i]) == mylist[i].count(mylist[i][0]) and not '\u00B7' in mylist[i]:
            return True
        else:
            False

def Win_x(box):
    mylist_x = [[],[]]
    i = 0
    j = -1
    for x in box:
        mylist_x[0].append(x[i])
        mylist_x[1].append(x[j])
        i += 1
        j -= 1
    for i in range(0,2):
        if len(mylist_x[i]) == mylist_x[i].count(mylist_x[i][0]) and not '\u00B7' in mylist_x[i]:
            return True
        else:
            False



    # if len(box[0]) == box[0].count(box[0][0]) and not '\u00B7' in box[0]:
    #     print("Win")
    
   

print_key = input("Отоброжать напровляющие(Ряд/Столб) Y/N: ").lower()
# choice = str(input("Будете ходить первым? y/n: ").lower())

while True:
    Print_box(box, print_key) 

    if 0 < len(unique):
        #user Ввод пользователя + проверка на уникальность + удаление элемента из уникального списка
        user = int(input("Число по горизонтали(РЯД): "))-1, int(input("Число по вериткали (СТОЛБ): "))-1
        user = Compare_unique(user, unique)
        unique.remove(user)
        box[user[0]][user[1]] = 'x'
        Win_g(box)
        print(Win_g(box))
        Win_v(box)
        print(Win_v(box))
        Win_x(box)
        print(Win_x(box))
        
        
      

        if 0 == len(unique):
            Print_box(box, print_key)
            print("Ничья")
            break

        # bot Выбор рандомного уникального элемента + удаление элемента из уникального списка
        # bot = random.choice(unique)
        # unique.remove(bot)
        # box[bot[0]][bot[1]] = 'o'
        

        print(f'Вы: {user}')
        print(f'Бот: {bot}')
        print('====================')
        # print(unique)
    else:
        Print_box(box, print_key)
        print("Ничья")
        break
 