import re

def get_input_data():
    with open(r'2023/input/1.txt') as f:
        lines = f.readlines()
    return lines

def remove_non_digits(input_str):
    return re.sub("\D","",input_str)

def get_first_and_last_digit(input_str):
    return int(input_str[0]+input_str[len(input_str)-1])

def convert_string_to_digit(input_str):
    return input_str.replace('one','o1e').replace('two','t2o').replace('three','th3ee').replace('four','fo4ur').replace('five','fi5ve').replace('six','si6x').replace('seven','se7ven').replace('eight','ei8ght').replace('nine','ni9ne')

def solve_a(lines):
    line_sum = 0
    for line in lines:
        digits_only = remove_non_digits(line)
        first_and_last_digit = get_first_and_last_digit(digits_only)
        line_sum = line_sum + first_and_last_digit
    print('A:',line_sum)
    return

def solve_b(lines):
    line_sum = 0
    for line in lines:
        string_to_digits = convert_string_to_digit(line)
        digits_only = remove_non_digits(string_to_digits)
        first_and_last_digit = get_first_and_last_digit(digits_only)
        line_sum = line_sum + first_and_last_digit
    print('B:',line_sum)
    return

def main():
    input_data = get_input_data()
    solve_a(input_data)
    solve_b(input_data)

if __name__ == "__main__":
    main()