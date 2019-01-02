a = 3
b = 5

for x in range(100):
    if x % a == 0 and x % b == 0:
        print("fizzbuzz")
        
    elif x % a == 0:
         print("fizz")
    elif x % b == 0:
        print("buzz")

    else:
        print(x)
         