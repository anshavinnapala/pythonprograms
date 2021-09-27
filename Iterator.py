class TopTen:
    def _init_(self):
        self.num=1
        
    def _iter_(self):
        return self
        
    def _next_(self):
        
        if self.num<=10:
            val = self.num
            self.num+=1
            
            return val
        else:
            raise StopIteration
            
values = TopTen()
print(next(values))

for i in values:
    print(i)
