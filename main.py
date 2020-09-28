from core.lexer import Lexer

# c_file = open('samples/teste_1.c', 'r').read()
c_file = 'int a = 0000.12345671;'
print(c_file)
lex = Lexer(c_file)
tokens = lex.tokenizar()
for token in tokens:
    print(token)