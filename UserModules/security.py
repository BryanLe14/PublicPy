import math,time,os,getpass,sys,datetime,UserModules.InfoComm,UserModules.colorama as colorama
from time import sleep

class SecurityError(Exception):
    def __init__(self, message):
        self.message = message

class request:
    pass
class requestPass(request):
    def __init__(self, password, errDo, passDo, pwDisp="Password: "):
        while True:
            print(colorama.Fore.ORANGE)
            inp = getpass.getpass(pwDisp)
            
            if inp != password:
                if type(errDo) == str and False:
                    #raise SecurityError(errMessage)
                    print(errDo)
                    sys.exit(0)
                errDo()
            elif inp == password:
                #print(passDo)
                passDo()
                break


_passwall=lambda:requestPass("\x50\x72\x6F\x67\x72\x61\x6D\x6D\x69\x6E\x67\x49\x49",lambda:(print(f"Authorizing input...")or sleep(0.2)or print(f"{colorama.Fore.RED}Access denied...")or sleep(0.2)or print(f"{colorama.Fore.RED}Program terminated.")or requestPass("Sorry", lambda:sys.exit(0), lambda:print(f"{colorama.Fore.BLUE}Access restored."), "")), lambda:(print(f"Authorizing input...")or sleep(0.2)or print(f"{colorama.Fore.GREEN}Attempt approved...")or sleep(0.1)or print(f"{colorama.Fore.GREEN}Proceeding to program...{colorama.RESET}\n")or sleep(0.5)))

_longpasswall=lambda:requestPass("\x49\x20\x72\x65\x61\x6C\x6C\x79\x20\x77\x69\x73\x68\x20\x74\x68\x69\x73\x20\x70\x72\x6F\x67\x72\x61\x6D\x20\x77\x65\x72\x65\x20\x74\x6F\x20\x6F\x70\x65\x6E\x20\x74\x68\x79\x20\x73\x65\x73\x61\x6D\x65\x2E",lambda:(print(f"\x41\x75\x74\x68\x6F\x72\x69\x7A\x69\x6E\x67\x20\x69\x6E\x70\x75\x74\x2E\x2E\x2E")or sleep(0.2)or print(f"{colorama.Fore.RED}\x41\x63\x63\x65\x73\x73\x20\x64\x65\x6E\x69\x65\x64\x2E\x2E\x2E")or sleep(0.2)or print(f"{colorama.Fore.RED}\x50\x72\x6F\x67\x72\x61\x6D\x20\x74\x65\x72\x6D\x69\x6E\x61\x74\x65\x64\x2E")or requestPass("\x53\x6F\x72\x72\x79\x20\x73\x65\x73\x61\x6D\x65", lambda:sys.exit(0), lambda:print(f"{colorama.Fore.BLUE}"), "\x41\x63\x63\x65\x73\x73\x20\x72\x65\x73\x74\x6F\x72\x65\x64\x2E")), lambda:(print(f"\x41\x75\x74\x68\x6F\x72\x69\x7A\x69\x6E\x67\x20\x69\x6E\x70\x75\x74\x2E\x2E\x2E")or sleep(0.2)or print(f"{colorama.Fore.GREEN}\x41\x74\x74\x65\x6D\x70\x74\x20\x61\x70\x70\x72\x6F\x76\x65\x64\x2E\x2E\x2E")or sleep(0.1)or print(f"{colorama.Fore.GREEN}\x4F\x70\x65\x6E\x69\x6E\x67\x20\x74\x68\x79\x20\x73\x65\x73\x61\x6D\x65\x2E\x2E\x2E{colorama.RESET}")or sleep(0.5)))

if __name__ == "__main__":
    _passwall()