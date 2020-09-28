from core.util.posicao      import Posicao
from core.util.token        import Token
from core.util.tokenTipos   import TokenTipo, keywords
from core.util.alfabeto     import *

from copy import copy
class Lexer : 

    def __init__ ( self, codigo : str ) :
        self.codigo = codigo
        self.posicao = Posicao()
        self.caracter_atual = None
        self.avancar()

    def lookahead ( self ) :
        auxPos = copy(self.posicao)
        self.posicao.avancar(quebrar_linha=( self.caracter_atual == '\n' ))
        index = self.posicao.pos
        self.posicao = auxPos
        return self.codigo [ index ] if index < len(self.codigo) else None

    def avancar ( self, qtd=1 ) :
        for i in range ( qtd ) :
            self.posicao.avancar( quebrar_linha=( self.caracter_atual == '\n' ) )
            self.caracter_atual = self.codigo[self.posicao.pos] if self.posicao.pos < len(self.codigo) else None

    def tokenizar ( self ) :
        tokens = []
        while self.caracter_atual != None :
            if self.caracter_atual in ' \t\n':
                self.avancar()
            elif self.caracter_atual == '#' :
                token = self.make_preprocessor ()
                tokens.append(token)
                self.avancar()
            elif self.caracter_atual in digitos + '.':
                token = self.make_numbers()
                tokens.append(token)
            elif self.caracter_atual in alfabeto :
                token = self.parse_word ()
                tokens.append(token)
            elif self.caracter_atual == '"':
                self.avancar()
                token = self.parse_string()
                tokens.append(token)
            elif self.caracter_atual == "'":
                self.avancar()
                token = self.parse_char()
                tokens.append(token)
            elif self.caracter_atual == '/' :
                self.avancar()
                if self.caracter_atual == '=' :
                    tokens.append(Token(TokenTipo.TOKEN_DIV_IG))
                    self.avancar()
                if self.caracter_atual == '/' :
                    while self.caracter_atual not in ( None, '\n' ) :
                        self.avancar()
                else:
                    tokens.append(Token(TokenTipo.TOKEN_DIV))
            elif self.caracter_atual == '*' :
                self.avancar()
                if self.caracter_atual == '=' :
                    tokens.append(Token(TokenTipo.TOKEN_MULT_IG))
                    self.avancar()
                else:
                    tokens.append(Token(TokenTipo.TOKEN_ASTERISCO))
            elif self.caracter_atual == '-' :
                self.avancar()
                if self.caracter_atual == '-' :
                    tokens.append(Token(TokenTipo.TOKEN_SUB_UM))
                    self.avancar()
                elif self.caracter_atual == '=' :
                    tokens.append(Token(TokenTipo.TOKEN_SUB_IG))
                    self.avancar()
                else :
                    tokens.append(Token(TokenTipo.TOKEN_SUB))
            elif self.caracter_atual == '+' :
                self.avancar()
                if self.caracter_atual == '+' :
                    tokens.append(Token(TokenTipo.TOKEN_SOMA_UM))
                    self.avancar()
                elif self.caracter_atual == '=' :
                    tokens.append(Token(TokenTipo.TOKEN_SOMA_IG))
                    self.avancar()
                else :
                    tokens.append(Token(TokenTipo.TOKEN_SOMA))
            elif self.caracter_atual == '(' :
                tokens.append(Token(TokenTipo.TOKEN_PARE))
                self.avancar()
            elif self.caracter_atual == ')' :
                tokens.append(Token(TokenTipo.TOKEN_PARD))
                self.avancar()
            elif self.caracter_atual == '{' :
                tokens.append(Token(TokenTipo.TOKEN_CHAVEE))
                self.avancar()
            elif self.caracter_atual == '}' :
                tokens.append(Token(TokenTipo.TOKEN_CHAVED))
                self.avancar()
            elif self.caracter_atual == '[' :
                tokens.append(Token(TokenTipo.TOKEN_COLCHETEE))
                self.avancar()
            elif self.caracter_atual == ']' :
                tokens.append(Token(TokenTipo.TOKEN_COLCHETED))
                self.avancar()
            elif self.caracter_atual == '%' :
                self.avancar()
                if self.caracter_atual == '=' :
                    tokens.append(Token(TokenTipo.TOKEN_MOD_IG))
                    self.avancar()
                else :
                    tokens.append(Token(TokenTipo.TOKEN_MOD))
            elif self.caracter_atual == '!' :
                tokens.append(Token(TokenTipo.TOKEN_NOT))
                self.avancar()
            elif self.caracter_atual == '~' :
                tokens.append(Token(TokenTipo.TOKEN_NOTB))
                self.avancar()
            elif self.caracter_atual == '^' :
                tokens.append(Token(TokenTipo.TOKEN_XOR))
                self.avancar()
            elif self.caracter_atual == '<' :
                self.avancar()
                if self.caracter_atual == '<' :
                    tokens.append(Token(TokenTipo.TOKEN_SHIFT_L))
                    self.avancar()
                elif self.caracter_atual == '=' :
                    tokens.append(Token(TokenTipo.TOKEN_MENOR_IG))
                    self.avancar()
                else :
                    tokens.append(Token(TokenTipo.TOKEN_MENOR))
            elif self.caracter_atual == '>' :
                self.avancar()
                if self.caracter_atual == '>' :
                    tokens.append(Token(TokenTipo.TOKEN_SHIFT_R))
                    self.avancar()
                elif self.caracter_atual == '=' :
                    tokens.append(Token(TokenTipo.TOKEN_MAIOR_IG))
                    self.avancar()
                else :
                    tokens.append(Token(TokenTipo.TOKEN_MAIOR))
            elif self.caracter_atual == '|' :
                self.avancar()
                if self.caracter_atual == '|' :
                    tokens.append(Token(TokenTipo.TOKEN_OR))
                    self.avancar()
                else :
                    tokens.append(Token(TokenTipo.TOKEN_ORB))
            elif self.caracter_atual == '&' :
                self.avancar()
                if self.caracter_atual == '&' :
                    tokens.append(Token(TokenTipo.TOKEN_AND))
                    self.avancar()
                else :
                    tokens.append(Token(TokenTipo.TOKEN_ANDB))
            elif self.caracter_atual == ':' :
                tokens.append(Token(TokenTipo.TOKEN_BITF))
                self.avancar()
            elif self.caracter_atual == ';' :
                tokens.append(Token(TokenTipo.TOKEN_PTV))
                self.avancar()
            elif self.caracter_atual == ',' :
                tokens.append(Token(TokenTipo.TOKEN_VIRG))
                self.avancar()
            elif self.caracter_atual == '=' :
                self.avancar()
                if self.caracter_atual == '=' :
                    tokens.append(Token(TokenTipo.TOKEN_IGUAL))
                    self.avancar()
                else:
                    tokens.append(Token(TokenTipo.TOKEN_ATRIB))
            else :
                message = 'Erro durante parsing: "' +  self.caracter_atual + '" posição: ' + str(self.posicao)
                raise Exception(message)            
        tokens.append(Token(TokenTipo.TOKEN_EOF))
        return tokens

    def make_numbers ( self ) :
        numero_final = ''
        contador_de_pontos = 0
        tokenTipo = None
        caracteres_aceitos = []
        if self.caracter_atual == '0' :
            charahead = self.lookahead()
            if charahead in ('b', 'B') :
                self.avancar(2)
                caracteres_aceitos = digitos_bin
                tokenTipo = TokenTipo.TOKEN_BIN
            elif charahead in ('x', 'X') :
                self.avancar(2)
                caracteres_aceitos = digitos_hexa
                tokenTipo = TokenTipo.TOKEN_HEXA
            elif charahead in digitos_oct:
                self.avancar()
                caracteres_aceitos = digitos_oct
                tokenTipo = TokenTipo.TOKEN_OCT
        if caracteres_aceitos == [] :
            while self.caracter_atual != None and self.caracter_atual in digitos + '.' :
                if self.caracter_atual == '.' :
                    if contador_de_pontos == 1:
                        break
                    contador_de_pontos += 1
                numero_final += self.caracter_atual
                self.avancar()
        else :
            while self.caracter_atual != None and self.caracter_atual in caracteres_aceitos :
                numero_final += self.caracter_atual
                self.avancar()
            return Token(tokenTipo, numero_final)
        if contador_de_pontos == 0 :
            return Token(TokenTipo.TOKEN_INT, int(numero_final))
        else :
            return Token(TokenTipo.TOKEN_REAL, float(numero_final))

    def make_preprocessor ( self ) :
        token_str = ''
        token_tipo = None
        while self.caracter_atual not in ( None, ' ' ) :
            token_str += self.caracter_atual
            self.avancar()
        if token_str == '#define' :
            token_tipo = TokenTipo.TOKEN_DEFINE
        elif token_str == '#include' :
            token_tipo = TokenTipo.TOKEN_INCLUDE
        elif token_str == '#pragma' :
            token_tipo = TokenTipo.TOKEN_PRAGMA
        token_data = ''
        while self.caracter_atual not in ( None, '\n' ) :
            token_data += self.caracter_atual
            self.avancar()
        return Token(token_tipo, token_data)

    def parse_word ( self ) :
        token_str = ''
        while self.caracter_atual != None and self.caracter_atual in alfanumu :
            token_str += self.caracter_atual
            self.avancar()
        if token_str in keywords :
            return Token(TokenTipo.TOKEN_KEYWORD, valor=token_str)
        else :
            return Token(TokenTipo.TOKEN_IDENT, valor=token_str)

    def parse_string ( self ) :
        token_str = ''
        while self.caracter_atual not in ( None, '"' ) :
            token_str += self.caracter_atual
            self.avancar()
        if self.caracter_atual == '"' :
            self.avancar()
        return Token(TokenTipo.TOKEN_STR, valor=token_str)

    def parse_char ( self ) :
        token_str = ''
        while self.caracter_atual not in ( None, "'" ) :
            token_str += self.caracter_atual
            self.avancar()
        if self.caracter_atual == "'" :
            self.avancar()
        return Token(TokenTipo.TOKEN_CHAR, valor=token_str)