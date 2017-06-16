#!/usr/bin/python
from updates.updater import updater as updater
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
with open("updates/autoupdater.json") as data_file:   
    try: 
        cversion = json.loads(data_file.read())
        version=cversion["version"]
    except Exception as e:
        print("[ X ] Invalid format in json data: "+e.message)
        exit()

try:
    r = requests.get('https://raw.githubusercontent.com/whitejaguars/eh_training/master/updates/autoupdater.json')
    version_data = json.loads(r.text)
    Print("[ ! ] Current version: "+version,"green")
    if version_data["version"] != version:
        #First release
        if '.' in version_data["version"]:
            major, minor = version_data["version"].split(".")
            cmajor, cminor = version.split(".")
            Print("[ ! ] Downloading updates","green")
            if cmajor != major:
                Print("[ ! ] Downloading major update","green")
                r = requests.get('https://raw.githubusercontent.com/whitejaguars/eh_training/master/updates/'+major+'.0.json')
                update_data = json.loads(r.text)
                updater.download(update_data)
            if cminor != minor:
                for i in range(cminor,minor):
                    r = requests.get('https://raw.githubusercontent.com/whitejaguars/eh_training/master/updates/'+major+'.0.json')
                    update_data = json.loads(r.text)
                    updater.download(update_data)
        else:
            Print("[ X ] Version data is invalid: "+version_data["version"])
except Exception:
    Print("[ X ] Error checking for updates, make sure you have a working internet connection","red")

