#AdventofCode 2019 - Day 1
#Ruben Villao
import math

def calcFuel(mass):
        return math.floor(int(mass)/3)-2

Input = open ("input.txt","r")
TotalFuel=0
for mass in Input:
        Fuel = calcFuel(mass)
        while (Fuel > 0):
                TotalFuel += Fuel
                Fuel = calcFuel(Fuel)
print (TotalFuel)
