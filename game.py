import time

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


def mushroom():
    print(r"""
                  .
                ('
                '|
                |'
               [::]
               [::]   _......_
               [::].-'      _.-`.
               [:.'    .-. '-._.-`.
               [/ /\   |  \        `-..
               / / |   `-.'      .-.   `-.
              /  `-'            (   `.    `.
             |           /\      `-._/      \
             '    .'\   /  `.           _.-'|
            /    /  /   \_.-'        _.':;:/
          .'     \_/             _.-':;_.-'
         /   .-.             _.-' \;.-'
        /   (   \       _..-'     |
        \    `._/  _..-'    .--.  |
         `-.....-'/  _ _  .'    '.|
                  | |_|_| |      | \  (o)
             (o)  | |_|_| |      | | (\'/)
            (\'/)/  ''''' |     o|  \;:;
             :;  |        |      |  |/)
         LGB  ;: `-.._    /__..--'\.' ;:
                  :;  `--' :;   :;
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

def MINOTAUR_HIT():
    return 5

def HYDRA_HIT():
    return 10

def CHIMERA_HIT():
    return 6

def BANSHEE_HIT():
    return 6

def CYCLOPS_HIT():
    return 8

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
        if choice == 1:
            return "Wizard"
        elif choice == 2:
            return "Mage"
        elif choice == 3:
            return "Sorcerer"
        elif choice == 4:
            return "Knight"

def choose_weapon():
    """
    User chooses their weapon.
    :return: Returns players chosen weapon as a string.
    """
    while True:
        choice = int(input("\nChoose your weapon: \n 1 - Sword \n 2 - Crossbow \n 3 - Machete \n 4 - Frying Pan \n"))
        if choice == 1:
            return "Sword"
        elif choice == 2:
            return "Crossbow"
        elif choice == 3:
            return "Machete"
        elif choice == 4:
            return "Frying Pan"

def player(name, hp, char_class, weapon, location):
    """

    :param name: a string
    :param hp: an integer
    :param char_class: a string defining the player's character class
    :param weapon: a string depicting the player's weapon
    :param location: TBD
    :return: Returns an f-string listing the player information
    """
    print('\033[96m' + "\nSUMMARY"
                       f"\nName: {name} \n"
                       f"HP: {hp} \n"
                       f"Class: {char_class} \n"
                       f"Weapon: {weapon} \n"
                       f"Location: {location} \n" + '\033[00m')

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
    print("Instructions: \n"
          "1) Choose your class based on the selections provided. Your class cannot be changed once chosen.\n"
          "2) Choose your weapon based on the selections provided. Your weapon cannot be changed after starting the "
          "game, unless you discover a weapon during gameplay, in which case you have a choice to swap it with your "
          "current weapon or not. \n"
          "3) Your HP level starts at 30 and can increase or decrease as you progress through the game. \n"
          "4) You may go in any direction you choose within the limitations of the board and can revisit the same spot "
          "more than once. If you land on a spot with a monster that you have previously fought, you may choose to "
          "fight it again. \n"
          "5) When choosing how to proceed at any point, enter the numbers corresponding to the choices provided.\n")

def create_player():
    player_name = input("\nWhat would you like to be called oh adventurer? ")
    print(f"\nWelcome, {player_name}! Your adventure awaits in the land of Faerod...")
    player_char = choose_char()
    weapon = choose_weapon()

    player(player_name, HP(), player_char, weapon, None)

def monster_generator(number):
    """Take the random number generated by the microservice and generate the monster"""
    if number == 1:
        print("Prepare to fight a\033[38;5;196m MINOTAUR \033[00m \n")
    if number == 2:
        print("Prepare to fight a\033[38;5;27m HYDRA \033[00m \n")
    if number == 3:
        print("Prepare to fight a\033[38;5;112m CHIMERA \033[00m \n")
    if number == 4:
        print("Prepare to fight a\033[38;5;178m CYCLOPS \033[00m \n")
    if number == 5:
        print("Prepare to fight a\033[38;5;165m BANSHEE \033[00m \n")


def proceed_or_exit():
    while True:
        try:
            start_stop = int(input("Type 1 to proceed or 2 to exit: "))
            if start_stop == 1 or start_stop == 2:
                return start_stop
        except ValueError:
            print("Not a number! Please try again.")

def reverse():
    # May need to merge this function with proceed or exit
    while True:
        try:
            player_choice = int(input("Select: "
                                      "\033[38;5;40m 1 - Next \033[00m | "
                                      "\033[38;5;184m 2 - Back \033[00m | "
                                      "\033[38;5;196m 3 - Exit Game \033[00m \n"))
            if player_choice == 1 or player_choice == 2 or player_choice == 3:
                return player_choice
        except ValueError:
            print("Not a number! Please try again")

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
    # print("Writing 'request' to rng_pipe.txt")
    write_to_txt_file("rng_pipe.txt", "request")

    while (check_txt_file_contents("rng_pipe.txt", "request") or
           check_txt_file_contents("rng_pipe.txt", "")):
        print("Waiting 1 second before checking the pipe...")
        time.sleep(1)

    pipe_contents = read_from_txt_file("rng_pipe.txt")
    rng_num = int(pipe_contents)

    # Now you can use rng_num for your service!
    # print(f"Received {rng_num} from the rng_pipe.txt file")
    # print("Goodbye!")

    # Return the rng_num to use for monster generator
    return rng_num

# ------------------------------------------------- RUN GAME ------------------------------------------------- #


def main():

    # Testing Monster Generator
    # random_number = run_microservice()
    # monster_generator(random_number)

    # Introduction and instructions
    # intro_art()
    # introduction()
    # intro_narrative()
    # instructions()
    proceed = proceed_or_exit()
    # choose_reverse = reverse()

    # Gameplay
    if proceed == 1:
        # Player creation and statistics
        create_player()
        reverse()
    else:
        print("Thank you for playing! See you next time. ")



if __name__ == "__main__":
    main()

