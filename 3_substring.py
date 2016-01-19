Class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head=0
        maxl=0
        sub={}
        for i in range(len(s)):
            if(s[i] in sub):
                head=max(sub[s[i]]+1,head)
            l=i-head+1
            maxl=l if l>maxl else maxl
            sub[s[i]]=i    
        return maxl
