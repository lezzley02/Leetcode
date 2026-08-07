class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Count whites in the first window
        white = 0
        for i in range(k):
            if blocks[i] == 'W':
                white += 1

        ans = white

        # Slide the window
        for i in range(k, len(blocks)):
            # Remove left character
            if blocks[i - k] == 'W':
                white -= 1

            # Add new right character
            if blocks[i] == 'W':
                white += 1

            ans = min(ans, white)

        return ans