def seta ( pos, st ) :
    string_final = st + '\n'
    for i in range(len(st)) :
        string_final += '^' if i == pos.pos else ' '
    if pos.pos >= len(st) :
        string_final += '^'
    return string_final