from core.lexer import Lexer

import sys

sys.path.append('../')

try :
    while True :
        comando = input('> ')
        print(comando)
        lexer = Lexer(comando)
        tokens = lexer.tokenizar()
        for token in tokens:
            print(token)
except KeyboardInterrupt :
    print('\b\bBye')
except EOFError:
    print('Bye')