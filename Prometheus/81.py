class CombStr(str):
    def __init__(self, inp):
        self.inp=inp
        
    def count_substrings(self, length):
        inp=self.inp
        strlst=[]
        found=[]
        counter=0
        if length==0:
            return 0
        for item in inp:
            
            s=inp[counter:counter+length]
            if len(s)==length:
                strlst.append(s)
            counter=counter+1
        for element in strlst:
            flag=False
            for i in found:
                if i==element and str(i)==str(element):
                    flag=True
            if not flag:
                found.append(element)
        return len(found)
