field = list(range(1,10))

def g_field():
    print("-------------------")
    for i in range(3):
        print("| ", field[0 + i * 3]," | ", field[1 + i * 3]," | ", field[2 + i * 3]," | ")
        print("-------------------")

def step_g(step, chip):
    ind = field.index(step)
    field[ind] = chip

def step_check():
    while True:
        step = int(input("        ходит: "))
        if 0 <= step <= 9:
            if step in field:
                return step
            else:
                print("Поле занято")
        else:
            print("Такого поля нет")

def vi_exe():
    victori = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
               [0, 3, 6], [1, 4, 7], [2, 5, 8],
               [0, 4, 8], [2, 4, 6]]
    num = ""
    for i in victori:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            num = "X"
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
            num = "O"
    return num

game_over = False
gamer = 0

while game_over == False:
    g_field()

    if gamer % 2 == 0:
        chip = "X"
        print("Первый игрок ")
        step = step_check()


    if gamer % 2 == 1:
        chip = "O"
        print("Второй игрок ")
        step = step_check()

    step_g(step, chip)
    num = vi_exe()
    if num != "" or gamer == 8:
        game_over = True
    else:
        game_over = False
    gamer += 1

g_field()
print ("Победили: ", num if num == "X" or num == "O" else "Ничья")