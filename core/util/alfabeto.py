import string

alfabeto        = string.ascii_letters

digitos         = '0123456789'
digitos_bin     = digitos[:2]
digitos_hexa    = digitos + alfabeto[:6] + alfabeto[:6].upper()
digitos_oct     = digitos[:8]

alfanum         = alfabeto + digitos
alfanumu        = alfanum + '_'