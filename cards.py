import random 
import time

def who_goes_first(trump_card,player_cards,bot_cards):
    suit_trump_card = trump_card[slice(2,-1)]
    suit_player_card = None
    suit_bot_card = None
    player_count = 0
    bot_count = 0
    player_numbers = []
    bot_numbers = []
    for index in range(6): #смотрим кто первый ходит
        suit_player_card_index = player_cards[index]
        suit_bot_card_index = bot_cards[index]
        number_player = suit_player_card_index[slice(1)]
        number_bot = suit_bot_card_index[slice(1)]
        suit_player_card = suit_player_card_index[slice(2,-1)]
        suit_bot_card = suit_bot_card_index[slice(2,-1)]
        if suit_player_card == suit_trump_card:
            player_numbers.append(number_player)
            player_count += 1 
        if suit_bot_card == suit_trump_card:
            bot_numbers.append(number_bot)
            bot_count += 1     
    if bot_count == 0:
        play_player_first(player_cards,bot_cards, suit_trump_card)    #первый ходит игрок         
    elif player_count == 0:
        play_bot_first(bot_cards)              # первый ходит бот
    else:
        lenght_of_list_player = len(player_numbers)
        lenght_of_list_bot = len(bot_numbers)
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
                            if player_numbers[lenght_player] == 'A':
                                player_trump_card = player_numbers[lenght_player]
                                break
                            else:
                                if player_numbers[lenght_player] == 'B':
                                    player_trump_card = player_numbers[lenght_player]
                                    break
                                else:
                                    if player_numbers[lenght_player] == 'D':
                                        player_trump_card = player_numbers[lenght_player]
                                        break
                                    else:
                                        if player_numbers[lenght_player] == 'K':
                                            player_trump_card = player_numbers[lenght_player]
                                            break
                                        else:
                                            if player_numbers[lenght_player] == 'T':
                                                player_trump_card = player_numbers[lenght_player]
                                                break
                                            else:
                                                print('pN')
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
                            if bot_numbers[lenght_bot] == 'A':
                                bot_trum_card = bot_numbers[lenght_bot]
                                break
                            else:
                                if bot_numbers[lenght_bot] == 'B':
                                    bot_trum_card = bot_numbers[lenght_bot]
                                    break
                                else:
                                    if bot_numbers[lenght_bot] == 'D':
                                        bot_trum_card = bot_numbers[lenght_bot]
                                        break
                                    else:
                                        if bot_numbers[lenght_bot] == 'K':
                                            bot_trum_card = bot_numbers[lenght_bot]
                                            break
                                        else:
                                            if bot_numbers[lenght_bot] == 'T':
                                                bot_trum_card = bot_numbers[lenght_bot]
                                                break
                                            else:
                                                print('bN')
        cards_num = ['6', '7', '8', '9', 'A', 'B', 'D', 'K', 'T']
        for index in range(len(cards_num)):
            if player_trump_card == cards_num[index]:
                play_player_first(player_cards,bot_cards, suit_trump_card) #первый игрок в силу меньшего козыря
                break
            elif bot_trum_card == cards_num[index]:
                play_bot_first(bot_cards) #первый бот в силу меньшего козыря
                print('bot start')
                break
            
def prepare_cards(): #подготовка колоды
    class Cards_class:
        def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit
    player_cards = []
    bot_cards = []
    print('\nLet`s gooo\n') #D - дама; B - валет ;) "A "= 10
    Cards_class.rank = ('6', '7', '8', '9', 'A', 'B', 'D', 'K', 'T')
    Cards_class.suit = (' hearts')
    cards = []
    for i in range(len(Cards_class.rank)):
        cards.append(Cards_class.rank[i]+Cards_class.suit)
    Cards_class.suit = (' diamonds')
    for i in range(len(Cards_class.rank)):
        cards.append(Cards_class.rank[i]+Cards_class.suit)
    Cards_class.suit = (' clubs')
    for i in range(len(Cards_class.rank)):
        cards.append(Cards_class.rank[i] + Cards_class.suit)
    Cards_class.suit = (' spades')
    for i in range(len(Cards_class.rank)):
        cards.append(Cards_class.rank[i] + Cards_class.suit)
    random.shuffle(cards)
    take_cards(cards, player_cards, bot_cards)

def take_cards(cards, player_cards, bot_cards):
    print('Jack is B, queen is D') #для пользователя, а то так хрен поймёшь :)
    print('Now you have:\n')
    while len(player_cards) != 6:
        player_cards.append(cards[0])
        cards.remove(cards[0])
    for i in range(len(player_cards)):
        print(player_cards[i])
    while len(bot_cards) != 6:
        bot_cards.append(cards[0])
        cards.remove(cards[0])
    print('\nThe trump card is...\n') #выводит козыря на экран
    trump_card = random.choice(cards)
    print(trump_card)
    print()
    who_goes_first(trump_card,player_cards,bot_cards)
    
    
def bot_takes_cards(selected_card,bot_cards,player_cards,number_selected_card):
    bot_cards.append(selected_card)
    answer = None
    count = 0
    while answer != "no" or count != 6:
        time.sleep(1)
        answer = input('\nThe bot is taking the cards now. \nDo you want to add more cards? (enter "yes" or "no")\n').lower()
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
    else:
        print('OK')

def play_player_first(player_cards, bot_cards, suit_trump_card):
    print(bot_cards) #ПОТОМ УБРАТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Это я сделала для себя шоб понять правильно ли работает :)
    while True:
        print("Choose a card.\n")
        card = input()
        count = 0
        try:
            while len(player_cards) == 6:
                selected_card = card
                player_cards.remove(card)
                break
            break
        except ValueError:
            print('Enter only your card!')
    play_bot(player_cards, bot_cards, suit_trump_card,selected_card)
                        
                    
def play_bot(player_cards, bot_cards, suit_trump_card, selected_card):
        suit_selected_card = selected_card[slice(2,-1)]
        number_selected_card = selected_card[slice(1)]
        count = 0
        suit_bot_card = []
        for index in range(len(bot_cards)):
            suit_bot_card_index = bot_cards[index]
            suit_bot_card.append(suit_bot_card_index[slice(2,-1)])
        number_selected_bot_card = []
        number_bot_trump_card_list = []
        if suit_selected_card == suit_trump_card:
            for index in range(len(bot_cards)):
                bot_card = bot_cards[index]
                suit_bot_card = bot_card[slice(2,-1)]
                number_bot_card = bot_card[slice(1)]
                if suit_bot_card == suit_trump_card:
                    number_bot_trump_card = bot_card[slice(1)]
                    number_bot_trump_card_list.append(number_bot_trump_card)
                    count += 1
                number_selected_bot_card.append(number_bot_card)
            number_bot_trump_card_list.sort()
            if count == 0:
                bot_takes_cards(selected_card,bot_cards,player_cards,number_selected_card)
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
                        bot_takes_cards(selected_card,bot_cards, player_cards,number_selected_card)
                    else:
                        bot_takes_cards(selected_card,bot_cards, player_cards,number_selected_card)
                if count_for_check == 0:
                    bot_takes_cards(selected_card,bot_cards, player_cards,number_selected_card)
                else: 
                    selected_bot_card = card + ' ' + suit_trump_card + 's'
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
                suit_bot_cards.append(bot_card[slice(2,-1)])
                number_bot_cards.append(bot_card[slice(1)])
            count = 0
            while count != 0: #проверка на наличие одной масти
                if suit_selected_card == 'diamond':
                    for i in range(len(suit_bot_cards)):
                        suit_bot_card = suit_bot_cards[i]
                        if suit_bot_card == 'diamond':
                            count += 1
                            break
                elif suit_selected_card == 'heart': 
                    for i in range(len(suit_bot_cards)):
                        suit_bot_card = suit_bot_cards[i]
                        if suit_bot_card == 'heart':
                            count += 1
                            break
                elif suit_selected_card == 'spade': 
                    for i in range(len(suit_bot_cards)):
                        suit_bot_card = suit_bot_cards[i]
                        if suit_bot_card == 'spade':
                            count += 1
                            break
                elif suit_selected_card == 'club': 
                    for i in range(len(suit_bot_cards)):
                        suit_bot_card = suit_bot_cards[i]
                        if suit_bot_card == 'club':
                            count += 1
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
                    bot_takes_cards(selected_card,bot_cards, player_cards,number_selected_card)
                else:
                    bot_trump_numbers = [] #поиск минимального козыря
                    for i in range(len(index)):
                        num_index = index[i]
                        bot_trump_card = bot_cards[num_index]
                        bot_trump_num = bot_trump_card[slice(1)]
                        bot_trump_numbers.append(bot_trump_num)
                    bot_trump_numbers.sort()
                    selected_bot_card = bot_trump_card[0]+' '+suit_trump_card+'s'
                    print('\nThe bot`s card is...\n')
                    time.sleep(1)
                    print(selected_bot_card)
                    print()
                    for i in range(len(bot_cards)):
                        if selected_bot_card == bot_cards[i]:
                            bot_cards.remove(selected_bot_card)
                            break
                    
    
def play_bot_first(bot_cards):
    print('bot start')

def help(): #мейби я потом доработаю правила, но сейчас мне лень переводить всё:)
    print('\nHere are the rules of the game.\n')
    print('The game uses a deck of 36 cards. \nPlayers are dealt 6 cards each, after which a trump card is announced. \nThe player with the lowest trump card goes first. \nThe one "under whom" they go must beat the card. \nThe rest of the participants can throw up cards, the player must beat them all. \nIf he breaks through, then he has the next move, if not, then he takes all the unbroken cards for himself and skips the turn. \nPlayers should always have 6 cards in their hands, they take the missing ones from the deck. \nWhen the deck ends, the players play with the remaining cards in their hands, gradually getting rid of all of them. \nWhoever is left with the cards is a fool.')

print('Hello! Welcome. \nEnter "play" to start the game. \nIf you need help, enter "help".\n')
command = input().lower()

if command == 'play':
    prepare_cards()
elif command == 'help':
    help()
else:
    print('Enter only "play" or "help"!!! >:[')