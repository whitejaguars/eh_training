#!/usr/bin/python
import hashlib, platform
class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    lightblue='\033[94m'
    pink='\033[95m'
    lightcyan='\033[96m'


def Print(txt,col=None):
    ccolor = bcolors.ENDC
    if col == None or platform.system() == 'Windows':
        print(txt)
        return
    elif col == 'red':
        ccolor = bcolors.RED
    elif col == 'green':
        ccolor = bcolors.GREEN
    elif col == 'orange':
        ccolor = bcolors.ORANGE
    elif col == 'blue':
        ccolor = bcolors.cyan
    print ccolor+txt+bcolors.ENDC
banner  = "" \
"     __    __   __   __   __   ________   ______    \n" \
"    |##|  |##| |##| |##| |##| |########| |######|   \n" \
"    |##|  |##| |##|_|##| |##|    |##|    |##|___    \n" \
"    |  |/\|  | |   _   | |  |    |  |    |   ___|   \n" \
"    |########| |##| |##| |##|    |##|    |##|       \n" \
"    |###/\###| |##| |##| |##|    |##|    |##|___    \n" \
"    |__/  \__| |__| |__| |__|    |__|    |______|   \n" \
"                __                                    \n" \
"               |  |             _______   __   __              _______      ______      \n" \
"               |  |     /\     |   ____| |  | |  |     /\     |   __  \    /  ___ |     \n" \
"               |  |    /  \    |  |  __  |  | |  |    /  \    |  | _\  \  |  |___\|     \n" \
"           __  |  |   /    \   |  | /_ | |  | |  |   /    \   |  | \  /    \___  \      \n" \
"          |  |_|  |  /  /\  \  |  |__| | |  |_|  |  /  /\  \  |  |  \  \  |\___|  |     \n" \
"          |_______| /__/  \__\ |_______| |_______| /__/  \__\ |__|   \__\ |______/      \n" \
"                                                                                        \n" \
"                                                           Mario Robles, Costa Rica     \n" \
"                                                                                        \n"
Print(banner,"blue")
Print("Cual es el codigo de la pregunta ?","red")
Print(" [ ! ] Solo numeros, sin espacios ni caracteres del alfabeto","orange")
nombre = raw_input("Codigo : ")
hash_object = hashlib.sha256(nombre.encode())
hex_dig = hash_object.hexdigest()
Print("\nSu respuesta es: "+bcolors.RED+ hex_dig+"\n","blue")
print("**********************************************************************************************")
print("* "+bcolors.cyan+"Recuerde que si brinda datos diferentes la respuesta puede ser considerada como incorrecta"+bcolors.ENDC+" *")
print("**********************************************************************************************")