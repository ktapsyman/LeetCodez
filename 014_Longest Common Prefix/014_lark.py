class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if 0 == len(strs) or "" in strs:
            return ""
        
        if len(strs)==1:
            return strs[0]
            
        MinLenStr = min(strs, key=len)
        
        prifix = ""
        ind = -1
        for j in MinLenStr:
            ind = ind+1
            for k in strs:
                if k[ind] == j:
                    continue
                else:return prifix
            prifix=prifix+j
        return prifix
