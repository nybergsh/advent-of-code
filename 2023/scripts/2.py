def get_input_data():
    with open(r'2023/input/2.txt') as f:
        lines = f.readlines()
    return lines

def check_which_games_are_possible(id,hands):
    rules = {'red':12,'green':13,'blue':14}
    for hand in hands.split('; '):
        for pair in hand.split(', '):
            colour = pair.split(' ')[1].strip()
            amount = int(pair.split(' ')[0])
            if amount > rules[colour]:
                return False
    return True


def solve_a(games):
    sum_of_game_ids = 0
    for game in games:
        game_id = int(game.split(':')[0].split(' ')[1])
        game = game.split(': ')[1]
        possible_game = check_which_games_are_possible(game_id,game)
        if possible_game:
            sum_of_game_ids += game_id
    print('A:',sum_of_game_ids)
    return

def solve_b(games):
    sum_of_game_powers = 0
    for game in games:
        max_per_colour = {'red':0,'green':0,'blue':0}
        game = game.split(': ')[1]
        for hand in game.split('; '):
            for pair in hand.split(', '):
                colour = pair.split(' ')[1].strip()
                amount = int(pair.split(' ')[0])
                if amount > max_per_colour[colour]:
                    max_per_colour[colour] = amount
        game_power = max_per_colour['red']*max_per_colour['blue']*max_per_colour['green']
        sum_of_game_powers += game_power
    print('B:',sum_of_game_powers)
        


def main():
    input_data = get_input_data()
    solve_a(input_data)
    solve_b(input_data)
    return


if __name__ == "__main__":
    main()