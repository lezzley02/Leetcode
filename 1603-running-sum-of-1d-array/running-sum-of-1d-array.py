class Solution(object):
    def runningSum(self, nums):
     s=0
     running_sum=[]
     for i in nums :
         s+=i
         running_sum.append(s)
     return running_sum