myNums = [4,8,12,16,20,24,28,32,36,40,44,48,52,56,60]
print(*myNums,"\n",(sum(myNums)))

print("\nHere are a bunch of cool statistics for this list!")
print(*myNums, "\nThe sum of this list: ", (sum(myNums)), "\nThe minimum number of this list: ", (min(myNums)), "\nThe maximum number in this list: ", (max(myNums)), "\nThe length of this list: ", (len(myNums)), "\nThe mean average of this list: ", (sum(myNums)/(len(myNums))))
