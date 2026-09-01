class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix=[0]
        rs=0

        for i in range(len(gain)):
            rs += gain[i]
            prefix.append(rs)

        return max(prefix)