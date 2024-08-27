import random 
import time

RANKS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return f'{self.rank} {self.suit}'
    
def show_cards(player_cards):
    for card in player_cards:
        print(card)

def main():
    print('Hello! Welcome. \nEnter "play" to start the game. \nIf you need help, enter "help".\n')
    command = input().lower()
    if command == 'play':
        play_card_game()
    elif command == 'help':
        help()
    else:
        print('Enter only "play" or "help"!!! >:[')
        
def prepare_cards(): #подготовка колоды
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    cards = [Card(rank,suit) for suit in suits for rank in RANKS]
    print('\nLet`s gooo\n') 
    random.shuffle(cards)
    return cards

def play_card_game():
    my_list = []
    cards = prepare_cards()
    player_cards = get_cards_into_hand(cards = cards, player_cards = [], cards_limit = 6)
    bot_cards = get_cards_into_hand(cards = cards, player_cards = [], cards_limit = 6)
    print('Now you have:\n')
    show_cards(player_cards)
    trump_card = trump_card_is(cards)
    minimum_trump(player_cards, trump_card)
    minimum_trump(bot_cards, trump_card)
    my_list.insert(1, trump_card)
    show_cards(player_cards=bot_cards)
    who_goes_first(trump_card,player_cards,bot_cards, cards)

def trump_card_is(cards):
    print('\nThe trump card is...\n') #выводит козыря на экран
    trump_card = cards.pop(-1)
    print(trump_card)
    print()
    return trump_card

def get_cards_into_hand(cards, player_cards, cards_limit):
    while len(player_cards) < cards_limit:
        card = cards.pop(-1)
        player_cards.append(card)
    return player_cards

def minimum_trump(player_cards, trump_card):
    min_trump_card_rank = 10
    for i in range(len(player_cards)):
        if player_cards[i].suit == trump_card.suit:
            current_trump_index = RANKS.index(player_cards[i].rank)
            min_trump_card_rank = min(min_trump_card_rank, current_trump_index)

def who_goes_first(trump_card,player_cards,bot_cards, cards):
    suit_trump_card = trump_card.suit
    suit_player_card = None
    suit_bot_card = None
    player_count = 0
    bot_count = 0
    player_numbers = []
    bot_numbers = []
    for index in range(6): #смотрим кто первый ходит
        player_card_index = player_cards[index]
        bot_card_index = bot_cards[index]
        number_player = player_card_index.rank
        number_bot = bot_card_index.rank
        suit_player_card = player_card_index.suit
        suit_bot_card = bot_card_index.suit
        if suit_player_card == suit_trump_card:
            player_numbers.append(number_player)
            player_count += 1 
        if suit_bot_card == suit_trump_card:
            bot_numbers.append(number_bot)
            bot_count += 1     
    if bot_count == 0:
        play_player_first(player_cards,bot_cards, suit_trump_card, cards)    #первый ходит игрок         
    elif player_count == 0:
        play_bot_first(bot_cards)# первый ходит бот
    elif player_count == 0 and bot_count == 0:
        num_for_random = [0, 1]
        random.shuffle(num_for_random)
        if num_for_random[0] == 0:
            play_bot_first
        else:
            play_player_first
    else:
        lenght_of_list_player = len(player_numbers)
        lenght_of_list_bot = len(bot_numbers)
        #sort(player_numbers, bot_numbers)
        player_numbers.sort()
        player_trump_card = None
        for lenght_player in range(lenght_of_list_player):
            if player_numbers[lenght_player] == '6': # проверка кто первый: меньший козырь
                player_trump_card = player_numbers[lenght_player]
                break
            else:
                if player_numbers[lenght_player] == '7':
                    player_trump_card = player_numbers[lenght_player]
                    break
                else:
                    if player_numbers[lenght_player] == '8':
                        player_trump_card = player_numbers[lenght_player]
                        break
                    else:
                        if player_numbers[lenght_player] == '9':
                            player_trump_card = player_numbers[lenght_player]
                            break
                        else:
                            if player_numbers[lenght_player] == '10':
                                player_trump_card = player_numbers[lenght_player]
                                break
                            else:
                                if player_numbers[lenght_player] == 'J':
                                    player_trump_card = player_numbers[lenght_player]
                                    break
                                else:
                                    if player_numbers[lenght_player] == 'Q':
                                        player_trump_card = player_numbers[lenght_player]
                                        break
                                    else:
                                        if player_numbers[lenght_player] == 'K':
                                            player_trump_card = player_numbers[lenght_player]
                                            break
                                        else:
                                            if player_numbers[lenght_player] == 'A':
                                                player_trump_card = player_numbers[lenght_player]
                                                break
        bot_trum_card = None
        bot_numbers.sort()
        for lenght_bot in range(lenght_of_list_bot):
            if bot_numbers[lenght_bot] == '6':
                bot_trum_card = bot_numbers[lenght_bot]
                break
            else:
                if bot_numbers[lenght_bot] == '7':
                    bot_trum_card = bot_numbers[lenght_bot]
                    break
                else:
                    if bot_numbers[lenght_bot] == '8':
                        bot_trum_card = bot_numbers[lenght_bot]
                        break
                    else:
                        if bot_numbers[lenght_bot] == '9':
                            bot_trum_card = bot_numbers[lenght_bot]
                            break
                        else:
                            if bot_numbers[lenght_bot] == '10':
                                bot_trum_card = bot_numbers[lenght_bot]
                                break
                            else:
                                if bot_numbers[lenght_bot] == 'J':
                                    bot_trum_card = bot_numbers[lenght_bot]
                                    break
                                else:
                                    if bot_numbers[lenght_bot] == 'Q':
                                        bot_trum_card = bot_numbers[lenght_bot]
                                        break
                                    else:
                                        if bot_numbers[lenght_bot] == 'K':
                                            bot_trum_card = bot_numbers[lenght_bot]
                                            break
                                        else:
                                            if bot_numbers[lenght_bot] == 'A':
                                                bot_trum_card = bot_numbers[lenght_bot]
                                                break
                                            else:
                                                print('bN')
        cards_num = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for index in range(len(cards_num)):
            if player_trump_card == cards_num[index]:
                play_player_first(player_cards,bot_cards, suit_trump_card, cards) #первый игрок в силу меньшего козыря
                break
            elif bot_trum_card == cards_num[index]:
                play_bot_first(bot_cards) #первый бот в силу меньшего козыря
                print('bot start')
                break

def take_cards(bot_cards,player_cards,cards):
    if len(bot_cards) < 6:
        while len(bot_cards) != 6:
            card_to_add = cards[0].rank+' '+cards[0].suit
            bot_cards.append(card_to_add)
            cards.remove(cards[0])
    if len(player_cards) < 6:
        while len(player_cards) != 6:
            card_to_add = cards[0].rank+' '+cards[0].suit
            player_cards.append(card_to_add)
            cards.remove(cards[0])
    
def bot_takes_cards(selected_cards,bot_cards,player_cards,number_selected_card):
    bot_cards.append(selected_cards)
    time.sleep(1)
    print('\nThe bot is taking the cards now.\n')
    add_cards(player_cards,number_selected_card, bot_cards)

def add_cards(player_cards,number_selected_card, bot_cards):
    count = 0
    time.sleep(1)
    print()
    print('Do you want to add more cards? (enter "yes" or "no")\n')
    answer = input().lower()
    while answer != "no" or count != 6:
        if answer == 'yes':
            count += 1
            card_to_add = input('Enter card you want to add...\n')
            number_card_to_add = card_to_add[slice(1)]
            count_for_check = 0
            count_for_check_num = 0
            while len(answer) != 0:
                for i in range(len(player_cards)):
                    if card_to_add == player_cards[i]:
                        count_for_check += 1
                        if number_card_to_add == number_selected_card:
                            count_for_check_num += 1
                if count_for_check == 0:
                    print("Enter only your cards!\n")
                    break
                else:
                    if count_for_check_num == 0:
                        print('\nYou can enter cards that only have the same number!\n')
                        break
                    else:
                        bot_cards.append(card_to_add)
                        break
        elif answer == 'no':
            print('OK\n')
            break
        else:
            print('Enter only "yes" or "no"!')
            break
def play_player_first(player_cards, bot_cards, suit_trump_card,cards):
    print(bot_cards) #ПОТОМ УБРАТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Это я сделала для себя шоб понять правильно ли работает :)
    print("Choose a card.\n")
    card = input()
    while cards != None:
        count = 0
        try:
            selected_cards = []
            while len(player_cards) == 6:
                for i in range(len(player_cards)):
                    selected_card = player_cards[i].rank+' '+player_cards[i].suit
                    if card == selected_card:
                        player_cards.remove(player_cards[i])
                        selected_cards.append(selected_card)
                        break
                break
            break
        except ValueError:
            print('Enter only your card!')
    play_bot(player_cards, bot_cards, suit_trump_card,cards, selected_cards)
    
                        
                    
def play_bot(player_cards, bot_cards, suit_trump_card,cards, selected_cards):
        suit_selected_card = selected_cards[slice(2,-1)]
        number_selected_card = selected_cards[slice(1)]
        count = 0
        suit_bot_card = []
        for index in range(len(bot_cards)):
            bot_card_index = bot_cards[index]
            suit_bot_card.append(bot_card_index.suit)
        number_selected_bot_card = []
        number_bot_trump_card_list = []
        if suit_selected_card == suit_trump_card: #если масть карты игрока совпадает с мастью козыря
            for index in range(len(bot_cards)):
                bot_card = bot_cards[index]
                suit_bot_card = bot_card.suit
                number_bot_card = bot_card.rank
                if suit_bot_card == suit_trump_card:
                    number_bot_trump_card = bot_card[slice(1)]
                    number_bot_trump_card_list.append(number_bot_trump_card)
                    count += 1
                number_selected_bot_card.append(number_bot_card)
            number_bot_trump_card_list.sort()
            if count == 0:
                bot_takes_cards(selected_cards,bot_cards,player_cards,number_selected_card)
            else:
                count_for_check = 0
                while count_for_check != 1:
                    if number_selected_card == '6':
                        for index in range(len(number_bot_trump_card_list)):
                            card = number_bot_trump_card_list[index]
                            if card == '7' or card == '8' or card == '9' or card == 'A' or card == 'B' or card == 'D' or card == 'K' or card == 'T':
                                count_for_check += 1
                                break
                    elif number_selected_card == '7':
                        for index in range(len(number_bot_trump_card_list)):
                            card = number_bot_trump_card_list[index]
                            if card == '8' or card == '9' or card == 'A' or card == 'B' or card == 'D' or card == 'K' or card == 'T':
                                count_for_check += 1
                                break
                    elif number_selected_card == '8':
                        for index in range(len(number_bot_trump_card_list)):
                            card = number_bot_trump_card_list[index]
                            if card == '9' or card == 'A' or card == 'B' or card == 'D' or card == 'K' or card == 'T':
                                count_for_check += 1
                                break
                    elif number_selected_card == '9':
                        for index in range(len(number_bot_trump_card_list)):
                            card = number_bot_trump_card_list[index]
                            if card == 'A' or card == 'B' or card == 'D' or card == 'K' or card == 'T':
                                count_for_check += 1
                                break
                    elif number_selected_card == 'A':
                        for index in range(len(number_bot_trump_card_list)):
                            card = number_bot_trump_card_list[index]
                            if card == 'B' or card == 'D' or card == 'K' or card == 'T':
                                count_for_check += 1
                                break
                    elif number_selected_card == 'B':
                        for index in range(len(number_bot_trump_card_list)):
                            card = number_bot_trump_card_list[index]
                            if card == 'D' or card == 'K' or card == 'T':
                                count_for_check += 1
                                break
                    elif number_selected_card == 'D':
                        for index in range(len(number_bot_trump_card_list)):
                            card = number_bot_trump_card_list[index]
                            if card == 'K' or card == 'T':
                                count_for_check += 1
                                break
                    elif number_selected_card == 'K':
                        for index in range(len(number_bot_trump_card_list)):
                            card = number_bot_trump_card_list[index]
                            if card == 'T':
                                count_for_check += 1
                                break
                    elif number_selected_card == 'T':
                        bot_takes_cards(selected_cards,bot_cards, player_cards,number_selected_card)
                        break
                    else:
                        bot_takes_cards(selected_cards,bot_cards, player_cards,number_selected_card)
                        break
                if count_for_check == 0:
                    bot_takes_cards(selected_cards,bot_cards, player_cards,number_selected_card)
                else: 
                    selected_bot_card = card + ' ' + suit_trump_card
                    print('\nThe bot`s card is...\n')
                    time.sleep(1)
                    print(selected_bot_card)
                    print()
                    for i in range(len(bot_cards)):
                        if selected_bot_card == bot_cards[i]:
                            bot_cards.remove(selected_bot_card)
                            break          
        else:
            suit_bot_cards = []
            number_bot_cards = []
            for i in range(len(bot_cards)):
                bot_card = bot_cards[i]
                suit_bot_cards.append(bot_card.suit)
                number_bot_cards.append(bot_card.rank)
            count = 0
            while count == 0: #проверка на наличие одной масти
                if suit_selected_card == 'diamond':
                    for i in range(len(suit_bot_cards)):
                        suit_bot_card = suit_bot_cards[i]
                        if suit_bot_card == 'diamonds':
                            count += 1
                            print('d')
                            break
                elif suit_selected_card == 'heart': 
                    for i in range(len(suit_bot_cards)):
                        suit_bot_card = suit_bot_cards[i]
                        if suit_bot_card == 'hearts':
                            count += 1
                            print('h')
                            break
                elif suit_selected_card == 'spade': 
                    for i in range(len(suit_bot_cards)):
                        suit_bot_card = suit_bot_cards[i]
                        if suit_bot_card == 'spades':
                            count += 1
                            print('s')
                            break
                elif suit_selected_card == 'club': 
                    for i in range(len(suit_bot_cards)):
                        suit_bot_card = suit_bot_cards[i]
                        if suit_bot_card == 'clubs':
                            count += 1
                            print('c')
                            break
                else:
                    break
            if count == 0: #если масти не совпадают
                index = []
                for i in range(len(suit_bot_cards)):
                    suit_bot_card = suit_bot_cards[i]
                    if suit_bot_card == suit_trump_card:
                        index.append(i)
                if len(index) == 0: #есть ли козырь, чтобы отбить (если нет козыря...)
                    bot_takes_cards(selected_cards,bot_cards, player_cards,number_selected_card)
                else:
                    bot_trump_numbers = [] #поиск минимального козыря
                    for i in range(len(index)):
                        num_index = index[i]
                        bot_trump_card = bot_cards[num_index]
                        bot_trump_num = bot_trump_card.rank
                        bot_trump_numbers.append(bot_trump_num)
                    bot_trump_numbers.sort()
                    selected_bot_card = bot_trump_num[0]+' '+suit_trump_card
                    print('\nThe bot`s card is...\n')
                    time.sleep(1)
                    print(selected_bot_card)
                    for i in range(len(bot_cards)):
                        if selected_bot_card == bot_cards[i]:
                            bot_cards.remove(selected_bot_card)
                            break
            else:
                count = 0
                bot_card_with_same_suit = []
                num_bot_card = []
                for i in range(len(bot_cards)):
                    bot_card = bot_cards[i]
                    if suit_selected_card == bot_card.suit:
                        count += 1
                        bot_card_with_same_suit.append(bot_card)
                        num_bot_card.append(bot_card.rank)
                num_bot_card.sort()
                count_for_check = 0
                while count_for_check != 1:
                    if number_selected_card == '6':
                        for index in range(len(num_bot_card)):
                            card = num_bot_card[index]
                            if card == '7' or card == '8' or card == '9' or card == '10' or card == 'J' or card == 'Q' or card == 'K' or card == 'A':
                                count_for_check += 1
                                break
                    elif number_selected_card == '7':
                        for index in range(len(num_bot_card)):
                            card = num_bot_card[index]
                            if card == '8' or card == '9' or card == '10' or card == 'J' or card == 'Q' or card == 'K' or card == 'A':
                                count_for_check += 1
                                break
                    elif number_selected_card == '8':
                        for index in range(len(num_bot_card)):
                            card = num_bot_card[index]
                            if card == '9' or card == '10' or card == 'J' or card == 'Q' or card == 'K' or card == 'A':
                                count_for_check += 1
                                break
                    elif number_selected_card == '9':
                        for index in range(len(num_bot_card)):
                            card = num_bot_card[index]
                            if card == 'A' or card == 'J' or card == 'Q' or card == 'K' or card == 'A':
                                count_for_check += 1
                                break
                    elif number_selected_card == '10':
                        for index in range(len(num_bot_card)):
                            card = num_bot_card[index]
                            if card == 'J' or card == 'Q' or card == 'K' or card == 'A':
                                count_for_check += 1
                                break
                    elif number_selected_card == 'J':
                        for index in range(len(num_bot_card)):
                            card = num_bot_card[index]
                            if card == 'Q' or card == 'K' or card == 'A':
                                count_for_check += 1
                                break
                    elif number_selected_card == 'Q':
                        for index in range(len(num_bot_card)):
                            card = num_bot_card[index]
                            if card == 'K' or card == 'A':
                                count_for_check += 1
                                break
                    elif number_selected_card == 'K':
                        for index in range(len(num_bot_card)):
                            card = num_bot_card[index]
                            if card == 'A':
                                count_for_check += 1
                                break
                    elif number_selected_card == 'A':
                        bot_takes_cards(selected_cards,bot_cards, player_cards,number_selected_card)
                    else:
                        bot_takes_cards(selected_cards,bot_cards, player_cards,number_selected_card)
                if count_for_check == 0:
                    bot_takes_cards(selected_cards,bot_cards, player_cards,number_selected_card)
                else: 
                    selected_bot_card = card + ' ' + suit_selected_card + 's'
                    print('\nThe bot`s card is...\n')
                    time.sleep(1)
                    print(selected_bot_card)
                    print()
                    for i in range(len(bot_cards)):
                        if selected_bot_card == bot_cards[i]:
                            bot_cards.remove(selected_bot_card)
                            break          
        answer = input('Do you want to put a card on the table?(enter "yes" or "no")\n').lower()
        while answer != 'yes' or answer != 'no':
                if answer == 'yes':
                    add_cards(player_cards,number_selected_card, bot_cards)
                    break
                elif answer == 'no':
                    print('\nOK\n')
                    take_cards(bot_cards,player_cards,cards)
                    print(player_cards)
                    print(bot_cards)
                    break
                else:
                    print("Enter only 'yes' or 'no'!")
                    break        
    
def play_bot_first(bot_cards):
    print('bot start')

def help(): #мейби я потом доработаю правила, но сейчас мне лень переводить всё:)
    print('\nHere are the rules of the game.\n')
    print('The game uses a deck of 36 cards. \nPlayers are dealt 6 cards each, after which a trump card is announced. \nThe player with the lowest trump card goes first. \nThe one "under whom" they go must beat the card. \nThe rest of the participants can throw up cards, the player must beat them all. \nIf he breaks through, then he has the next move, if not, then he takes all the unbroken cards for himself and skips the turn. \nPlayers should always have 6 cards in their hands, they take the missing ones from the deck. \nWhen the deck ends, the players play with the remaining cards in their hands, gradually getting rid of all of them. \nWhoever is left with the cards is a fool.')
main()