import random

champion = {"Rock": 'r', "Paper": 'p', "Scissors": 's', "Lizard": 'l', "Spock": 'sp'}
champion_lookup = dict((v, k) for k, v in champion.items())


def is_win(player, opponent):
    blackboard = {'s': ['p', 'l'], 'p': ['r', 'sp'], 'r': ['l', 's'], 'l': ['sp', 'p'], 'sp': ['s', 'r']}
    return opponent in blackboard.get(player, [])


def select_weapon():
    while True:
        user = input("Choose your weapon:\n{}\n".format(','.join(champion)))
        if user.title() in champion:
            return champion[user.title()]


def play():
    user_selection = select_weapon()
    computer_selection = random.choice(['r', 'p', 's', 'l', 'sp'])

    if user_selection == computer_selection:
        return "It's a tie!", user_selection, computer_selection
    elif is_win(user_selection, computer_selection):
        return 'You won!', user_selection, computer_selection
    else:
        return 'You Lost', user_selection, computer_selection


def play_multi():
    while True:
        message, champion_choice, computer = play()
        print(message)
        print('Champion weapon {}\nOpponent weapon {}'.format(champion_lookup[champion_choice],
                                                              champion_lookup[computer]))

        again = str(input("Do you want to play again, type yes or no "))

        if again.lower() != "yes":
            break


play_multi()

# To add: Different Levels, Item Rewards, Best of Functionality
# Add a UI
# Long Term Goal: Player vs Player using sockets
