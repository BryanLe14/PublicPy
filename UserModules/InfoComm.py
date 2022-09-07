import UserModules.colorama as colorama
tab="  "
class Put:
    def In(indent, txt):
        if indent==0:indent=""
        elif type(indent)==int:indent=tab*indent
        else:indent=""+indent[0:]
        return input(f"{indent}{txt}{colorama.RESET}")
    def Out(indent, txt):
        if indent==0:indent=""
        elif type(indent)==int:indent=tab*indent
        else:indent=""+indent[0:]
        return print(f"{indent}{txt}{colorama.RESET}")