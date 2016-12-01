class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        else:
            max_common_prefix = 0
            min_str = min(strs, key=len)
            s = len(min_str)
            for k in range(s):
                if len(set([i[k] for i in strs])) == 1:
                    max_common_prefix += 1
                else:
                    break
            return strs[0][0:max_common_prefix]
