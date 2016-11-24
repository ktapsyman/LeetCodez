class Solution(object):
    def divide(self, dividend, divisor):
        MAX_INT=2147483647
        count = 0
        a=abs(dividend)
        b=abs(divisor)
        string1 = str(a)
        string2 = str(b)
        
        #if a>MAX_INT:count=MAX_INT
        
        if len(string1)<len(string2):
            count = 0
        
        elif len(string1) <= len(string2)+2:
            while a >= b:
                a = a-b
                count = count+1
                
        else:
            i = len(string2)+1
            while len(string1)>len(string2):
                x = int(string1[:i])
                count = int(str(count)+'0')
                while x>=b:
                    x = x - b
                    count = count+1
                string1 = str(x)+string1[i:]
                
        
        if abs(dividend+divisor) < abs(dividend)+abs(divisor):
            count = 0-count
            if abs(count)>MAX_INT+1:count=MAX_INT
        if count>MAX_INT:count=MAX_INT
        
        return count     
