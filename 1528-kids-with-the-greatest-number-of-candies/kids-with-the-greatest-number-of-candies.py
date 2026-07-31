class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
         maxi=max(candies)
         answer=[]
         
         for candy in candies :
             if candy + extraCandies >= maxi:
                  answer.append(True)
             else :
                 answer.append(False)
        
         return answer
        