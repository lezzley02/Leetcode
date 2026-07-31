class Solution(object):
    def threeSum(self, nums):
         nums.sort()
         result= set()
         for i in range(len(nums)):
             left = i + 1
             right = len(nums)-1
             
             while  left < right:
                 sum = nums[i] + nums[left] + nums[right]
                 target =0
                 if sum == target:
                     result.add((nums[i] ,nums[left] ,nums[right]))
                     left += 1
                     right -= 1
                 elif sum >target:
                     right -= 1
                 else :
                     left +=1
         return list(result)


                    
            