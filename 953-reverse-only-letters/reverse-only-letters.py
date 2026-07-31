class Solution(object):
     def letter(self, ch):
         x = ord(ch)
         return (65 <= x <= 90) or (97 <= x <= 122)

     def reverseOnlyLetters(self, s):
         s=list(s)

         left = 0
         right=len(s)-1

         while left< right:
             if self.letter(s[left]) and self.letter(s[right]):
                 s[right],s[left]=s[left],s[right]
                 left += 1
                 right -=1
             elif self.letter(s[left]):
                 right -= 1
             elif self.letter(s[right]):
                 left += 1
             else :
                 left += 1
                 right -=1

         return ''.join(s)

        