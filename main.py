from core.lexer import Lexer

c_file = open('samples/teste_2.c', 'r').read()
# c_file = ''
# print(c_file)
lex = Lexer(c_file)
tokens = lex.tokenizar()
for token in tokens:
    print(token)