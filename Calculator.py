                                                            # mani - tayefeh 🌹
import pyfiglet
from colorama import Fore , Back
from tqdm import tqdm
from time import sleep

txt = pyfiglet.figlet_format('Calculator', font='slant')

print(f"{txt}")

print(Back.YELLOW,"                                                  ",Back.RESET)

print(Fore.GREEN,"\n\t\tEnter the number 1",Fore.RESET)

num1 = float(input("\n\t\t       "))

print(Back.BLUE,"                                                  ",Back.RESET)


print(Fore.CYAN,"\t       Enter your oparator",Fore.RESET)

print(Fore.RED,"\n    ⚠ you can type for example * or multiplied ⚠",Fore.RESET)

print(Fore.LIGHTRED_EX,"\t\t\t\t\t\t\t\t\tGuidance for operators : (* or Multiplied) (% or Modulus) \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t(/ or Division) (+ or Plus) (- or Minus) (^ or Exponen)",Fore.RESET)

oparator = str(input("\n\t\t       "))


if oparator == "+" or oparator == "plus" or oparator == "Plus" or oparator == "minus" or oparator == "Minus" or oparator == "-" or  oparator == "^" or oparator == "exponen" or oparator == "Exponen" or oparator == "/" or oparator == "division" or oparator == "Division" or oparator == "Div" or oparator == "div" or oparator == "%" or oparator == "Modules" or oparator == "modules" or oparator =="Mod" or oparator == "mod" or oparator == "*" or oparator == "multiplied" or oparator == "Multiplied":
    pass
else:
    print(Fore.RED,"\t⚠  W  a  r  n  n  i  n  g  ⚠",Fore.RESET)
    exit()


print(Back.CYAN,"                                                  ",Back.RESET)



print(Fore.MAGENTA,"\n\t\tEnter the number 2",Fore.RESET)

num2 = float(input("\n\t\t       "))

print(Back.MAGENTA,"                                                   ",Back.RESET)

print(Fore.GREEN,"\n\t\t   Processing...",Fore.RESET)
for char in tqdm(range(100) , colour="GREEN",ncols=80):
    sleep(0.01)

print("\n\t    👇Your math calculations👇\n")   


if oparator == "+" or oparator == "plus" or oparator == "Plus":
    m = num1 + num2

elif oparator == "-" or oparator == "minus" or oparator == "Minus":
    m = num1 - num2  

elif oparator == "/" or oparator == "division" or oparator == "Division" or oparator == "div" or oparator == "Div":
    m = num1 / num2 

elif oparator == "%" or oparator == "modules" or oparator == "Modules" or oparator == "mod" or oparator == "Mod":
    m = (num2 / 100) * num1 

elif oparator == "*" or oparator == "multiplied" or oparator == "multiplied":
    m = num1 * num2 

elif oparator == "^" or oparator == "exponen" or oparator == "Exponen":
    m = num1 ** num2       


print(f"\t      {m}")    



