import time

# Калькулятор
 
def print_with_delay(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    
print_with_delay("""
█████████████████
█   Calculator  █
█               █
█████████████████
█  <1> Adding   █
█  <2> Sub      █
█  <3> Multiply █
█  <4> Divide   █
█  <5> Circle A █
█  <6> Circle D █
█  <7> number π █
█████████████████""")

select = input("Choose")

if select == "1":
    a = int(input("Input the first number: "))
    b = int(input('Input the second number: '))
    print(f'If you add up these numbers you will get', a + b)
    
elif select == "2":
    c = int(input("Input the first number: "))
    d = int(input("Input the second number: "))
    print(f'If you subtract these numbers you will get', c - d)
    
elif select == "3":
    e = int(input("Input the first number: "))
    f = int(input("Input the second number: "))
    print(f'If you multiply these numbers you will get', e * f)
    
elif select == "4":
    g = int(input("Input the first number: "))
    h = int(input("Input the second number: "))
    print(f'If you divide these numbers you will get', g / h)
    
elif select == "5":
    i = int(input("Input the diameter of a circle: "))
    print(f'The radius of the circle is', i / 2)
    
elif select == "6":
    j = int(input("Input the circumference of a circle: "))
    print(f'The diameter of tje circle is', j / 3.14159265359)

elif select == "7":
    pi = input("""INPUT number = get what number pi is
    INPUT times = multiply number pi 
    INPUT divide = divide number pi 
    INPUT add = add number pi 
    INPUT subtract = subtract number pi""")
    if pi == "number":
        print("3.14159265359")
        
    if pi == "times":
        k = int(input("Input the number you want to multiply pi by: "))
        print(f'Pi multiplied by your number is:', k * 3.14159265359)
            
    if pi == "divide":
        l = int(input("Input the number you want divide by pi: "))
        print(f'Your number divided by pi is:', l / 3.14159265359)
                
    if pi == "add":
        m = int(input("Input the number you want to add up with pi"))
        print(f'Your number add up with pi is:', m + 3.14159265359)
                    
    if pi == "subtract":
        n = int(input("Input the number you want to subtract pi from: "))
        print(f'Your number subtracted from pi is:', n - 3.14159265359)
