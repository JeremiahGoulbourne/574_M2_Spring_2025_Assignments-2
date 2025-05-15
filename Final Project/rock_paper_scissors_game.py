import random

cpu_score = 0
player_score = 0

def main():
    while True:
        global player_score, cpu_score

        computer = get_computer_choice()
        player = get_user_choice()

        if check_if_invalid_option(player):
            print(f"Error! {player} is an invalid option")
            continue

        result = play(computer, player)
        print(result)

        update_scores(result)

        if player_score == 3 or cpu_score == 3:
            declare_winner()
            break

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    return input("rock, paper or scissors? ").lower()

def check_if_invalid_option(player):
    return player not in ["rock", "paper", "scissors"]

def play(computer, player):
    if computer == player:
        return "It's a tie!"
    elif (computer == "rock" and player == "scissors") or \
         (computer == "paper" and player == "rock") or \
         (computer == "scissors" and player == "paper"):
        global cpu_score
        cpu_score += 1
        return f"Computer wins this round! ({computer} beats {player})"
    else:
        global player_score
        player_score += 1
        return f"You win this round! ({player} beats {computer})"

def update_scores(result):
    global cpu_score, player_score

    if "Computer wins" in result:
        cpu_score += 1
    elif "You win" in result:
        player_score += 1

def declare_winner():
    print("\nFinal Scores:")
    print(f"Computer: {cpu_score}")
    print(f"Player: {player_score}")

    if player_score > cpu_score:
        print("You win the game!")
    else:
        print("Computer wins the game! Better luck next time.")

if __name__ == "__main__":
    main()