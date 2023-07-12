
# CONSTANTS


def HP():
    return 30


def MINOTAUR_HIT():
    return 5


# ENEMIES


def MINOTAUR():
    return 15


def HYDRA():
    return 30


def CHIMERA():
    return 20


def CYCLOPS():
    return 25


# CHARACTERS
def MAGICIAN():
    return

# WEAPONS


# SETUP

def board():
    pass


def player(name, hp, character, location, ):
    print('\033[96m' + f"\nName: {name} \n"
                       f"HP: {hp} \n"
                       f"Character: {character} \n"
                       f"Location: {location} \n" + '\033[00m')

# GAME MECHANICS


def introduction():
    print('\033[94m' + "Welcome to Faerod! A single-user dungeon game where you journey through a magical world filled "
                       "with beasts, treasure, and fairies. \n" + '\033[00m')


def intro_narrative():
    pass


# RUN GAME


def main():
    introduction()
    # Narrative
    player_name = input("What would you like to be called? ")
    player(player_name, HP(), "Mage", 5)


if __name__ == "__main__":
    main()

