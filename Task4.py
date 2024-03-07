import random


options = ("rock","paper","scissors")
playing = True

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissors): ")

    print(f"player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("it's a tie!")
    elif player == "scissor" and computer == "paper":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "rock" and computer == "scissor":
        print("You win!")
    else:
        print("you lose!")

    play_again = input("DO you want to play? (y/n) ").lower()
    if not play_again == "y":
        playing = False

print("Thank you for playing")