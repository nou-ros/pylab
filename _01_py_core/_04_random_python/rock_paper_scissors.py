import random

def play():
    user = input("Choose 'r' for rock, 'p' for paper and 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'
    # r > s, s > p, p > r
    if win(user, computer):
        return 'You won!'

    return 'Computer won!'

def win(player, opponent):
    # return true if player wins
    if (player=='r' and opponent =='s') or (player=='s' and opponent=='p') \
        or (player == 'p' and opponent == 'r'):
        return True

play()