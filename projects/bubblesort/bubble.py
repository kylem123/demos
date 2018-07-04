import random

val = 0
l = []
while True:
    val = input("Enter a number ('r' for random, 's' for stop) > ")
    #print(val)
    if(val == 's'):
        break
    if(val == 'r'):
        lower = int(input("Lower bound > "))
        upper = int(input("Upper bound > "))
        val = random.randint(lower, upper)
    l = l + [int(val)]

old = []

for x in range(0, len(l) - 1):
    for i in range(0, len(l) - 1):
        if((i < len(l) - 1) and l[i] > l[i + 1]):
            n1 = l[i]
            n2 = l[i + 1]

            l[i] = n2
            l[i + 1] = n1
            print("Swapping ", n1, " and ", n2)
        #if(l != old):
        print("[Pass " + str(x + 1) + "] -> " + str(l))
        old = l
