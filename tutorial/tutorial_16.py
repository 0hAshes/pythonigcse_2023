# excersise 1

numcol1 = [1,1003442,5.32222342]
numcol2 = [5.62233,7.364363,9.32747474342]
numcol3 = [9.2634526,7.866832817,10.781237892798]

print("\nLeft Justify")
for i in range(3):
    print(f"{numcol1[i]:<15} {numcol2[i]:<15} {numcol3[i]:<15}")

print("\nRight justify with fixed decimal points")
for i in range(3):
    print(f"{numcol1[i]:>15.2f} {numcol2[i]:>15.2f} {numcol3[i]:>15.2f}")
# Note the order here. >15 and then .2f which is 2 decimal places

print("\nCentred with fixed decimal points")
for i in range(3):
    print(f"{numcol1[i]:^15.2f} {numcol2[i]:^15.2f} {numcol3[i]:^15.2f}")


# excersise 2 - make my own table
    numcol1 = [3,5,6]
numcol2 = [2,4,6,8,10]
numcol3 = [2.3,5,7,9]

print("\nRandom")
for i in range(3):
    print(f"{numcol1[i]:<15} {numcol2[i]:<15} {numcol3[i]:<15}")

print("\nEven Numbers")
for i in range(3):
    print(f"{numcol1[i]:>15.2f} {numcol2[i]:>15.2f} {numcol3[i]:>15.2f}")
# Note the order here. >15 and then .2f which is 2 decimal places

print("\nPrime Numbers")
for i in range(3):
    print(f"{numcol1[i]:^15.2f} {numcol2[i]:^15.2f} {numcol3[i]:^15.2f}")

    
# exercise 3 - make binary convertor 
    

def binaryConvertor():
    denary = int(input("Give us a denary number: "))
    binary = print(f"Binary: {denary:b}")

    
(binaryConvertor())
