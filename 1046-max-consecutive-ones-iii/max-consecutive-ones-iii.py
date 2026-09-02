class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
         curr_sum=0
         left=0
         max_length=0

         for right in range(len(nums)):
            if nums[right]== 0:
                 curr_sum += 1

            while curr_sum > k:
                 if nums[left]== 0:
                     curr_sum -= 1
                 left += 1

            length= right - left + 1
            max_length=max(max_length,length)
         return max_length