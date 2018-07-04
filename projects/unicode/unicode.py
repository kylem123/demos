import time

#print("\u23F0")

line = ""

input()

#Number of unicode characters = 1112064
#Only 65536 are printable (Others are non BMP). Stop at 65535
total = 65536
for i in range(0, total - 1):
    if(len(line) < 50):
        line = line + (" " + chr(i))
    else:
        percentage = str((100 / total) * i)
        spacing = int(18 - len(percentage[2:])) * " "  
        print("|| " + percentage + spacing + "%" + " ||" + line)
        line = ""
        time.sleep(0.001)
        
