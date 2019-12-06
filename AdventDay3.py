#AdventofCode  2019 - Day 3
#Ruben Villao

Input = open("input3.txt","r")
list1 = {(1,2),(2,3)}
print(list1)

for wire in Input:
    wire = wire.split(",")
    x=0
    y=0
    for move in wire:
        if move[0] == "L":
            print(move[1:])
        elif move[0] == "R":
            print(move[1:])
        elif move[0] == "U":
            print(move[1:])
        else:
            print(move[1:])
    #print(wire)

    
