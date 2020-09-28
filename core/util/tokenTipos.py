from enum import Enum

keywords = [
    'auto',  
    'break',
    'double',
    'case',
    'char',
    'const',
    'continue',
    'default',
    'do',
    'else',
    'enum',
    'extern',
    'float',
    'for',
    'goto',
    'if',
    'int',
    'long',
    'register',
    'return',
    'short',
    'signed',
    'sizeof',
    'static',
    'struct',
    'switch',
    'typedef',
    'union',
    'unsigned',
    'void',
    'volatile',
    'while'
]

class TokenTipo ( Enum ) :

    # Delimitadores
    TOKEN_PARE       = 'TOKEN_PARE'         # Parênteses esquerdo           '('
    TOKEN_PARD       = 'TOKEN_PARD'         # Parênteses direito            ')'
    TOKEN_CHAVEE     = 'TOKEN_CHAVEE'       # Chave esquerda                '{'
    TOKEN_CHAVED     = 'TOKEN_CHAVED'       # Chave direita                 '}'
    TOKEN_COLCHETEE  = 'TOKEN_COLCHETEE'    # Colchete esquerdo             '['
    TOKEN_COLCHETED  = 'TOKEN_COLCHETED'    # Colchete direito              ']'


    # Números
    TOKEN_HEXA       = 'TOKEN_HEXA'         # Número hexadecimal            '0x[0-9a-fA-F]+'
    TOKEN_OCT        = 'TOKEN_OCT'          # Número octal                  '0[0-7]+'
    TOKEN_BIN        = 'TOKEN_BIN'          # Número binário                '0b[0-1]+'
    TOKEN_INT        = 'TOKEN_INT'          # Número inteiro                '[0-9]+'
    TOKEN_REAL       = 'TOKEN_REAL'         # Número real                   '[0-9]+\.[0-9]+'
    
    TOKEN_CHAR       = 'TOKEN_CHAR'
    TOKEN_STR        = 'TOKEN_STR'

    TOKEN_INCLUDE    = 'TOKEN_INCLUDE'
    TOKEN_DEFINE     = 'TOKEN_DEFINE'
    TOKEN_PRAGMA     = 'TOKEN_PRAGMA'

    # Operadores
    TOKEN_SOMA       = 'TOKEN_SOMA'         # Operador soma                         '+'
    TOKEN_SOMA_IG    = 'TOKEN_SOMA_IG'      # Operador soma e atribui               '+='
    TOKEN_SOMA_UM    = 'TOKEN_SOMA_UM'      # Operador incrementar um               '++'
    TOKEN_SUB        = 'TOKEN_SUB'          # Operador subtração                    '-'
    TOKEN_SUB_IG     = 'TOKEN_SUB_IG'       # Operador subtrai e atribui            '-='
    TOKEN_SUB_UM     = 'TOKEN_SUB_UM'       # Operador decrementar um               '--'
    TOKEN_ASTERISCO  = 'TOKEN_ASTERISCO'    # Operador multiplicação ou ponteiro    '*'
    TOKEN_DIV        = 'TOKEN_DIV'          # Operador divisão                      '/'
    TOKEN_MULT_IG    = 'TOKEN_MULT_IG'      # Operador multiplica e atribui         '*='
    TOKEN_DIV_IG     = 'TOKEN_DIV_IG'       # Operador divide e atribui             '/='
    TOKEN_MOD        = 'TOKEN_MOD'          # Operador módulo                       '%'
    TOKEN_MOD_IG     = 'TOKEN_MOD_IG'       # Operador módulo e atribui             '%='
    TOKEN_NOT        = 'TOKEN_NOT'          # Operador negação                      '!'
    TOKEN_TERN       = 'TOKEN_TERN'         # Operador ternário                     '?'
    TOKEN_MENOR      = 'TOKEN_MENOR'        # Operador menor                        '<'
    TOKEN_MAIOR      = 'TOKEN_MAIOR'        # Operador maior                        '>'
    TOKEN_MENOR_IG   = 'TOKEN_MENOR_IG'     # Operador menor igual                  '<='
    TOKEN_MAIOR_IG   = 'TOKEN_MAIOR_IG'     # Operador maior igual                  '>='
    TOKEN_SHIFT_L    = 'TOKEN_SHIFT_L'      # Operador Shift para esquerda          '<<'
    TOKEN_SHIFT_R    = 'TOKEN_SHIFT_R'      # Operador Shift para direita           '>>'
    TOKEN_XOR        = 'TOKEN_XOR'          # Operador Or exclusivo                 '^'
    TOKEN_OR         = 'TOKEN_OR'           # Operador Or                           '||' 
    TOKEN_ORB        = 'TOKEN_ORB'          # Operador Or bit a bit                 '|'
    TOKEN_AND        = 'TOKEN_AND'          # Operador And                          '&&'
    TOKEN_ANDB       = 'TOKEN_ANDB'         # Operador And bit a bit                '&'
    TOKEN_NOTB       = 'TOKEN_NOTB'         # Operador Not bit a bit                '~'
    TOKEN_BITF       = 'TOKEN_BITF'         # Operador bit field                    ':'
    TOKEN_IGUAL      = 'TOKEN_IGUAL'        # Operador igual                        '=='
    TOKEN_ATRIB      = 'TOKEN_ATRIB'        # Operador atribuição                   '='
    
    TOKEN_VIRG       = 'TOKEN_VIRG'         # Virgula
    TOKEN_PTV        = 'TOKEN_PTV'          # Ponto e vírgula
    TOKEN_EOF        = 'TOKEN_EOF'          # Fim de arquivo

    TOKEN_IDENT      = 'TOKEN_IDENT'        # Identificador
    TOKEN_KEYWORD    = 'TOKEN_KEYWORD'      # Keyword

# # KEYWORDS DO C
# KEYWORD_AUTO     = 'AUTO'             
# KEYWORD_BREAK    = 'BREAK'           
# KEYWORD_DOUBLE   = 'DOUBLE'            
# KEYWORD_CASE     = 'CASE'           
# KEYWORD_CHAR     = 'CHAR'           
# KEYWORD_CONST    = 'CONST'           
# KEYWORD_CONTINUE = 'CONTINUE'           
# KEYWORD_DEFAULT  = 'DEFAULT'           
# KEYWORD_DO       = 'DO'           
# KEYWORD_ELSE     = 'ELSE'           
# KEYWORD_ENUM     = 'ENUM'           
# KEYWORD_EXTERN   = 'EXTERN'           
# KEYWORD_FLOAT    = 'FLOAT'           
# KEYWORD_FOR      = 'FOR'           
# KEYWORD_GOTO     = 'GOTO'           
# KEYWORD_IF       = 'IF'           
# KEYWORD_INT      = 'INT'           
# KEYWORD_LONG     = 'LONG'           
# KEYWORD_REGISTER = 'REGISTER'           
# KEYWORD_RETURN   = 'RETURN'           
# KEYWORD_SHORT    = 'SHORT'           
# KEYWORD_SIGNED   = 'SIGNED'           
# KEYWORD_SIZEOF   = 'SIZEOF'           
# KEYWORD_STATIC   = 'STATIC'           
# KEYWORD_STRUCT   = 'STRUCT'       
# KEYWORD_SWITCH   = 'SWITCH'       
# KEYWORD_TYPEDEF  = 'TYPEDEF'       
# KEYWORD_UNION    = 'UNION'       
# KEYWORD_UNSIGNED = 'UNSIGNED'           
# KEYWORD_VOID     = 'VOID'       
# KEYWORD_VOLATILE = 'VOLATILE'           
# KEYWORD_WHILE    = 'WHILE'  