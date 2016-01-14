class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if(num<10):
            return num
        else:
            s = 0
            while(num/10 > 0):
                s = s + num % 10
                num = num /10
            s = s + num
            return self.addDigits(s)


b = Solution()
print b.addDigits(38)
