# ali
from datetime import datetime
from zipfile import ZipFile
import termcolor2
from colorama import Fore
import os
import time

os.system('clear')
time.sleep(2)
# ===========================================
print(""" 


 ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗     ███████╗██╗██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ╚══███╔╝██║██╔══██╗
██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝      ███╔╝ ██║██████╔╝
██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗     ███╔╝  ██║██╔═══╝ 
╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║    ███████╗██║██║     
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝╚═╝     
                                                                               

                                                                                                              

 """)
os.system('clear')
print(Fore.BLUE)
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
print(Fore.CYAN)
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
# ===========================================
print(termcolor2.colored(" Coded By Ali and Mmd",color="red"))

print(termcolor2.colored("      efcoriti channel in the tel >> @efcoriti_programmer",color="green"))

print(termcolor2.colored("		rubika & telegram_id_ali >> @efcoriti",color="cyan"))

print(termcolor2.colored("			rubika id_mmd >> @exploite",color="white"))

# ===========================================
print("\n\n\n\n\n\n\n\n\n\n\n\n")
f = input(termcolor2.colored('ENTER YOUR ZIP FILE  => ',color="yellow"))
p = input(termcolor2.colored('ENTER THE PASSWORD LIST  => ',color="yellow"))

# ===========================================
f = ZipFile(f)
L = 0
start = datetime.now()
for password in open(p):
    password = password.strip("\n")
    print("Testing : {}".format(password))
    tests += 1
    try:
        f.extractall(pwd=password.encode())
        end = datetime.now()
        B = end - start
        print("-"*50)
        print(Fore.GREEN+"Password : {}", termcolor2.colored('‹---›     {} Passwords Tested in {} seconds !!!!',color="cyan").format(password,L,B.total_seconds()))
        input()
        break
    except :
        continue
