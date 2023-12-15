import numpy as np

def get_input_data():
    with open(r'2023/input/4.txt') as f:
        lines = f.readlines()
    return lines

def main():
    scratchcards = get_input_data()
    number_of_lottery_tickets = np.ones(len(scratchcards))
    winning_sum = 0
    for index,card in enumerate(scratchcards):
        card_value = 0.5
        winning_card = False
        matching_numbers = 0
        card_id = card.split(': ')[0].split(' ')[1]
        winning_numbers = card.split(': ')[1].split(' | ')[0].split(' ')
        card_numbers = card.split('| ')[1].strip().split(' ')
        #print(card_numbers)
        #print(winning_numbers)
        for number in card_numbers:
            if number != '' and number in winning_numbers:
                #print(card_id,number)
                card_value = card_value * 2
                matching_numbers += 1
                number_of_lottery_tickets[index+matching_numbers] += 1*number_of_lottery_tickets[index]
                winning_card = True
        if winning_card:
            print('id:',index,'win:',card_value)
            winning_sum += card_value
            
    print('a:',winning_sum)
    print('b:',number_of_lottery_tickets.sum())
    return


if __name__ == "__main__":
    main()