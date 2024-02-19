kipling = "rudyard.txt"

maam = "maam.txt"


with open(maam,"r") as whole_file:
   for line in whole_file:
        print(line,end="")
