
def main():

    continue_playing = True

    while ______:
        user1 = _____("Player 1: What's your name?")
        user2 = _____("Player 2: What's your name?")
        user1_answer = _____(f"{_____}, do yo want to choose rock, paper or scissors?")
        user2_answer = _____(f"{_____}, do you want to choose rock, paper or scissors?")

        if user1_answer == user2_answer:
            solution = "It's a tie!"
        elif user1_answer == 'rock':
            if ___________ == 'scissors':
                solution = "Rock wins!"
            else:
                solution = "___________"
        elif __________ == 'scissors':
            if user2_answer == '________':
                solution = "Scissors win!"
            else:
                ________ = "Rock wins!"
        elif _________ == 'paper':
            if user2_answer == 'rock':
                solution = "Paper wins!"
            else:
                solution = "Scissors win!"
        else:
            solution = "Invalid input! You have not entered rock, paper or scissors, try again."

        print(________)

        keep_playing = input("Do you want to continue playing? (Y/N)")

        if ________:
            continue_playing = True
        else:
            continue_playing = False


if __name__ == "__main__":
    main()