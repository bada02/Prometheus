def find_fraction(inp):
    if inp<2:
        return False
    if float(inp/2)==inp/2:
        upp=inp/2-1
        low=inp/2+1
    else:
        upp=inp/2
        low=inp/2+1
    while upp!=0:
        a=upp
        b=low
        while a!=0 and b!=0:
            if a>b:
                a=a%b
            else:
                b=b%a
            com=a+b
        if com==1:
            return upp,low
        upp=upp-1
        low=low+1
    return False
