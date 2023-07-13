
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
    Prompts user for their choice of character.
    :return: Returns a string
    """
    while True:
        choice = input("Pick your character: \n 1 - Wizard \n 2 - Mage \n 3 - Sorcerer \n 4 - Knight \n")
        if choice == 1:
            choice = "Wizard"
            print(f"Welcome, {choice}! Get ready for an adventure.")
            break
        elif choice == 2:
            choice = "Mage"
            print(f"Welcome, {choice}! Get ready for an adventure.")
            break
        elif choice == 3:
            choice = "Sorcerer"
            print(f"Welcome, {choice}! Get ready for an adventure.")
            break
        elif choice == 4:
            choice = "Knight"
            print(f"Welcome, {choice}! Get ready for an adventure.")
            break

    return choice


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
    # intro_art()
    # introduction()
    # # Narrative
    # player_name = input("What would you like to be called? ")
    # player(player_name, HP(), choose_char(), 5)
    choose_char()


if __name__ == "__main__":
    main()

