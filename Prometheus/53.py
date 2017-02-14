def super_fibonacci(p,q):
    k=[1]*q
    while len(k)<p:
        z=sum(k[-q:])
        k.append(z)
    return z
