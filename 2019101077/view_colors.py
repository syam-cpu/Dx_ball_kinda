import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
SCREEN=200


def view_colours():
    print(Fore.WHITE + Back.BLACK + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.BLUE + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.CYAN + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.GREEN + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTBLACK_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTBLUE_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTCYAN_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTGREEN_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTRED_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTWHITE_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTYELLOW_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.MAGENTA + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.RED + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.WHITE + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.YELLOW + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    
def view_colours2():
    print(Fore.WHITE + Back.LIGHTWHITE_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.MAGENTA + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTCYAN_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTBLUE_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTBLACK_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTGREEN_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.RED + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTRED_EX + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTYELLOW_EX+ Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    print(Fore.WHITE + Back.YELLOW + Style.BRIGHT + "               ".center(SCREEN)+Style.RESET_ALL)
    
#view_colours()

#view_colours2()
BEAM1=Fore.LIGHTGREEN_EX+" ______O______"
BEAM3=Fore.LIGHTGREEN_EX+"(_____________)"
print(BEAM1)
print(BEAM3)