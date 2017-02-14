def encode_morze(text):
    morze = {
        "A" : ".-", 
        "B" : "-...", 
        "C" : "-.-.", 
        "D" : "-..", 
        "E" : ".", 
        "F" : "..-.", 
        "G" : "--.", 
        "H" : "....", 
        "I" : "..", 
        "J" : ".---", 
        "K" : "-.-", 
        "L" : ".-..", 
        "M" : "--", 
        "N" : "-.", 
        "O" : "---", 
        "P" : ".--.", 
        "Q" : "--.-", 
        "R" : ".-.", 
        "S" : "...", 
        "T" : "-", 
        "U" : "..-", 
        "V" : "...-", 
        "W" : ".--", 
        "X" : "-..-", 
        "Y" : "-.--", 
        "Z" : "--..", 
    }
    out = ''
    for i in text:
        add = ''
        if i == ' ':
            add = '____'
        elif i.upper() in morze.keys():
            to_add = morze[i.upper()].replace('.','^_').replace('-','^^^_') + '__'
        out = out + add    
    if len(encoded):
        while encoded[-1] == '_':
            out = out[:-1]    
    return out
