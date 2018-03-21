import random
import time


def main():
    print("Would you like to play Rock, Paper, Scissors or Flip a coin a bunch?")
    game = input('''Enter "RPS" to play Rock, Paper, Scissors or "Coin" to play coin flip''').lower()
    if game == 'rps':
        rps()
    elif game == 'coin':
        coin_flip()
    else:
        print("Invalid choice, try again.")
        time.sleep(1)
        main()


def rps():

    player_score = 0
    computer_score = 0

    new_game = 'yes'

    while new_game == 'yes':

        player = input('''Select "rock", "paper", or "scissors"''').lower()
        computer = (random.choice(['rock', 'paper', 'scissors']))

        beat_me_dict = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}

        if player in beat_me_dict:
            if player == computer:
                print("Tie!")
                print(player_score, "-", computer_score)
                time.sleep(1)
                new_game = input('''New game? Enter "yes" to play again.''').lower()
                if new_game != 'yes':
                    main()
            elif computer == beat_me_dict[player]:
                computer_score += 1
                print("Computer wins")
                print(player_score, "-", computer_score)
                time.sleep(1)
                new_game = input('''New game? Enter "yes" to play again.''').lower()
                if new_game != 'yes':
                    main()
            else:
                player_score += 1
                print("Player wins")
                print(player_score, "-", computer_score)
                time.sleep(1)
                new_game = input('''New game? Enter "yes" to play again.''').lower()
                if new_game != 'yes':
                    main()
        else:
            print("Invalid entry, try again.")
            new_game = 'yes'


def coin_flip():
    amount = int(input("How many times do you want to flip the coin?"))
    print("Total amount of times the coin was flipped:", amount)

    heads = 0
    tails = 0

    while amount >= 0:
        coin = (random.choice(['Heads', 'Tails']))
        if amount == 0:
            print("Heads total:", heads)
            print("Tails total:", tails)
            time.sleep(2)
            main()
        elif coin == 'Heads':
            heads += 1
            amount -= 1
        else:
            tails += 1
            amount -= 1


if __name__ == '__main__':
    main()
