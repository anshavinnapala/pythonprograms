class student:
    def _init_(self,m1,m2):
        self.m1=m1
        self.m2=m2
        
    def _add_(self,other):
        m1 = self.m1+other.m1
        m2 = self.m2+other.m2
        s3 = student(m1,m2)
        
        return s3
    
    def _gt_(self,other):
        r1 = self.m1+self.m2
        r2 = other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False
        
    def _str_(self):
        return '{} {}'.format(self.m1, self.m2)
        
s1 = student(58,69)
s2 = student(69,65)

s3=s1+s2

if s1>s2:
    print("s1 Wins")
else:
    print("s2 Wins")
    
a=9
print(a._str_())

print(s1)
print(s2)
