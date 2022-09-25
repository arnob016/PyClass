def upperN(string):
      return "".join(map(lambda c: chr(ord(c) -32) if 97 <= ord(c) <= 122 else c, string))
