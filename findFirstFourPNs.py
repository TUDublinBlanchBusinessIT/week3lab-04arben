#Arben_Ozcikrikci
#17/02/25
from perfectNumber import isperfectNumber

def four_perfect_numbers():
    count = 1
    num = 1
    while count < 4:
        if isperfectNumber(num):
            print(f"{num} is a perfect number")
            count += 1
        num += 1

four_perfect_numbers()






#Write a program here that finds the first four perfect numbers.
#Put your name and date at the top of the file.
#The pseudocode in the README.md file will help you write this program.



