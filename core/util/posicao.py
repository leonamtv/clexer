class Posicao :
    def __init__ ( self ) :
        self.pos     = -1
        self.linha   = 0
        self.coluna  = -1

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