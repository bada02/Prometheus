class SuperStr(str):


    def is_repeatance(self, s):
        if isinstance(s,str) and len(s)>0 and len(self)>0:
            n=len(self)/len(s)
            if self==(s*n):
                return True
            else:
                return False
        else:
            return False
            
    def is_palindrom(self):
        flag = True
        s_cleaned = self.lower().replace(' ', '')
        s_length = len(s_cleaned)
        for i in range(s_length / 2):
            if s_cleaned[i] != s_cleaned[s_length-1-i]:
                flag = False
        return flag
