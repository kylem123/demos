chars = []
array = []
print("Enter at least 10 integers and then type 'stop' to stop")
while True:
    x = input("Number > ")
    if(x.isdigit()):
        array = array + [int(x)]
    elif(x == "stop"):
        if(len(array) >= 10):
            break
        else:
            print("Need at least 10 integers (Currently there are " + str(len(array)) + ")")
    elif(x.isalpha() and len(x) == 1):
        chars = chars + [x]
    else:
        print("Invalid Input!")

new = list(array)
new.sort()
even = []

for i in range(0, len(array)):
    if(array[i] % 2 == 0):
        even = even + [array[i]]
        new.remove(array[i])

print(str(chars + array))
chars.sort()
chars2 = []
for i in range(len(chars) - 1, 0, -1):
    chars2 = chars2 + [chars[i]]
    
new = chars2 + new + even
print(new)
