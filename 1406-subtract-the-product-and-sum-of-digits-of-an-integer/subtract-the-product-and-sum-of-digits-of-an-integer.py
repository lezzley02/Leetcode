class Solution(object):
    def subtractProductAndSum(self, n):
        sum = 0
        product = 1

        while n > 0:
            digit = n % 10
            product = product * digit
            sum = sum + digit
            n //= 10

        return product - sum