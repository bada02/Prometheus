def counter (x,y):
    x=list(str(x))
    y=list(str(y))
    m=0
    n=0
    z=[]
    for i in y:
        flag=False
        for i in x:
            if y[m]==x[n]:
                flag= True
            if flag==True:
                z.append(x[n])
            n=n+1
            flag=False
        n=0
        m=m+1
    n=0
    for i in z:
        a= z[n]  
        q=n+1  
        for i in z[q:]:
            if a==z[q] and type(a)==type(z[q]):
                z[q]=None
            q=q+1
        n=n+1
    for i in range(len(z)):
        try:
            z.remove(None)
        except:
            break
    return len(z)
