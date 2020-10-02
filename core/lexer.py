from copy                            import copy
from collections                     import deque
from core.util.token                 import Token
from core.util.posicao               import Posicao
from core.util.alfabeto              import alfabeto, digitos, digitos_bin, digitos_hexa, digitos_oct, alfanumu, alfabeto_completo
from core.util.tokenTipos            import TokenTipo, keywords, operadores_duplos, operadores_unicos, separadores
from core.util.apontador_de_caracter import apontador_de_caracter

import sys
import re

class Lexer : 
    """
    Classe que implementa o Lexer da linguagem C ANSI.
    O método tokenizar() faz a análise léxica, retornando
    uma lista com os tokens capturados.
    """

    def __init__ ( self, codigo : str ) :
        """
        Construtor da classe Lexer, que recebe um código
        em C como string.
        """
        self.codigo = codigo
        self.linha_atual = ''
        self.contexto = self.linha_atual
        
        sys.tracebacklimit = 0

        if len(codigo) > 0 :
            self.posicao = Posicao()
            self.caracter_atual = None
            self.remover_comentarios()
            self.avancar()
        else:
            raise Exception("Código não pode ser vazio!")

    def lookahead ( self ) :
        """
        Retorna o próximo caracter no código.
        """
        auxPos = copy(self.posicao)
        self.posicao.avancar(quebrar_linha=( self.caracter_atual == '\n' ))
        index = self.posicao.pos
        self.posicao = auxPos
        return self.codigo [ index ] if index < len(self.codigo) else None


    def avancar_ate ( self, chars ) :
        """
        Avança até o caracter passado por parâmetro.
        """
        if chars != None :
            self.avancar() # Avança um pra não contar o atual
            while self.caracter_atual not in chars :
                self.avancar()


    def avancar ( self, qtd=1 ) :
        """
        Avança no código quantas vezes forem passadas. Por
        padrão avança em um caracter.
        """
        for _ in range ( qtd ) :
            if self.caracter_atual in [ '\n', None ] :
                self.linha_atual = ''
            else :
                self.linha_atual += self.caracter_atual
            self.contexto = apontador_de_caracter(self.posicao, self.linha_atual)
            self.posicao.avancar( quebrar_linha=( self.caracter_atual == '\n' ) )
            self.caracter_atual = self.codigo[self.posicao.pos] if self.posicao.pos < len(self.codigo) else None


    def capturar_linha ( self ) :
        """
        Captura a linha atual do código.
        """
        self.avancar()
        while self.caracter_atual != None and  self.caracter_atual != '\n' :
            self.linha_atual += self.caracter_atual
            self.avancar()
        return self.linha_atual


    def get_new_contexto ( self ) :
        """
        Gera um novo contexto com uma apontador_de_caracter apontando para o
        último caracter da linha atual.
        """
        new_contexto = apontador_de_caracter(Posicao(self.posicao.pos + 1, self.posicao.linha, self.posicao.coluna), self.linha_atual)
        return new_contexto


    def remover_comentarios ( self ) :
        """
        Remove comentários com regex
        """
        # Bloco de comentário
        self.codigo = re.sub(r"\/\*(\*(?!\/)|[^*])*\*\/", "", self.codigo)
        # Comentários de uma linha
        self.codigo = re.sub(r"(\/\/.+)", "", self.codigo)


    def tokenizar ( self ) :
        """
        Tokeniza o código da classe Lexer e returna uma 
        fila de tokens. Essa fila é a implementada inter-
        namente na classe 'deque' do python, então em vez
        de um método 'dequeue()' temos um 'popleft()' de 
        funcionalidade equivalente. 
        """
        tokens = []
        while self.caracter_atual != None :
            if self.caracter_atual in ' \t\n\r\b\v\f':
                self.avancar()
            elif self.caracter_atual == '#' :
                token = self.make_preprocessor ()
                tokens.append(token)
                self.avancar()
            elif self.caracter_atual == '.' :
                if self.lookahead() not in digitos :
                    self.avancar()
                    tokens.append(Token(TokenTipo.TOKEN_STRUCT_REF))
            elif self.caracter_atual in digitos + '.':
                token = self.make_numbers()
                tokens.append(token)
            elif self.caracter_atual in list(operadores_unicos.keys()) + operadores_duplos :
                token = self.make_operador ()
                if token != None:
                    tokens.append(token)
                self.avancar()
            elif self.caracter_atual in alfabeto + '_' :
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
            elif self.caracter_atual in list(separadores.keys()) :
                token = self.make_separador()
                tokens.append(token)
                self.avancar()
            elif self.caracter_atual not in alfabeto_completo :
                message = 'Caracter fora do alfabeto reconhecido ' + str(self.posicao)
                self.avancar()
                message += '\nlinha:\n\n' + self.contexto
                raise Exception(message)            
            else :
                message = 'Erro durante analise léxica: "' +  self.caracter_atual + '" Caracter não identificado.\n\nposição: ' + str(self.posicao)
                self.avancar()
                message += '\nlinha:\n\n' + self.contexto
                raise Exception(message)            
        tokens.append(Token(TokenTipo.TOKEN_EOF))
        return deque(tokens)


    def make_separador ( self ) :
        """
        Captura um token do tipo Separador
        """
        return Token(separadores[self.caracter_atual])


    def make_operador ( self ) :
        """
        Captura um token do tipo Operador, atentando
        para os operadores duplos (>>, <<, || etc.).
        """
        if self.caracter_atual in list(operadores_unicos.keys()) :
            return Token(operadores_unicos[self.caracter_atual])
        if self.caracter_atual == '+' :
            if self.lookahead() == '=' :
                self.avancar()
                return Token(TokenTipo.TOKEN_SOMA_IG)
            if self.lookahead() == '+' :
                self.avancar()
                return Token(TokenTipo.TOKEN_SOMA_UM)
            return Token(TokenTipo.TOKEN_SOMA)
        if self.caracter_atual == '-' :
            if self.lookahead() == '=' :
                self.avancar()
                return Token(TokenTipo.TOKEN_SUB_IG)
            if self.lookahead() == '-' :
                self.avancar()
                return Token(TokenTipo.TOKEN_SUB_UM)
            if self.lookahead() == '>' :
                self.avancar()
                return Token(TokenTipo.TOKEN_STRUCT_REF)
            return Token(TokenTipo.TOKEN_SUB)
        if self.caracter_atual == '>' :
            if self.lookahead() == '>' :
                self.avancar()
                if self.lookahead() == '=' :
                    self.avancar()
                    return Token(TokenTipo.TOKEN_SHIFT_R_IG)
                return Token(TokenTipo.TOKEN_SHIFT_R)
            if self.lookahead() == '=' :
                self.avancar()
                return Token(TokenTipo.TOKEN_MAIOR_IG)
            return Token(TokenTipo.TOKEN_MAIOR)
        if self.caracter_atual == '<' :
            if self.lookahead() == '<' :
                self.avancar()
                if self.lookahead() == '=' :
                    self.avancar()
                    return Token(TokenTipo.TOKEN_SHIFT_L_IG) 
                return Token(TokenTipo.TOKEN_SHIFT_L)
            if self.lookahead() == '=' :
                self.avancar()
                return Token(TokenTipo.TOKEN_MENOR_IG)            
            return Token(TokenTipo.TOKEN_MENOR)
        if self.caracter_atual == '|' :
            if self.lookahead() == '|' :
                self.avancar()
                return Token(TokenTipo.TOKEN_OR)
            if self.lookahead() == '=' :
                self.avancar()
                return Token(TokenTipo.TOKEN_OR_IG)            
            return Token(TokenTipo.TOKEN_ORB)
        if self.caracter_atual == '!' :
            if self.lookahead() == '=' :
                self.avancar()
                return Token(TokenTipo.TOKEN_NOT_IG)
            return Token(TokenTipo.TOKEN_NOT)
        if self.caracter_atual == '&' :
            if self.lookahead() == '&' :
                self.avancar()
                return Token(TokenTipo.TOKEN_AND)
            if self.lookahead() == '=' :
                self.avancar()
                return Token(TokenTipo.TOKEN_AND_IG)            
            return Token(TokenTipo.TOKEN_AMPERSAND)
        if self.caracter_atual == '=' :
            if self.lookahead() == '=' :
                self.avancar()
                return Token(TokenTipo.TOKEN_IGUAL)
            return Token(TokenTipo.TOKEN_ATRIB)
        if self.caracter_atual == '*' :
            if self.lookahead() == '=' :
                self.avancar()
                return Token(TokenTipo.TOKEN_MULT_IG)
            return Token(TokenTipo.TOKEN_ASTERISCO)
        if self.caracter_atual == '%' :
            if self.lookahead() == '=' :
                self.avancar()
                return Token(TokenTipo.TOKEN_MOD_IG)
            return Token(TokenTipo.TOKEN_MOD)
        if self.caracter_atual == '^' :
            if self.lookahead() == '=' :
                self.avancar()
                return Token(TokenTipo.TOKEN_XOR_IG)
            return Token(TokenTipo.TOKEN_XOR)
        if self.caracter_atual == '/' :
            if self.lookahead() == '/' :
                self.avancar_ate(chars=['\n', None])
            if self.lookahead() == '=' :
                self.avancar()
                return Token(TokenTipo.TOKEN_DIV_IG)
            if self.lookahead() == '*' :
                self.avancar(2)
                while self.lookahead() not in ['/', None] :
                    self.avancar_ate(chars=['*', None])
                self.avancar()
            else :
                return Token(TokenTipo.TOKEN_DIV)


    def make_numbers ( self ) :
        """
        Captura um token do tipo número, seja ele inteiro (
        decimal, binário, octal ou hexadecimal) ou real ( no-
        tação científica ou não).
        """
        numero_final = ''

        while self.caracter_atual != None and self.caracter_atual not in separadores :
            numero_final += self.caracter_atual
            self.avancar()

        if numero_final.startswith('0b') or numero_final.startswith('0B') :
            return Token(TokenTipo.TOKEN_BIN, numero_final )
        if numero_final.startswith('0x') or numero_final.startswith('0X') :
            return Token(TokenTipo.TOKEN_HEXA, numero_final )
        if numero_final.startswith('0') and len(numero_final) > 1 :
            return Token(TokenTipo.TOKEN_OCT, numero_final )
        if '.' in numero_final :
            return Token(TokenTipo.TOKEN_REAL, numero_final )
        return Token(TokenTipo.TOKEN_INT, numero_final)


    def make_preprocessor ( self ) :
        """
        Captura um token do tipo preprocessador (define,
        include e pragma)
        """
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
        """
        Captura uma palavra do tipo identificador ou keyword
        """
        token_str = ''
        while self.caracter_atual != None and self.caracter_atual in alfanumu :
            token_str += self.caracter_atual
            self.avancar()
        if token_str in keywords :
            return Token(TokenTipo.TOKEN_KEYWORD, valor=token_str)
        else :
            return Token(TokenTipo.TOKEN_IDENT, valor=token_str)


    def parse_string ( self ) :
        """
        Captura um token do tipo string
        """
        token_str = ''
        while self.caracter_atual not in ( None, '"' ) :
            token_str += self.caracter_atual
            self.avancar()
        if self.caracter_atual == '"' :
            self.avancar()
        return Token(TokenTipo.TOKEN_STR, valor=token_str)


    def parse_char ( self ) :
        """
        Captura um token do tipo char
        """
        token_str = ''
        while self.caracter_atual not in ( None, "'" ) :
            token_str += self.caracter_atual
            self.avancar()
        if self.caracter_atual == "'" :
            self.avancar()
        return Token(TokenTipo.TOKEN_CHAR, valor=token_str)