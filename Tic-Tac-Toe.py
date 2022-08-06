from array import array


input_list = []
rows, cols = (3, 3)
winn = False
winner = 'None'
arr = [[" " for i in range(cols)] for j in range(rows)]


def print_grid():
    row_1 = ' | | '
    row_sep_1 = '-+-+-'
    row_2 = ' | | '
    row_sep_2 = '-+-+-'
    row_3 = ' | | '
    print('\n', row_1, '\n', row_sep_1, '\n',
          row_2, '\n', row_sep_2, '\n', row_3,)


def user_input(num_1):
    print('\n', '7 8 9', '\n', '4,5,6', '\n', '1 2 3')
    tester = True
    while(tester):
        num_1 = int(
            input('Please select a value from following grid to place your mark: '))
        if num_1 in range(1, 10):
            if num_1 in input_list:
                print('Selected position is already filled please select another one')
            else:
                input_list.append(num_1)
                return num_1
        else:
            print("Invalid user input please try again")
            pass


def editing_array_pa(num_2):
    if num_2 == 1:
        arr[2][0] = 'x'
    elif num_2 == 2:
        arr[2][1] = 'x'
    elif num_2 == 3:
        arr[2][2] = 'x'
    elif num_2 == 4:
        arr[1][0] = 'x'
    elif num_2 == 5:
        arr[1][1] = 'x'
    elif num_2 == 6:
        arr[1][2] = 'x'
    elif num_2 == 7:
        arr[0][0] = 'x'
    elif num_2 == 8:
        arr[0][1] = 'x'
    else:
        arr[0][2] = 'x'


def editing_array_pb(num_2):
    if num_2 == 1:
        arr[2][0] = "o"
    elif num_2 == 2:
        arr[2][1] = 'o'
    elif num_2 == 3:
        arr[2][2] = 'o'
    elif num_2 == 4:
        arr[1][0] = 'o'
    elif num_2 == 5:
        arr[1][1] = 'o'
    elif num_2 == 6:
        arr[1][2] = 'o'
    elif num_2 == 7:
        arr[0][0] = 'o'
    elif num_2 == 8:
        arr[0][1] = 'o'
    else:
        arr[0][2] = 'o'


def win_check(arr_1):
    for x in range(0, 2):
        y = 0
        if arr_1[x][y] == arr_1[x][y+1] == arr_1[x][y+2] != ' ':
            return arr_1[x][y]
        elif arr_1[x][y] == arr_1[x+1][y] == arr_1[x+2][y] != ' ':
            return arr_1[x][y]
        elif arr_1[0][0] == arr_1[1][1] == arr_1[2][2] != ' ':
            return arr_1[x][y]
        elif arr_1[2][0] == arr_1[1][1] == arr_1[0][2] != ' ':
            return arr_1[x][y]
        else:
            return 'None'
            

def print_real_arr(arr):
    for row in arr:
        print(row)


num_1 = 0
for z in range(1, 10):
    if z % 2 != 0:
        temp_num = user_input(num_1)
        editing_array_pa(temp_num)
        print_real_arr(arr)
        if z > 4:
            winner = win_check(arr)
        else:
            pass
    else:
        temp_num = user_input(num_1)
        print(input_list)
        editing_array_pb(temp_num)
        print_real_arr(arr)
        if z > 4:
            winner = win_check(arr)
        else:
            pass
    if winner != 'None':
        break
    else:
        pass
print(winner, "Wins")
