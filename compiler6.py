"""
Write a program to detect valid identifier or not.
"""

import re
keywords = ["auto", "break", "case", "char", "const", "continue", "default", "do", "double",
"else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register",
"return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]

pattern = re.compile(r'^[a-zA-Z_][A-Za-z0-9_]*$')
id = input("Enter an identifier: ")
flag = id in keywords

if id!=flag and pattern.match(id) and len(id) <= 31:
    print('Valid identifier')
else:
    print('Invalid identifier')