class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if not ransomNote:
            return True
        elif not magazine:
            return False
        char_dict = {}
        for char in magazine:
            try:
                char_dict[char] += 1
            except:
                char_dict[char] = 1
        for char in ransomNote:
            try:
                char_dict[char] -= 1
                if char_dict[char] < 0:
                    return False
            except:
                return False
        return True

if __name__ == "__main__":
	res = Solution()
	print(res.canConstruct("xcdfsaf", "cxbklsdjfaiojsadf"))
