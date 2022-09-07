import math,\
    time,\
    os,\
    getpass,\
    sys,\
    datetime,\
    UserModules.colorama as colorama,\
    UserModules.security as security,\
    UserModules.InfoComm as InfoComm,\
    platform,\
    socket
from time import sleep
from UserModules.security import (_passwall, requestPass)
from UserModules.InfoComm import Put
from UserModules.colorama import (Fore, Back, Font)
In = Put.In
Out = Put.Out
osUname=os.uname()
osName=os.name

def _clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
_clear()

_passwall()

#print("\x1b[31m"+"Hello world!")



#posix.uname_result(sysname='Linux', nodename='d3675cb0a57d', release='4.4.0-1101-aws', version='#112-Ubuntu SMP Thu Jan 9 11:27:02 UTC 2020', machine='x86_64')

tab="  "
#inpt=lambda tabs=0, txt="":input(tab*tabs+txt)





try:lastLogin=lastLogin
except:lastLogin=datetime.datetime.today()

class Terminalator:
    def __init__(s,t):
        s.name = t["name"]
        s.mem = {}
        s.cmnds = {
            "spin": "spin [name] - creates memory [with name]",
            "spout": "spout [keywords] - retrieves memory [for keywords]",
            "sudo": "sudo [commands] - runs commands after requesting the password",
            "help": "help [keywords] - outputs all commands [or keywords] and descriptions",
            "rename": "rename [id] - renames a memory [with id] to an input",
            "change username": "change username [name] - rename your username [with name or] with input"
        }
    def _spin(s, name=None):
        Out(1,f"<{s.name.lower()}.spin>")
        if name == None:
            memName = In(2,"Enter memory name: ")
        else:memName=name.strip();Out(2,"Memory name: "+memName)
        memAttr = In(2,"Enter memory attributes: ")
        s.mem.update({
            memName: ", ".join(memAttr.split(",")),
        })
    def _spout(s,find=""):
        Out(1,f"<{s.name.lower()}.spout>")
        spN=0
        
        for k in s.mem:
            if find in str(k):
                v=s.mem[k]
                Out(2,k+": "+"["+v+"] ")
                spN+=1
        if spN == 0:Out(2,"Insufficient data for a meaningful output.")
    def _help(s,find=""):
        if find == "zen":
            Out(1,f"<{s.name.lower()}.ZEN>")
            Out(2,"""The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!""")
        else:
            Out(1,f"<{s.name.lower()}.help>")
            spN=0
            string=""
            for k in s.cmnds:
                if find in str(k):
                    v="      "+s.cmnds[k]
                    string+=v+"\n"
                    spN+=1
            if spN == 0:Out(2,"Invalid search.")
            else:
                Out(2,f"""Brackets represent an optional argument
    Angle brackets represent a required argument
    
    Help:
{string}""")
        

rattle=Terminalator({"name":"Rattle"})

_spin=lambda name=None:rattle._spin(name)
_spout=lambda find="":rattle._spout(find)
_help=lambda find="":rattle._help(find)

#spin()
#spout()



username=osUname.sysname
username=platform.platform()
username=osUname.sysname+"-"+socket.gethostbyname(socket.gethostname())

Put.Out("", "Welcome to Programming II\nType \"help\" for commands\n")

while True:
    food=In(0,Fore.BLUE+str(username)+": ").strip()
    while food.find("  ") != -1: food = food.replace("  ", "")
    f=feed=food.split(" ")
    
    
    trueFeed = []
    for i in reversed(range(len(feed))):
        trueFeed.append(feed[i])
        feed[i] = feed[i].lower()
        if feed[i] == "sudo" and feed[0] != "help":
            feed.remove("sudo")
            _passwall()
    f=feed
    
    for k in range(len(f)):
        key=f[k]
        
        if key == "help" or key == "rattle.help" or key == "rattle.help":
            if len(feed) >= 2:
                _help(" ".join(feed[1:]))
            elif len(feed) == 1:
                _help()
        elif key == "spin" or key == "rattle.spin" or key == "rattle.spin":
            if len(feed) >= 2:
                _spin(" ".join(feed[1:]))
            elif len(feed) == 1:
                _spin()
        elif key == "spout" or key == "rattle.spout" or key == "rattle.spout":
            if len(f) == 0:
                _spout()
            else:
                _spout(" ".join(f[1:]))
        elif key == "lock": _passwall()
        elif key == "quit" or key == "exit": sys.exit(0)
        elif key == "rename":
            id_ = input("Enter the name of the memory to be renamed: ")
            if id_ in rattle.mem:
                if len(feed) >= 2:
                    rattle.mem[" ".join(reversed(trueFeed[:-1]))] = rattle.mem.pop(id_)
                else:
                    newName = input("Enter the new name: ")
                    rattle.mem[newName] = rattle.mem.pop(id_)
        elif len(f) > 1 and k < len(f)-2 and (key+" "+f[k+1] == "rename username" or key+" "+f[k+1] == "change username"):
            if len(feed) >= 2:
                username = "-".join(reversed(trueFeed[:-1]))
            else:
                username = In(2, "Enter new username: ")
        else:continue;