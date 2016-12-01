class Solution(object):
	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		len_s = len(s)
		res = []
		if len_s < 4 or len_s > 12:
			return res

		MAX_VALID_VAL = 255
		def is_valid_ip_col(str):
			len_str = len(str)
			if len_str > 3 or len_str == 0:
				return False
			elif len_str == 3:
				if str[0] == "0" or int(str) > MAX_VALID_VAL:
					return False
			elif len_str == 2:
				if str[0] == "0":
					return False
			return True

		COL_MAX_CNT = 3
		col = [0,0,0,0]
		col_start_idx = [0,1,2,3]
		for i in range(1, COL_MAX_CNT + 1):
			col[0] = s[:i]
			if not is_valid_ip_col(col[0]):
				continue
			col_start_idx[1] = i
			for j in range(1, COL_MAX_CNT + 1):
				col[1] = s[ col_start_idx[1] : col_start_idx[1] + j ]
				if not is_valid_ip_col(col[1]):
					continue
				col_start_idx[2] = col_start_idx[1] + j
				for k in range(1, COL_MAX_CNT + 1):
					col_start_idx[3] = col_start_idx[2] + k
					col[3] = s[col_start_idx[3]:]
					if not is_valid_ip_col(col[3]):
						continue
					col[2] = s[ col_start_idx[2] : col_start_idx[2] + k ]
					if not is_valid_ip_col(col[2]):
						continue
					
					res.append(".".join(col))

		return res

if __name__ == "__main__":
	res = Solution()
	print(res.restoreIpAddresses("11111"))
