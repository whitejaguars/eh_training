#!/usr/bin/python
from subprocess import call
class updater():
    def download(self,recipe):
        for update in recipe:
            if update["action"] == "run":
                return_code = call("echo Hello World", shell=True) 
                print("Return Code: "+str(return_code))