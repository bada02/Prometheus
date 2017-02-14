def saddle_point(mat):
    mattr=[]
    flag=False
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            if j==0:
                mattr.append([])
            mattr[i].append(mat[j][i])
    for i in mat:        
        for j in mattr:    
            if min(i)==max(j):                            
                z=(j.index(max(j)),i.index(min(i)))
                flag=True
                return z
    if flag==False:
        return False
