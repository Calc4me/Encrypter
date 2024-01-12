from random import randint as r
#Encrypt function
def scramble(n):
     #Space
     if(n == 32):
          #It's harder to tell what are spaces if it's slightly random.
          return 166 + r(1, 10)
     #Unscramble space
     if(167 <= n <= 175):
          #Space
          return 32
     #Not space
     else:
          return 156 - n
#Paste message in preset
preset = ""
values = []
#Input
usepreset = input("Use preset? (y/n) ")
if usepreset == "y":
  message = preset
elif usepreset == "n":
  message = input("Message: ")
#Put into values
for i in range(len(message)):
     values.append(ord(message[i]))
#Scramble and print
for j in range(len(values)):
     print(chr(scramble(values[j])), end="")