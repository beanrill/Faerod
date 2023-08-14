import time
import random

# ------------------------------------------------- ASCII ART ------------------------------------------------- #
def intro_art():
    print(r"""
                   ,   ,
                 ,-`{-`/
              ,-~ , \ {-~~-,
            ,~  ,   ,`,-~~-,`,
          ,`   ,   { {      } }                                             }/
         ;     ,--/`\ \    / /                                     }/      /,/
        ;  ,-./      \ \  { {  (                                  /,;    ,/ ,/
        ; /   `       } } `, `-`-.___                            / `,  ,/  `,/
         \|         ,`,`    `~.___,---}                         / ,`,,/  ,`,;
          `        { {                                     __  /  ,`/   ,`,;
                /   \ \                                 _,`, `{  `,{   `,`;`
               {     } }       /~\         .-:::-.     (--,   ;\ `,}  `,`;
               \\._./ /      /` , \      ,:::::::::,     `~;   \},/  `,`;     ,-=-
                `-..-`      /. `  .\_   ;:::::::::::;  __,{     `/  `,`;     {
                           / , ~ . ^ `~`\:::::::::::<<~>-,,`,    `-,  ``,_    }
                        /~~ . `  . ~  , .`~~\:::::::;    _-~  ;__,        `,-`
               /`\    /~,  . ~ , '  `  ,  .` \::::;`   <<<~```   ``-,,__   ;
              /` .`\ /` .  ^  ,  ~  ,  . ` . ~\~                       \\, `,__
             / ` , ,`\.  ` ~  ,  ^ ,  `  ~ . . ``~~~`,                   `-`--, \
            / , ~ . ~ \ , ` .  ^  `  , . ^   .   , ` .`-,___,---,__            ``
          /` ` . ~ . ` `\ `  ~  ,  .  ,  `  ,  . ~  ^  ,  .  ~  , .`~---,___
        /` . `  ,  . ~ , \  `  ~  ,  .  ^  ,  ~  .  `  ,  ~  .  ^  ,  ~  .  `-,

                    """)

def game_over():
    print(r"""         
       ___   ___  ___  ___  ____      ___   __ __  ____ ____ 
      // \\ // \\ ||\\//|| ||        // \\  || || ||    || \\
     (( ___ ||=|| || \/ || ||==     ((   )) \\ // ||==  ||_//
      \\_|| || || ||    || ||___     \\_//   \V/  ||___ || \\                                                    
       """)

# ------------------------------------------------- ENEMIES ------------------------------------------------- #

def MINOTAUR():
    return 15

def HYDRA():
    return 30

def CHIMERA():
    return 20

def BANSHEE():
    return 20

def CYCLOPS():
    return 25

# ------------------------------------------------- SETUP ------------------------------------------------- #

def HP():
    return 50

def choose_char():
    """
    Prompts user for their choice of character class.

    :return: Returns a string holding the player's character class
    """
    while True:
        choice = int(input("\nChoose your class: \n 1 - Wizard \n 2 - Mage \n 3 - Sorcerer \n 4 - Knight \n"))
        if choice == 1 and validate_choice():
            return "Wizard"
        elif choice == 2 and validate_choice():
            return "Mage"
        elif choice == 3 and validate_choice():
            return "Sorcerer"
        elif choice == 4 and validate_choice():
            return "Knight"

def choose_weapon():
    """
    Prompts user for their choice of weapon.

    :return: Returns players chosen weapon as a string.
    """
    while True:
        choice = int(input("\nChoose your weapon: \n 1 - Sword \n 2 - Crossbow \n 3 - Machete \n 4 - Frying Pan \n"))
        if choice == 1 and validate_choice():
            return "Sword"
        elif choice == 2 and validate_choice():
            return "Crossbow"
        elif choice == 3 and validate_choice():
            return "Machete"
        elif choice == 4 and validate_choice():
            return "Frying Pan"

def player(name, hp, char_class, weapon, location, status):
    """
    Assigns player name, hp, class, weapon, location, and status into a dictionary.

    :param name: a string
    :param hp: an integer
    :param char_class: a string defining the player's character class
    :param weapon: a string depicting the player's weapon
    :param location: a string
    :param status: a string
    :return: Returns a dictionary
    """
    return {"Name": name, "HP": hp, "Class": char_class, "Weapon": weapon, "Location": location, "Status": status}

def create_player():
    """
    Creates a player with class and weapon choices.

    :return: Returns the dictionary of the final created player
    """
    player_name = input("\nWhat would you like to be called oh adventurer? ")
    print(f"\nWelcome, {player_name}! Your adventure awaits in the land of Faerod...")
    player_class = choose_char()
    weapon = choose_weapon()
    created_player = player(player_name, HP(), player_class, weapon, 0, "Alive")
    return created_player

def print_player(character: dict):
    """
    Prints the current player's stats

    :param character: a dictionary
    :return: A string of the player's stats/profile
    """

    print('\033[96m' + "\nSUMMARY"
                       f"\nName: {character['Name']} \n"
                       f"HP: {character['HP']} \n"
                       f"Class: {character['Class']} \n"
                       f"Weapon: {character['Weapon']} \n"
                       f"Location: {character['Location']} \n"
                       f"Status: {character['Status']} \n" + '\033[00m')

# ------------------------------------------------- GAME MECHANICS -------------------------------------------------- #
def introduction():
    print('\033[38;5;123m' + "Welcome to Faerod! A single-user dungeon game where you journey through a magical world filled "
                       "with beasts, treasure, and fairies. \n" + '\033[00m')

def intro_narrative():
    print('\033[38;5;180m' + "You blink." + '\033[00m')
    time.sleep(1)
    print('\033[38;5;180m' + "Blinding rays strike your eyes as the sunshine peaks through the evergreen glades."
          + '\033[00m')
    time.sleep(1)
    print('\033[38;5;222m' +"You pull yourself up from the ground and take in your surroundings. A pair of scuttling rabbits "
          "pass on your right, and above the chickadees sing across the canopy of trees." + '\033[00m')
    time.sleep(1.5)
    print('\033[38;5;222m' + "You turn to make your way down the trodden path back to your cottage and squint ahead."
          + '\033[00m')
    time.sleep(1.5)
    print('\033[38;5;179m' + "Silence. The rays of sun absolve into a tunnel of darkness and a strange cloud of "
          "dense fog whispers your name. " + '\033[00m')
    time.sleep(2)
    print('\033[38;5;179m' + "As you approach, the fog morphs into a barrier with light streaming from within."
          + '\033[00m')
    time.sleep(2)
    print('\033[38;5;179m' + "You take a deep breath and step through......\n" + '\033[00m')
    time.sleep(2)

def instructions():
    print('\033[38;5;123m' + "You have entered the forrest of Faerod and are tasked with returning back to your realm\n"
          + '\033[00m')
    print("\033[38;5;12mInstructions: \n"
          "1) Choose your class based on the selections provided. Your class cannot be changed once chosen.\n"
          "2) Choose your weapon based on the selections provided. Your weapon cannot be changed after starting the "
          "game. \n"
          "3) Your HP level starts at 50 and can increase or decrease as you progress through the game. \n"
          "4) The board is split into 9 squares, each round will prompt you to choose between squares 1-9. \n"
          "5) You may go in any direction you choose within the limitations of the board and can revisit the same spot "
          "more than once.\nIf you land on a spot with a monster that you have previously fought, you may choose to "
          "fight it again.\n"
          "6) When choosing how to proceed at any point, enter the numbers corresponding to the choices provided.\033[00m \n")

def movement(player_dict, monster_dict):
    """
    Movement of player across the board. Selection of number between 1-9 to either fight monster or earn HP increase.

    :param player_dict: a dict representing the player's stats, see player()
    :param monster_dict: a dict representing the monster name and HP see monster_generator()
    :return: none
    """
    number = int(input("Which square would you like to go to? (Pick 1 - 9)\n"))
    monsters = [3, 5, 7, 9]
    # Squares are either fight monster or increase HP
    if number in monsters:
        player_dict['Location'] = number
        combat(player_dict, monster_dict)
    else:
        player_dict['Location'] = number
        player_dict['HP'] += 10
        print("\033[38;5;99mYou stumble upon a Winclamit fruit and take a bite.\033[00m\n\n\033[38;5;141mGain +10 HP.\033[00m ")
        print_player(player_dict)

def monster_generator(number):
    """
    Generate a monster.

    :param number: random int generated by the microservice
    :return: Returns a dict of the monster name and its HP
    """
    if number == 1:
        return {"Monster": "Minotaur", "HP": MINOTAUR()}
    if number == 2:
        return {"Monster": "Hydra", "HP": HYDRA()}
    if number == 3:
        return {"Monster": "Chimera", "HP": CHIMERA()}
    if number == 4:
        return {"Monster": "Cyclops", "HP": BANSHEE()}
    if number == 5:
        return {"Monster": "Banshee", "HP": CYCLOPS()}

def print_monster(monster):
    """
    Prints monster name and HP.

    :param monster: dict value
    :return: none
    """
    print(f"Prepare to fight a\033[38;5;196m {monster['Monster']} \033[00m \n")

def validate_choice():
    """
    Validates player's choice.

    :return: a boolean
    """
    choice = int(input("\033[38;5;193m Are you sure? 1 - Yes | 2 - No \033[00m \n"))
    if choice == 1:
        return True
    else:
        return False

def proceed_or_exit():
    """
    Proceed or exit the game. Use only at start of game.

    :return: returns int
    """
    while True:
        try:
            start_stop = int(input("Type 1 to proceed or 2 to exit: "))
            if start_stop == 1 or start_stop == 2:
                return start_stop
        except ValueError:
            print("Not a number! Please try again.")

def intro():
    intro_art()
    introduction()
    intro_narrative()
    instructions()

def end_game():
    game_over()
    print("\033[38;5;183mThank you for playing! See you next time.\033[00m")

# ------------------------------------------------- COMBAT -------------------------------------------------- #
def attack():
    """
    Determines who attacks who.

    :return: a boolean
    """
    player_roll = random.randint(1, 25)
    monster_roll = random.randint(1, 25)
    while True:
        if player_roll > monster_roll:
            print(f"Player rolls: {player_roll} | Monster rolls: {monster_roll}")
            return True
        else:
            print(f"Player rolls: {player_roll} | Monster rolls: {monster_roll}")
            return False

def check_combat_winner(curr_player, player_hp, monster_hp):
    """
    Checks if player or monster won the combat.

    :param curr_player: a dictionary representing the current player's stats
    :param player_hp: an integer
    :param monster_hp: an integer
    :return: a print statement or none
    """
    if player_hp <= 0:
        # Game over
        curr_player['Status'] = "Dead"
        print("\033[38;5;154mGame over, you have been vanquished!\033[00m")
        end_game()
    elif monster_hp <= 0:
        print("\033[38;5;199mCongratulations! You have defeated the monster!\033[00m")
    else:
        return

def combat_stats(curr_player, curr_hp):
    """
    Checks the combat stats of the player and prints updated summary.

    :param curr_player: a dict of the player
    :param curr_hp: an int
    :return: none
    """
    if curr_hp < 0:
        curr_player['HP'] = 0
    else:
        curr_player['HP'] = curr_hp
    print_player(curr_player)

def combat(curr_player, monster):
    """
    Combat between player and monster

    :param curr_player: a dictionary
    :param monster: a dictionary
    :return: none
    """
    print(f"\n\033[38;5;43mBEGIN COMBAT\033[00m \n"
          f"\033[38;5;155m{curr_player['Name']}\033[00m fights the \033[38;5;160m{monster['Monster']}!\033[00m \n")

    while curr_player['HP'] > 0 and monster['HP'] > 0:
        if attack(): # Player hits monster
            print(f"\033[38;5;155m{curr_player['Name']} strikes the {monster['Monster']}!\033[00m \n")
            monster['HP'] -= 5
        else:
            print(f"\033[38;5;196m{monster['Monster']} attacks {curr_player['Name']}!\033[00m \n")
            curr_player['HP'] -= 7

        print(f"{curr_player['Name']}: {curr_player['HP']} | {monster['Monster']}: {monster['HP']} \n")

        # Check if player or monster died
        check_combat_winner(curr_player, curr_player['HP'], monster['HP'])

    # Print updated stats of player
    combat_stats(curr_player, curr_player['HP'])

# ------------------------------------------------- MICROSERVICE -------------------------------------------------- #
def check_txt_file_contents(file_path, str_to_check):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            if file_content.strip() == str_to_check:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

def write_to_txt_file(file_path, str_to_write):
    try:
        with open(file_path, 'w') as file:
            file.write(str_to_write)
        # print("File written successfully.")
    except Exception as e:
        print(f"Error occurred while writing to the file: {e}")

def read_from_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def run_microservice():
    # Write the request over
    write_to_txt_file("rng_pipe.txt", "request")

    while (check_txt_file_contents("rng_pipe.txt", "request") or
           check_txt_file_contents("rng_pipe.txt", "")):
        time.sleep(1)

    pipe_contents = read_from_txt_file("rng_pipe.txt")
    rng_num = int(pipe_contents)

    # Return the rng_num to use for monster generator
    return rng_num

# ------------------------------------------------- RUN GAME ------------------------------------------------- #
def main():
    # Introduction and instructions
    intro()

    # Run Game
    if proceed_or_exit() == 2:
        end_game()
    else:
        new_player = create_player()
        print_player(new_player)
        while new_player['Status'] == "Alive":
            if proceed_or_exit() == 1:
                # Start microservice
                random_number = run_microservice()
                monster = monster_generator(random_number)
                movement(new_player, monster)
            else:
                end_game()
                break


if __name__ == "__main__":
    main()

