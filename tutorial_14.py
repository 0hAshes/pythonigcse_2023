spriteIntro = "Heya! My name is Elise"

print(spriteIntro[0:3])

print(spriteIntro[3::])
#Prints from character 3 to the end. Advantage of this is that you don't need to know the length of the string. Notice the ::

print(spriteIntro[0:6:2])

#The third part of the command is the step. This example prints every alternate character. It's ace isn't it?

print(spriteIntro[-1:-7:-1])
#We can start at the right side of the string and work backwards. -1 is the last character of the string.

print(spriteIntro[0:-2])
