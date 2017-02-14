def convert_n_to_m(x,n,m):
    out=[]
    ans=[]
    z=0
    k=0
    empty=""
    alphabet="0123456789abcdefghijklmnopqrstuvwxyz"
    
    if (isinstance(x,str) and x[0]!="-") or (isinstance(x,int)and x>=0)or (isinstance(x,long)and x>=0):
        alphabet=alphabet.upper()
        x=str(x)
        x=x.upper()
        if n==m:
            return x
        for i in x:            
            if alphabet.index(i)>=n:
                return False
            else:
                z=z+alphabet.index(i)*(n**(len(x)-1-k))
                k=k+1
                print z
        if m==1:
            return "0"*z
        if z==0:
            return 0
        print z
        while z!=0:       
            out.append(z%m)
            z=z/m
        out.reverse()
        for it in out:
            ans.append(alphabet[it])
        return empty.join(ans)
    else:
        return False
