import random

print('Hello! Welcome. \nEnter "play" to start the game. \nIf you need help, enter "help".\n')
key = input().lower()

def play_player(player_cards):
    while True:
        print("Choose a card.")
        card = input().lower()
        count = 0
        for x in range(6):
            if card == player_cards[x]:
                count += 1
                break
            else:
                continue
        while len(player_cards) == 6:
            if count == 0:
                print('Enter only your card!')
                break
            else:
                selected_card = card
                player_cards.remove(card)
                print(player_cards)
                print(selected_card)
                break
        break
    suit_selected_card = selected_card[slice(2,-1)]
    number_selected_card = selected_card[slice(1)]
    count = 0
    if suit_selected_card == suit_trump_card:
        print('sc')
        #if 
    
def play_bot_first():
    print('bot')

def help():
    print('\nHere are the rules of the game.\n')
    print('The game uses a deck of 36 cards. \nPlayers are dealt 6 cards each, after which a trump card is announced. \nThe player with the lowest trump card goes first. \nThe one "under whom" they go must beat the card. \nThe rest of the participants can throw up cards, the player must beat them all. \nIf he breaks through, then he has the next move, if not, then he takes all the unbroken cards for himself and skips the turn. \nPlayers should always have 6 cards in their hands, they take the missing ones from the deck. \nWhen the deck ends, the players play with the remaining cards in their hands, gradually getting rid of all of them. \nWhoever is left with the cards is a fool.')

if key == 'play':
    player_cards = []
    bot_cards = []
    print('\nLet`s gooo\n') #D - дама; B - валет ;) "A "= 10
    cards = ['6 hearts', '7 hearts', '8 hearts', '9 hearts', 'A hearts', 'B hearts', 'D hearts', 'K hearts', 'T hearts','6 diamonds', '7 diamonds', '8 diamonds', '9 diamonds', 'A diamonds', 'B diamonds', 'D diamonds', 'K diamonds', 'T diamonds', '6 clubs', '7 clubs', '8 clubs', '9 clubs', 'A clubs', 'B clubs', 'D clubs', 'K clubs', 'T clubs', '6 spades', '7 spades', '8 spades', '9 spades', 'A spades', 'B spades', 'D spades', 'K spades', 'T spades']
    random.shuffle(cards)
    print('Now you have:\n')
    for i in range(6):
        i = random.choice(cards)
        cards.remove(i)
        print(i)
        player_cards.append(i)
    for l in range(6):
        l = random.choice(cards)
        cards.remove(l)
        bot_cards.append(l)
    print('\nThe trump card is...\n')
    trump_card = random.choice(cards)
    print(trump_card)
    print()
    number = trump_card[slice(1)]
    suit_trump_card = trump_card[slice(2,-1)]
    suit_player_card = None
    suit_bot_card = None
    player_count = 0
    bot_count = 0
    player_numbers = []
    bot_numbers = []
    for index in range(6):
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
        play_player(player_cards)            
    elif player_count == 0:
        play_bot_first()              
    else:
        lenght_of_list_player = len(player_numbers)
        lenght_of_list_bot = len(bot_numbers)
        player_numbers.sort()
        player_trump_card = None
        for lenght_player in range(lenght_of_list_player):
            if player_numbers[lenght_player] == '6':
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
                play_player(player_cards)
                break
            elif bot_trum_card == cards_num[index]:
                play_bot_first()
                print('bot start')
                break
elif key == 'help':
    help()
else:
    print('Enter only "play" or "help"!!! >:[')