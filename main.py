import random
def scramble(n):
     if(n == 32):
          return 166 + random.randint(1, 10)
     if(167 <= n <= 175):
          return 32
     else:
          return 156 - n
message = input()
values = []
for i in range(len(message)):
     values.append(ord(message[i]))
for j in range(len(values)):
     print(chr(scramble(values[j])), end="")