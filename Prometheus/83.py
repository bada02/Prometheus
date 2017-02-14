def make_sudoku(size=1):
    res=[]
    c=0
    q=0
    n=range(1,size*size+1,1)
    while len(res)<(size*size):
        if len(res)%size==0:
            c=0
            q=q+1
        line= n[(size*c)+q:]+n[:(size*c)+q]
        res.append(line)
        c=c+1
    return res
