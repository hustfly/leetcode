Class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index=[]
        i=1
        for num in nums:
            r=target-num
            if(r in nums[i:]):
                index.append(i)
                index.append(nums[i:].index(r)+i+1)
                break
            i=i+1
        return index
