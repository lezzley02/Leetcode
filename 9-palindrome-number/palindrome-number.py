class Solution(object):
    def isPalindrome(self, x):
         r = str(x)[::-1]

         if r != str(x):
             return False
         else :
             return True
           
        