import random


def get_computer_move():
    moves = ['R', 'P', 'S']
    return random.choice(moves)


def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "It's a tie!", 0, 0
    elif (player_move == 'R' and computer_move == 'S') or \
            (player_move == 'P' and computer_move == 'R') or \
            (player_move == 'S' and computer_move == 'P'):
        return "You win!", 1, 0
    else:
        return "Computer wins!", 0, 1


def main():
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0
    computer_score = 0

    while True:
        player_move = input("Enter your move (R for Rock, P for Paper, S for Scissors, Q to quit): ").upper()
        if player_move == 'Q':
            print("Thanks for playing!")
            print(f"Final Score - You: {player_score}, Computer: {computer_score}")
            break
        if player_move not in ['R', 'P', 'S']:
            print("Invalid input. Please enter R, P, or S.")
            continue

        computer_move = get_computer_move()
        print(f"Computer chose: {computer_move}")

        result, player_point, computer_point = determine_winner(player_move, computer_move)
        player_score += player_point
        computer_score += computer_point

        print(result)
        print(f"Current Score - You: {player_score}, Computer: {computer_score}\n")


if __name__ == "__main__":
    main()
