class Solution:
    def MissingNumber(self,array,n):
        # code here
        x = set(array)
        for i in range(1,n+1):
            if i not in x:
                return i