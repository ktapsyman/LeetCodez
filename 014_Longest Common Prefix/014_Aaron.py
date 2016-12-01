class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		list_len = len(strs)
		idx = 0
		res = ""
		while True:
			try:
				now_char = strs[0][idx]
			except:
				return res
			try:
				for i in range(1, list_len):
					if strs[i][idx] != now_char:
						return res
			except:
				return res
			res += now_char
			idx += 1

if __name__ == "__main__":
	strs = ["asdf", "aser", "asio"]
	res = Solution()
	print(res.longestCommonPrefix(strs))