import random


def main():
    valid_choices = ['R', 'P', 'S']

    # Play
    # Guest choice
    while True:
        guest_choice = input("[R]ock, [P]aper, [S]cissors? ")
        if guest_choice.upper() in valid_choices:
            guest_choice = to_rock_paper_scissors(guest_choice)
            print(f"You chose: {guest_choice}")
            break
        else:
            print("Hey, you gotta choose a letter: [R]ock, [P]aper or [S]cissors!")

    # PC choice
    pc_choice = random.choice(valid_choices)
    pc_choice = to_rock_paper_scissors(pc_choice)
    print(f"Pc chose: {pc_choice}")

    tie = "It's a tie!"
    guest_won = "You are the winner!"
    pc_won = "PC is the winner!"

    guest_choice = from_rock_paper_scissors(guest_choice)
    pc_choice = from_rock_paper_scissors(pc_choice)

    # Winner
    if guest_choice == pc_choice:
        print(tie)
    elif guest_choice.upper() == "R" and pc_choice == "P":
        print(pc_won)
    elif guest_choice.upper() == "S" and pc_choice == "R":
        print(pc_won)
    elif guest_choice.upper() == "P" and pc_choice == "S":
        print(pc_won)
    else:
        print(guest_won)

    print("Thanks for playing!")

def to_rock_paper_scissors(s):
    if s.upper() == "S":
        s = "Scissors"
    elif s.upper() == "P":
        s = "Paper"
    elif s.upper() == "R":
        s = "Rock"
    return s

def from_rock_paper_scissors(s):
    if s == "Scissors":
        s = "S"
    elif s == "Paper":
        s = "P"
    elif s == "Rock":
        s = "R"
    return s

main()
