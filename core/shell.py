from core.lexer import Lexer

while True :
    comando = input('> ')
    print(comando)
    lexer = Lexer(comando)
    tokens = lexer.tokenizar()
    for token in tokens:
        print(token)