#AdventofCode  2019 - Day 2
#Ruben Villao

Input = open("input2.txt","r").read()

string = Input.split(",")
intList = []
for i in string:
    intList.append(int(i))
#Made a copy of original intList for Part 2
intListPart2 = intList.copy()

#part 1 solution
pos = 0;
while intList[pos] != 99:
    if intList[pos] == 1:
        intList[intList[pos+3]] = intList[intList[pos+2]] + intList[intList[pos+1]]
    else:
        intList[intList[pos+3]] = intList[intList[pos+2]] * intList[intList[pos+1]]
    pos += 4
print("Part 1 Solution:")
print(intList)


#Part 2 Solution
for noun in range(100):
    for verb in range(100):
        intListNew = intListPart2.copy()
        intListNew[1] = noun
        intListNew[2] = verb
        pos = 0;
        while intListNew[pos] != 99:
            if intListNew[pos] == 1:
                intListNew[intListNew[pos+3]] = intListNew[intListNew[pos+2]] + intListNew[intListNew[pos+1]]
            else:
                intListNew[intListNew[pos+3]] = intListNew[intListNew[pos+2]] * intListNew[intListNew[pos+1]]
            pos += 4
        if intListNew[0] == 19690720:
            break;
    if intListNew[0] == 19690720:
        break;
print("Part 2 Solution:")            
print (str(noun)+""+str(verb))
            
