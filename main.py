import random
from static_data import LETTERS, NUMBERS, SYMBOLS

CHARACTER_SETS = [["letters", LETTERS], ["numbers", NUMBERS], ["symbols", SYMBOLS]]


def main():
    print("Welcome to the PyPassword Generator!")

    characters = []

    for character_set in CHARACTER_SETS:

        set_name = character_set[0]
        set = character_set[1]

        state = True
        user_input = 0

        while state:
            user_input = input(
                f"Enter number of {set_name} you would ike in your password: "
            )

            try:
                for i in range(1, int(user_input) + 1):
                    idx = random.randint(0, len(set) - 1)
                    characters.append(set[idx])

            except:
                print("Huh?")
                continue

            state = False

    password = ""
    for i in range(1, len(characters) + 1):
        idx = random.randint(0, len(characters) - 1)
        char = characters.pop(idx)
        password += char

    print(f"\nYour password is: {password}")


if __name__ == "__main__":
    main()
