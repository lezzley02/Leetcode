class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
         sum = 0
         n=x
         while n>0:
              digit=n % 10
              sum = sum +digit
              n=n // 10
              
         if x%sum == 0:
             return sum 
         else :
             return -1

        