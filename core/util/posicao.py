class Posicao :
    def __init__ ( self, pos=-1, linha=0, coluna=-1 ) :
        self.pos     = pos
        self.linha   = linha
        self.coluna  = coluna

    def avancar ( self, quebrar_linha = False ) :
        self.pos     += 1
        self.coluna  += 1
        if quebrar_linha:
            self.linha += 1
            self.coluna = 0
    
    def __str__ ( self ) :
        return f"[ lin: {self.linha}, col: {self.coluna} ]"

    def __repr__ ( self ):
        return str(self)

    def __copy__ ( self ) :
        newPos = Posicao()
        newPos.pos = self.pos
        newPos.linha = self.linha
        newPos.coluna = self.coluna
        return newPos