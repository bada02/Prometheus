class Student():
    def __init__(self,name,conf):
        self.name=name
        self.conf=conf
        self.lst=[]
        self.lst=[0]*self.conf["lab_num"]
        self.k=self.conf['k']
        self.lab_max=self.conf['lab_max']
        self.exam_max=self.conf['exam_max']
        self.exam=float(0)
        
    def make_lab(self, m,n=None):
        if m>self.lab_max:
            m=self.lab_max
        if n<=len(self.lst) and n!=None:
            self.lst[n]=m
        elif n==None:
            self.lst[self.lst.index(0)]=m
        u=str(self.lst)
        u=u[1:len(u)-1]
        u=u.replace(",", "")
        return "labs: %s, exam: %d" %(u,self.exam)
        
    def make_exam(self,m):
        if m>self.exam_max:
            m=self.exam_max
        self.exam=m
        u=str((self.lst))
        u=u[1:len(u)-1]
        u=u.replace(",", "")
        return "labs: %s, exam: %d" %(u,self.exam)
            
    def is_certified(self):
        coef=(float(sum(self.lst))+self.exam)
        coef=round(coef,1)
        if coef/100>=self.k:
            flag=True
        else:
            flag=False
        return coef, flag
