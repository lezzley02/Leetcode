class Solution(object):
    def selfDividingNumbers(self, left, right):
        answer = []

        for num in range(left, right + 1):

            temp = num
            valid = True

            while temp > 0:
                digit = temp % 10

                if digit == 0:
                    valid = False
                    break

                if num % digit != 0:
                    valid = False
                    break

                temp = temp // 10

            if valid:
                answer.append(num)

        return answer