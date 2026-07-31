class Solution(object):
 def isVowel(self, ch):
        return ch in "aeiouAEIOU"
    
 def reverseVowels(self, s):
          
         s= list(s)

         left= 0
         right=len(s)-1
          
         while left < right:
             if self.isVowel(s[left]) and self.isVowel(s[right]):
                 s[left],s[right] = s[right],s[left]
                 left +=1
                 right -=1
             elif self.isVowel(s[left]):
                 right -=1
             elif self.isVowel(s[right]):
                 left +=1
             else:
                 left +=1
                 right -=1
         return ''.join(s)
                     





        