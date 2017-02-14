def count_holes(n):
    hole_dic={0:1,1:0,2:0,3:0,4:1,5:0,6:1,7:0,8:2,9:1}
    z=[]
    try:
        if type(n)==int or type(n)==str or type(n)==long:
            if type(n)==int or type(n)==long:
                n=str(n)
            if type(n)==str:
                n=str(int(n))
            n=list(n)
            if n[0]=='-':
                del(n[0])
            for i in n:
                i=int(i)
                z.append(hole_dic[i])
            q=sum(z[0:len(z)])
            return q
        else:
            return 'ERROR'
    except Exception:
        return 'ERROR'
