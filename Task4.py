import random


options = ("rock","paper","scissors")
playing = True
player_score = 0
computer_score = 0

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("\nEnter your choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("it's a tie!")
    elif (
            (player == "scissors" and computer == "paper") or
            (player == "paper" and computer == "rock") or
            (player == "rock" and computer == "scissors")
    ):
        print("You win!")
        player_score += 1
    else:
        print("you lose!")
        computer_score += 1

    print("\nScore Board")
    print(f"Player: {player_score}, Computer: {computer_score}")
    play_again = input("\nDO you want to play? (y/n) ").lower()
    if not play_again == "y":
        playing = False

print("Thank you for playing")