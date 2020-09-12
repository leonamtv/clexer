class Token () :
    
    def __init__ ( self, tipo, valor = None ) :
        self.tipo = tipo
        self.valor = valor
    
    def __repr__ ( self ) :
        return f'[ { self.tipo }' + ( f': { self.valor } ]' if self.valor != None else ' ]' )