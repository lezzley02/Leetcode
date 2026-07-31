class Solution(object):
    def mergeAlternately(self, word1, word2):
         lst=[]
         length=max(len(word1),len(word2))
         for i in range(length):
             if i < len(word1):
                 lst.append(word1[i])
             if i < len(word2):
                 lst.append(word2[i])

         return ''.join(lst)
        