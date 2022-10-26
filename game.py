import random


box = [['\u00B7','\u00B7','\u00B7'], ['\u00B7','\u00B7','\u00B7'], ['\u00B7','\u00B7','\u00B7']]
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

# def Compare_win(box, w):
#     # control = True
#     for j in box[0]:
#         if j == 'x':
#             print(f'{w} Win!!!')
#             control = False
#             return control
            
def Compare_win(box, w):
    if w == 2:
        for i in range(0,3):
            res = all(x == box[0][0] for x in box[i])
            if res == True:
                return res
            else:
                for j in range(0,3):
                    mylist = [ i[x][0] for x in range(0,3) for i in box]
                    mylist = [mylist[i:i + 3] for i in range(0, len(mylist), 3)] 
                    res2 = all(x == mylist[0][0] for x in mylist[j])
                    if res2 == True:
                        return res2
                    # доделать условие победы по пересечению от угла до угла

       
                



control = True 

print_key = input("Отоброжать напровляющие(Ряд/Столб) Y/N: ").lower()
# choice = str(input("Будете ходить первым? y/n: ").lower())

while control == True:
    
    Print_box(box, print_key)

    if 0 < len(unique) and control == True:
        #user Ввод пользователя + проверка на уникальность + удаление элемента из уникального списка
        user = int(input("Число по горизонтали(РЯД): "))-1, int(input("Число по вериткали (СТОЛБ): "))-1
        user = Compare_unique(user, unique)
        unique.remove(user)
        box[user[0]][user[1]] = 'x'
        print(type(Compare_win(box, user)))
        print(Compare_win(box, 2))

        if 0 == len(unique) and control == False:
            Print_box(box, print_key)
            print("Ничья")
            control = False
            break

        #bot Выбор рандомного уникального элемента + удаление элемента из уникального списка
        # bot = random.choice(unique)
        # unique.remove(bot)
        # box[bot[0]][bot[1]] = 'o'
        # Compare_win(box, bot)

        print(f'Вы: {user}')
        print(f'Бот: {bot}')
        print('====================')
        # print(unique)
    else:
        Print_box(box, print_key)
        print("Ничья")
        control = False
        break
 