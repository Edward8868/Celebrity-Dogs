import random
import time


def mainmenu():
    print('Welcome to Celebrity dogs!')
    print('1. Start Game\n2. Quit Game')
    choice = str(input('Please choose one of the options above\n>>> '))
    if choice == '1':
        numcards()
    elif choice == '2':
        print('Thank you for playing Celebrity Dogs!')
        quit()
    else:
        print('That value is not 1 or 2')
        mainmenu()


def numcards():
    print(
        '\nINTRUCTIONS\nThis is a python made copy of Top Trumps\nThe stats to choose from are: exercise, intelligence, friendliness'
        ', and amount of drool\nThe cards are formatted as: Name / Exercise value / Intelligence value / friendliness value'
        ' / Drool produced value\nExercise is rated from 1-5\nIntelligence is rated from 1-100\nFriendliness is rated from 1-5'
        '\nDrool produced is rated from 1-10')
    numofcards = int(input(
        '\nPlease input the number of cards you would like to play with, the number has to be between 4 and 30 and must be even\n>>>  '))
    if 4 <= numofcards <= 30:
        if numofcards % 2 == 0:
            print('\nYou will be playing with', numofcards, 'cards\nEach you and the computer will have',
                  numofcards // 2, 'cards\n')
        else:
            print('Your value is an odd number, please make sure it is even.')
            mainmenu()
    else:
        print('Please make sure your number is between 4 and 30')
        mainmenu()
    file = open("C:\\Users\\edwar\\OneDrive\\Documents\\Stuff\\dogs.txt", "r")
    dog_names_list = [(line.strip()).split() for line in file]
    file.close()
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, ac, ad = dog_names_list
    var = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, ac, ad]
    cards_used = random.sample(var, numofcards)
    random.shuffle(cards_used)
    for i in (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, ac, ad):
        i.append(random.randint(1, 5))
        i.append(random.randint(1, 100))
        i.append(random.randint(1, 10))
        i.append(random.randint(1, 10))
    player_cards = cards_used[:len(cards_used) // 2]
    computer_cards = cards_used[len(cards_used) // 2:]

    game(player_cards, computer_cards)


def game(player_cards, computer_cards):
    win = True
    player_win = '.\nYour card and the computers has been moved to the back of your pile'
    comp_win = '.\nYour card and the computer have been moved to the back of the computers pile'
    while len(player_cards) > 0 and len(computer_cards) > 0:
        if win:
            print('\nThese are your cards, you are using the first card in the list for this round:')
            print(player_cards[0])
            stat = input(
                '\nPlease choose which stat you want to use: E for exercise, I for intelligence, F for friendliness, D for drool\n>>> ').lower()
        if not win:
            cate = ['e', 'i', 'f', 'd']
            stat = random.choice(tuple(cate))
            print('\nThe computer is choosing the stat for this round')
            time.sleep(3)
            print('\nThe card, you are using this round:')
            print(player_cards[0])
        if stat == 'e':
            var1, var2 = player_cards[0], computer_cards[0]
            if player_cards[0][1] >= computer_cards[0][1]:
                print('\nWell done you won this round, the computers exercise was', computer_cards[0][1], player_win)
                win = True
                player_cards.append(var1)
                player_cards.append(var2)
            else:
                print('\nYou lost this round, the computers exercise was', computer_cards[0][1], comp_win)
                win = False
                computer_cards.append(var1)
                computer_cards.append(var2)
            computer_cards.pop(0)
            player_cards.pop(0)
        if stat == 'i':
            var1, var2 = player_cards[0], computer_cards[0]
            if player_cards[0][2] >= computer_cards[0][2]:
                print('\nWell done you won this round, the computers intelligence was', computer_cards[0][2],
                      player_win)
                win = True
                player_cards.append(var1)
                player_cards.append(var2)
            else:
                print('\nYou lost this round, the computers intelligence was', computer_cards[0][2], comp_win)
                win = False
                computer_cards.append(var1)
                computer_cards.append(var2)
            computer_cards.pop(0)
            player_cards.pop(0)
        if stat == 'f':
            var1, var2 = player_cards[0], computer_cards[0]
            if player_cards[0][3] >= computer_cards[0][3]:
                print('\nWell done you won this round, the computers friendliness was', computer_cards[0][3],
                      player_win)
                win = True
                player_cards.append(var1)
                player_cards.append(var2)
            else:
                print('\nYou lost this round, the computers friendliness was', computer_cards[0][3], comp_win)
                win = False
                computer_cards.append(var1)
                computer_cards.append(var2)
            computer_cards.pop(0)
            player_cards.pop(0)
        if stat == 'd':
            var1, var2 = player_cards[0], computer_cards[0]
            if player_cards[0][4] <= computer_cards[0][4]:
                print('\nWell done you won this round, the computers drool was', computer_cards[0][4], player_win)
                win = True
                player_cards.append(var1)
                player_cards.append(var2)
            else:
                print('\nYou lost this round, the computers drool was', computer_cards[0][4], comp_win)
                win = False
                computer_cards.append(var1)
                computer_cards.append(var2)
            computer_cards.pop(0)
            player_cards.pop(0)
        elif stat != 'e' or 'i' or 'f' or 'd':
            print('That is not a valid value')
    if win:
        print('\nWell done you won')
        mainmenu()
    else:
        print('\nYou lost')
        mainmenu()


mainmenu()
