from core.lexer import Lexer

import argparse

content = open('samples/teste_1.c', 'r').read()

print(content)
lex = Lexer(content)
tokens = lex.tokenizar()
for token in tokens:
    print(token)
