word= input()
n=1

def upperN(string):
      return "".join(map(lambda c: chr(ord(c) -32) if 97 <= ord(c) <= 122 else c, string))

for n in range(len(word)):
    if n%2 != 0:
        print(upperN(word[n]), end='')
