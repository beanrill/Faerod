
# CONSTANTS

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


def HP():
    return 30


def MINOTAUR_HIT():
    return 5


def HYDRA_HIT():
    return 10


def CHIMERA_HIT():
    return 6


def CYCLOPS_HIT():
    return 8


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


def choose_char():
    """
    Prompts user for their choice of character class.
    :return: Returns a string holding the player's character class
    """
    while True:
        choice = int(input("\nChoose your class: \n 1 - Wizard \n 2 - Mage \n 3 - Sorcerer \n 4 - Knight \n"))
        if choice == 1:
            choice = "Wizard"
            break
        elif choice == 2:
            choice = "Mage"
            break
        elif choice == 3:
            choice = "Sorcerer"
            break
        elif choice == 4:
            choice = "Knight"
            break
    return choice


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

# GAME MECHANICS


def introduction():
    print('\033[94m' + "Welcome to Faerod! A single-user dungeon game where you journey through a magical world filled "
                       "with beasts, treasure, and fairies. \n" + '\033[00m')


def intro_narrative():
    # Breaking print statements up for the narrative so some time sleeps can be inserted later on.
    print("You blink.")
    print("Blinding rays strike your eyes as the sunshine peaks through the evergreen glades.")
    print("You pull yourself up from the ground and take in your surroundings. A pair of scuttling rabbits pass on your "
          "right, and above the chickadees sing across the canopy of trees.")
    print("You turn to make your way down the trodden path back to your cottage and squint ahead.")
    print("Silence. The rays of sun absolve into a tunnel of darkness and a strange cloud of "
          "dense fog whispers your name. ")
    print("As you approach, the fog morphs into a barrier with light streaming from within.")
    print("You take a deep breath and step through......")


def instructions():
    print("You have entered the forrest of Faerod and are tasked with returning back to your realm")
    print("Instructions: \n"
          "1) Choose your class based on the selections provided. Your class cannot be changed once chosen.\n"
          "2) Choose your weapon based on the selections provided. Your weapon cannot be changed after starting the game"
          "unless you discover a weapon during gameplay, in which case you have a choice to swap it with your current"
          "weapon or not. \n"
          "3) Your HP level starts at 30 and can increase or decrease as you progress through the game. \n"
          "4) You may go in any direction you choose within the limitations of the board and can revisit the same spot"
          "more than once. If you land on a spot with a monster that you have previously fought, you may choose to "
          "fight it again. \n"
          "5) When choosing how to proceed at any point, enter the numbers corresponding to the choices provided. \n")


def proceed_or_exit():
    player_input = input("Type")

# RUN GAME


def main():
    # Introduction and instructions
    intro_art()
    introduction()
    intro_narrative()
    instructions()
    # Player creation and statistics
    player_name = input("\nWhat would you like to be called? ")
    print(f"\nWelcome, {player_name}! Your adventure awaits in the land of Faerod..")
    player_char = choose_char()
    player(player_name, HP(), player_char, None, None)


if __name__ == "__main__":
    main()

