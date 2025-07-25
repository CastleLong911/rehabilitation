'''
# Brute Force way
x = float(input())
sol = []
def gab(n):
    n_str = str(n)[1:] + str(n)[0] 
    return float(n_str)

def terminator(n):
    target = []
    for i in range(1, 9):
        if len(str(n) * i) < 6:
            target.append(int(str(n) * i))
        else:
            break
    for i in target:
        sol.remove(i)

for i in range(1, 100_000_000):
    if i * x == gab(i):
         sol.append(i)

if len(sol) == 0:
    print("No solution")
else:
    for i in sol:
        print(i)
'''

# Mathematical way (By ChatGPT model o3)

from fractions import Fraction #부동소수점문제 해결 위해 사용

def find_rotating_numbers(x, upper=100_000_000):
    '''

    자연수 n = a * 10^자릿수-1 + b(맨앞자리를 제외한 뒷자리수)
    앞자리를 뒤로 보낸 자연수 rotating(n) = b * 10 + a
    즉,
    (a * 10^자릿수-1 + b) * x = b * 10 + a
    b * x - b * 10 = a - a*x*10^자릿수-1
    b(x - 10) = a(1 - x*10^자릿수-1)
    
            1 - x*10^자릿수-1  
    b = a ----------------------
              x - 10

    즉, x가 2.6 이고 자릿수가 3, a가 1일때, 


            1 - 2.6*10^3-1  
    b = 1 ----------------------
              2.6 - 10

                -259  
    = 1 ----------------------
                -7.4
              
    =35

    즉 b = 35 이고 a = 1 이므로 n = 135, rotating(n) = 351이 됨

    '''
    x = Fraction(str(x))
    den = x - 10
    if den == 0:
        return []

    res = []
    max_digits = len(str(upper))

    for d in range(1, max_digits + 1):       
        pow10 = 10 ** (d - 1)                
        num_factor = 1 - x * pow10           

        for a in range(1, 10):               
            b = a * num_factor / den         
            if b.denominator != 1:           
                continue
            b = b.numerator                 

            if 0 <= b < pow10:              
                n = a * pow10 + b
                if n <= upper:               
                    
                    s = str(n)
                    rotated = int(s[1:] + s[0])
                    if n * x == rotated:
                        res.append(n)

    return sorted(res)

x = float(input())
sol = find_rotating_numbers(x)

if len(sol) == 0:
    print("No solution")
else:
    for i in sol:
        print(i)
