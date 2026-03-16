#FizzBuzz

for numero in range(1, 51):
    
    if numero % 3 == 0:
        print("Fizz")
        
    elif numero % 5 == 0:
        print("Buzz")
        
    elif numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
        
    else:
        print(numero)
