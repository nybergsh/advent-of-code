import numpy as np

def get_input_data():
    # Read the file line by line
    with open(r'2023/input/3.txt') as file:
        lines = file.read().splitlines()

    # Initialize an empty 2D array
    data = np.empty((len(lines), len(lines[0])), dtype='str')

    # Populate the array with characters from the file
    for i, line in enumerate(lines):
        data[i, :] = list(line)

    # Display the result
    return data

def adjust_boards(c,s,p,value,start_xy,end_xy):
    for row in range(max(start_xy[0]-1,0),min(end_xy[0]+2,len(c))):
        for col in range(max(start_xy[1]-1,0),min(end_xy[1]+2,len(c[0]))):
            c[row,col] = c[row,col] + 1
            s[row,col] = s[row,col] + value
            p[row,col] = p[row,col] * value
    return c,s,p

def create_digit_boards(data):
    i = 0
    cnt_board = np.zeros((len(data),len(data[0])))
    sum_board = np.zeros((len(data),len(data[0])))
    prod_board = np.ones((len(data),len(data[0])))

    for i in range(0,len(data)):
        j = 0
        while j < len(data[i]):
            if data[i,j].isdigit():
                number = int(data[i,j])
                start_xy = [i,j]
                end_xy = [i,j]
                j += 1
                while j < len(data[i]):
                    if data[i,j].isdigit():
                        number = number*10 + int(data[i,j])
                        end_xy = [i,j]
                    else:
                        break
                    j += 1
                cnt_board,sum_board,prod_board = adjust_boards(cnt_board,sum_board,prod_board,number,start_xy,end_xy)
            j += 1
    return cnt_board,sum_board,prod_board

def solve_a(op_board,s_board):
    part_number_sum = 0
    for i in range(0,len(op_board)-1):
        for j in range(0,len(op_board[0])-1):
            if not op_board[i,j].isdigit() and op_board[i,j] != '.':
                part_number_sum += s_board[i,j]
    print('a:',part_number_sum)
    return

def solve_b(op_board,c_board,p_board):
    gear_prod_sum = 0
    for i in range(0,len(op_board)-1):
        for j in range(0,len(op_board[0])-1):
            if op_board[i,j] == '*' and c_board[i,j] == 2:
                gear_prod_sum += p_board[i,j]
    print('b:',gear_prod_sum)
    return

def main():
    board = get_input_data()
    cnt_array,sum_array,prod_array = create_digit_boards(board)
    solve_a(board,sum_array)
    solve_b(board,cnt_array,prod_array)
    return


if __name__ == "__main__":
    main()