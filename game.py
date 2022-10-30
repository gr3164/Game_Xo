import random

box = [['\u00B7','\u00B7','\u00B7'], ['\u00B7','\u00B7','\u00B7'], ['\u00B7','\u00B7','\u00B7']]
unique = [(x,y) for x in range(0,3) for y in range(0,3)]
# bot = random.choice(unique)

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
          
def Win_g(box):
    mylist = [ i[x][0] for x in range(0,3) for i in box]
    mylist = [mylist[i:i + 3] for i in range(0, len(mylist), 3)]
    for i in range(0,3):
        for x in box:
            if len(x) == x.count(x[i]) and not '\u00B7' in x or len(mylist[i]) == mylist[i].count(mylist[i][0]) and not '\u00B7' in mylist[i]:
                return True
            else:
                return Win_x(box)
        

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
        if Win_g(box):
            Print_box(box, print_key)
            print("Вы победили !!!")
            break
        
        if 0 == len(unique):
            Print_box(box, print_key)
            print("Ничья")
            break


        # bot Выбор рандомного уникального элемента + удаление элемента из уникального списка
        bot = random.choice(unique)
        unique.remove(bot)
        box[bot[0]][bot[1]] = 'o'
        if Win_g(box):
            Print_box(box, print_key)
            print("Бот выиграл !!!")
            break

    else:
        Print_box(box, print_key)
        print("Ничья")
        break
 