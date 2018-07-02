def word():
    l = []
    word = input("Word > ")
    #file = open("titin.txt")
    #word = file.read()
    word = word.lower()
    #word = "llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
    for c in word:
        l = l + [(ord(c) - 96)]
    x = insertion_sort(l, True)
    a = ""
    for n in x:
        a = a + chr(n + 96)
    print(word + " -> " + a)

def loop():
    l = []
    print("Input each number individually ('s' to stop)")
    while True:
        val = input("Number > ")
        if val == 's':
            break
        l = l + [int(val)]
    x = insertion_sort(l, False)
    print("Insertion Sorted List: " + str(x))

def insertion_sort(l, letters):
    o = []
    for num in l:
        o = o + [num]
    x = []
    count = 0
    for num in l:
        for i in range(0, len(x)):
            #print(i)
            #print(num)
            if(num < x[i]):
                x.insert(i, num)
                o.remove(num)
                break
            elif(num == x[i]):
                x.insert(i + 1, num)
                o.remove(num)
                break
            elif(i == len(x) - 1):
                x.insert(i + 1, num)
                o.remove(num)
        if(len(x) == 0):
            x = x + [num]
            o.remove(num)
        
        x2 = []
        o2 = []
        if(letters == True):
            for num in x:
                x2 = x2 + [chr(num + 96)]
            for num in o:
                o2 = o2 + [chr(num + 96)]
        else:
            x2 = x
            o2 = o
        
        print("Sorted: " + str(x2) + ", Unsorted: " + str(o2))
        #print(str((100/len(x)) * count) + "%")
        count = count + 1
    return x

def main():
    while True:
        c = input("Type 'w' to sort a word or 'n' to sort numbers > ")
        if(c == 'w'):
            word()
        elif(c == 'n'):
            loop()
    
main()