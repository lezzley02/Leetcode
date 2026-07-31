class Solution(object):
    def findNumbers(self, nums):
         count= 0

         for num in nums:
             digit=0
             temp=num

             while temp > 0:
                 digit +=1
                 temp=temp//10

             if digit % 2 ==0 :
                 count+=1

         return count


        