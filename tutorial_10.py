import random
mynumber = random.uniform(0.1, 9.9)

print(mynumber)


Choose_Name = ["mimi","nini","momo","nono"]
for i in range(1,5):
    chosen = random.choice(Choose_Name)
    print(chosen)
    a = input("do you want to keep this name? yes/no ")
    if a == "yes":
      print("hm")
    if a == "no":
      Choose_Name.remove(chosen)
