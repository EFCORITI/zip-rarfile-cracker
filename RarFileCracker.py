# mmd
import rarfile
import sys
from colorama import Fore
import termcolor2

rarfile.UNRAR_TOOL = "unrar"
print(""" 

 ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗     ██████╗  █████╗ ██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗
██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝    ██████╔╝███████║██████╔╝
██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗    ██╔══██╗██╔══██║██╔══██╗
╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║    ██║  ██║██║  ██║██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                    

 """)
print(Fore.BLUE)
print(""" 

 .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| | ____    ____ | || | ____    ____ | || |  ________    | |
| ||_   \  /   _|| || ||_   \  /   _|| || | |_   ___ `.  | |
| |  |   \/   |  | || |  |   \/   |  | || |   | |   `. \ | |
| |  | |\  /| |  | || |  | |\  /| |  | || |   | |    | | | |
| | _| |_\/_| |_ | || | _| |_\/_| |_ | || |  _| |___.' / | |
| ||_____||_____|| || ||_____||_____|| || | |________.'  | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' 
 """)
print(Fore.CYAN)
print(""" 

 .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| |      __      | || |   _____      | || |     _____    | |
| |     /  \     | || |  |_   _|     | || |    |_   _|   | |
| |    / /\ \    | || |    | |       | || |      | |     | |
| |   / ____ \   | || |    | |   _   | || |      | |     | |
| | _/ /    \ \_ | || |   _| |__/ |  | || |     _| |_    | |
| ||____|  |____|| || |  |________|  | || |    |_____|   | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' 

 """)
print(termcolor2.colored(" Coded By Ali and Mmd",color="red"))

print(termcolor2.colored("      efcoriti channel in the tel >> @efcoriti_programmer",color="green"))

print(termcolor2.colored("		rubika & telegram_id_ali >> @efcoriti",color="cyan"))

print(termcolor2.colored("			rubika id_mmd >> @exploite",color="white"))

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
rarFile = input(Fore.YELLOW +"ENTER YOUR RAR FILE => ")
passwordlist_address = input(Fore.YELLOW+"ENTER THE PASSWORD LIST => ")


rar_file = rarfile.RarFile(rarFile)

passwordlist = open(passwordlist_address)

password_found = False
print("-------------------------------")
for password in passwordlist:
    password = password.strip("\n")
    print("Testing : {}".format(password))
    try:
        rar_file.setpassword(password)
        rar_file.testrar()
        print("*"*50)
        print("Password : {}".format(password))
        password_found = True
        break
    except:
        continue

if password_found:
    input()
    sys.exit(0)
else:
    print("*"*50)
    print(Fore.RED+"Sorry I can't find correct Password in your password list :( ")