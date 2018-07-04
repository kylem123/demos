import re

binary = [1, 2, 4, 8, 16, 32, 64, 128]
binary_format = "[0-1][0-1][0-1][0-1][0-1][0-1][0-1][0-1]"

def binary_to_denary(inpt):
    total = 0

    for i in range(8, 0, -1):
        digit = inpt[i - 1]
        digit = int(digit)

        if(digit == 1):
            total += binary[8 - i]
            
    print(total)

def denary_to_binary(inpt):
    number = int(inpt)
    result = ""
    for i in range(8, 0, -1):
        if(number >= binary[i - 1]):
            number -= binary[i - 1]
            result = result + "1"
        else:
            result = result + "0"
            
    print(result)
    
def main():
    while(True):
        mode = ""
        while(mode.isdigit() == False):
            mode = input("Would you like to [1] Convert from binary to denary [2] Convert from denary to binary? > ")
        if(int(mode) == 1):
##            inpt = ""
##            while(inpt == ""):
##                unchecked = input("> ")
##                if(re.search(binary_format, unchecked) == True):
##                    inpt = unchecked
##                else:
##                    print("Invalid binary format!")
            binary_to_denary(input("> "))
        elif(int(mode) == 2):
            denary_to_binary(int(input("> ")))
        
main()
