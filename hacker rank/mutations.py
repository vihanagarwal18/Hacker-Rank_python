def mutate_string(string, position, character):
    newstring=string[0:position]+character+string[position+1:]
    return newstring