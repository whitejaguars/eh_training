#!/usr/bin/python
import platform, requests, json
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
    print(ccolor+txt+bcolors.ENDC)
banner  = "" \
"     __    __   __   __   __   ________   ______    \n" \
"    |##|  |##| |##| |##| |##| |########| |######|   \n" \
"    |##|  |##| |##|_|##| |##|    |##|    |##|___    \n" \
"    |  |/\|  | |   _   | |  |    |  |    |   ___|   \n" \
"    |########| |##| |##| |##|    |##|    |##|       \n" \
"    |###/\###| |##| |##| |##|    |##|    |##|___    \n" \
"    |__/  \__| |__| |__| |__|    |__|    |______|   \n" \
"                __                                    \n" \
"               |  |             _______   __   __              _______      ______ \n" \
"               |  |     /\     |   ____| |  | |  |     /\     |   __  \    /  ___ |\n" \
"               |  |    /  \    |  |  __  |  | |  |    /  \    |  | _\  \  |  |___\|\n" \
"           __  |  |   /    \   |  | /_ | |  | |  |   /    \   |  | \  /    \___  \ \n" \
"          |  |_|  |  /  /\  \  |  |__| | |  |_|  |  /  /\  \  |  |  \  \  |\___|  |\n" \
"          |_______| /__/  \__\ |_______| |_______| /__/  \__\ |__|   \__\ |______/ \n" \
"                                                                                   \n" \
"                                                           AppSec S.C, Costa Rica  \n" \
"                                                                                   \n"
Print(banner,"blue")
try:
    r = requests.get('https://raw.githubusercontent.com/whitejaguars/eh_training/master/updates/autoupdater.json')
    version_data = json.loads(r.text)
    if version_data["version"] != "1.0":
        #First release
        Print("[ ! ] Downloading updates","green")
except Exception:
    Print("[ X ] Error checking for updates, make sure you have a working internet connection","red")

