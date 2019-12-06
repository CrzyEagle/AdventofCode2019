#AdventofCode  2019 - Day 4
#Ruben Villao


def isvalid(value):
    lastlastdigit=0
    lastdigit=0
    double=0
    possibledouble=0
    for digit in str(value):
        if int(digit) == int(lastdigit):
            possibledouble = 1
        elif int(digit) < int(lastdigit):
            return 0
        lastlastdigit=lastdigit;
        lastdigit = digit;
    return (double or possibledouble)

valid=0
x = 231832

while x <= 767346:
    if isvalid(x):
        valid+=1
    x+=1

print(isvalid(113444))
print(isvalid(123444))

print(valid)
