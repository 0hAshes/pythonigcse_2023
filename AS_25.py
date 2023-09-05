list = [5,6,7]
string = []

def histogram():
     for i in list:
           for x in range (i):
               string.append("*")
           print(*string)

print(histogram())
