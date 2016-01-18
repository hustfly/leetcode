class Solution(object):
  def addDigits(self,num):
    input=num
    while(input>=10):
      s=0
      while(input/10>0):
        s=s+input%10
        input=input/10
      s+=input
      print s
      input=s
    return input

b = Solution()
print b.addDigits(38)
