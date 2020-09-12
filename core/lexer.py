from core.util.posicao      import Posicao
from core.util.token        import Token
from core.util.tokenTipos   import TokenTipo
from core.util.alfabeto     import digitos

class Lexer : 

    def __init__ ( self, codigo : str ) :
        self.codigo = codigo
        self.posicao = Posicao()
        self.caracter_atual = None
        self.avancar()

    def avancar ( self ) :
        self.posicao.avancar( quebrar_linha=( self.caracter_atual == '\n' ) )
        self.caracter_atual = self.codigo[self.posicao.pos] if self.posicao.pos < len(self.codigo) else None

    def tokenizar ( self ) :
        tokens = []
        while self.caracter_atual != None :
            if self.caracter_atual in ' \t':
                self.avancar()
            elif self.caracter_atual in digitos + '.':
                numero_final = ''
                contador_de_pontos = 0
                while self.caracter_atual != None and self.caracter_atual in digitos + '.' :
                    if self.caracter_atual == '.' :
                        if contador_de_pontos == 1:
                            break
                        contador_de_pontos += 1
                    numero_final += self.caracter_atual
                    self.avancar()
                if contador_de_pontos == 0 :
                    tokens.append(Token(TokenTipo.TOKEN_INT, int(numero_final)))
                else :
                    tokens.append(Token(TokenTipo.TOKEN_REAL, float(numero_final)))
            elif self.caracter_atual == '/' :
                self.avancar()
                if self.caracter_atual == '=' :
                    tokens.append(Token(TokenTipo.TOKEN_DIV_IG))
                    self.avancar()
                else:
                    tokens.append(Token(TokenTipo.TOKEN_DIV))
            elif self.caracter_atual == '*' :
                self.avancar()
                if self.caracter_atual == '=' :
                    tokens.append(Token(TokenTipo.TOKEN_MULT_IG))
                    self.avancar()
                else:
                    tokens.append(Token(TokenTipo.TOKEN_MULT))
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
        tokens.append(Token(TokenTipo.TOKEN_EOF))
        return tokens
