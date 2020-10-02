from core.lexer import Lexer

import os
import argparse

parser = argparse.ArgumentParser(description="Lexer para a linguagem ANSI C. Leonam Teixeira de Vasconcelos.", add_help=False)

parser.add_argument('f', nargs='+', action='store', help='Lista de arquivos nos quais a análise léxica será realizada')
parser.add_argument('-h', '--help', action='help', help='Mostra essa mensagem e sai.')

args = parser.parse_args()

if args.f :
    for file in args.f :
        if not os.path.isfile ( file ) :
            print('Arquivo não encontrado: ', file)
        print('Tokenizando o arquivo: ', file, '...')
        content = open(file, 'r').read()
        lex = Lexer(content)
        tokens = lex.tokenizar()
        for token in tokens:
            print(token)        
else :
    print('Você precisa de fornecer os arquivos de entrada.')
