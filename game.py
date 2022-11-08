import random
from colorama import *
import webbrowser


init(autoreset=True)


print(Fore.GREEN + "Добро пожаловать в игру!!!\n\"Крестики нолики\"")

while (True):
    print("")
    box = [['\u00B7','\u00B7','\u00B7'], ['\u00B7','\u00B7','\u00B7'], ['\u00B7','\u00B7','\u00B7']]
    unique = [(x,y) for x in range(0,3) for y in range(0,3)]

    def check_win(box):
        win_comb = (((0,0),(0,1),(0,2)), ((1,0),(1,1),(1,2)), ((2,0),(2,1),(2,2)),
                    ((0,0),(1,0),(2,0)), ((0,1),(1,1),(2,1)), ((0,2),(1,2),(2,2)),
                    ((0,0),(1,1),(2,2)), ((0,2),(1,1),(2,0)))
        for i in win_comb:
            if box[i[0][0]][i[0][1]] == box[i[1][0]][i[1][1]] == box[i[2][0]][i[2][1]] != '\u00B7':
                return (box[i[0][0]][i[0][1]]).upper()
        return False
        
    def Print_box(box, key):
        if key == 'y':
            j = 1
            print('====================')
            # print("  \u0332 \u03321\u0332 \u03322\u0332 \u03323")
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
                print(Fore.RED + "Координата занята или несуществует. Выберите другую: ")
                Print_box(box, print_key)
                p = int(input("Число по горизонтали(РЯД): "))-1, int(input("Число по вериткали (СТОЛБ): "))-1 
                if p in unique:
                    break
            return p
        else: return p

    print_key = input("Отоброжать напровляющие(Ряд/Столб) Y/N: ").lower()
    while (True):
        Print_box(box, print_key)
        if check_win(box) != False:
            print(Fore.GREEN + "Победа " + check_win(box))
            break 
        
        user = int(input("Число по горизонтали(РЯД): "))-1, int(input("Число по вериткали (СТОЛБ): "))-1
        user = Compare_unique(user, unique)
        unique.remove(user)
        box[user[0]][user[1]] = Fore.RED + 'x' + Style.RESET_ALL

        if check_win(box) != False:
            Print_box(box, print_key)
            print(Fore.GREEN + "Победа " + check_win(box))
            break 
        if 0 == len(unique):
            Print_box(box, print_key)
            print(Fore.CYAN + "Ничья")
            break

        bot = random.choice(unique)
        unique.remove(bot)
        box[bot[0]][bot[1]] = Fore.CYAN + 'o' + Style.RESET_ALL
    
    print(Fore.CYAN + "Играть еще раз Y/N ? ", end='') 
    F = input().lower()
    if F != 'y':
        break


print(Fore.RED + "Посмотреть исходный код ? Y/N : ")
k = input().lower()
if k == 'y':
    webbrowser.open('https://github.com/gr3164/Game_Xo.git')
input()


    