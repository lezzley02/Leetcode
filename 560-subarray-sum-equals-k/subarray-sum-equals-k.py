class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
         Subcount =0
         csum = 0
         seen ={0:1}


         for i in nums:
             csum += i
             req = csum - k
             if req in seen :
                  Subcount += seen[req]
             seen[csum]=seen.get(csum,0)+1
         return Subcount

         
            