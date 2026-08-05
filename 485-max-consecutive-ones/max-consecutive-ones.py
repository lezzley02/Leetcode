class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
     mx= 0
     count = 0
     for i in range (len(nums)):
         if nums[i]==1:
             count+=1
             mx=max(count, mx)
         else :
            count = 0
     return mx
        
        