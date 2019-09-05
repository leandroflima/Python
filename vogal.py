def vogal(letra):
    vogais = "aeiou"
    for vogal in vogais:
        if (letra.capitalize() == vogal.capitalize()):
            return True
    return False
    
