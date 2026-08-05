class Solution(object):
    def maxPower(self, s):
         mx=1
         count=1
         for i in range(1,len(s)):
             if s[i] == s[i-1]:
                 count += 1
             else :
                 mx=max(mx,count)
                 count=1
             
         return max(mx,count)
        