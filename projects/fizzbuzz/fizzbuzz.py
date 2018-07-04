def isPrime(num):
    for i in range(1, num + 1):
        if(num / i - int(num / i) == 0):
            factor = num / i
            if(factor != 1 and factor != num):
                return False
    if(num == 1):
        return False
    else:
        return True

number = input("Number > ")
fizz = int(input("What multiple would you like to be replaced with Fizz? > "))
buzz = int(input("What multiple would you like to be replaced with Buzz? > "))
for i in range(1, int(number) + 1):
    #if(isPrime(i) == True):
    #    print("OOPS!")
    if(i % fizz == 0 and i % buzz == 0):
        print("FizzBuzz")
    elif(i % fizz == 0):
        print("Fizz")
    elif(i % buzz == 0):
        print("Buzz")
    else:
        print(i)

        
