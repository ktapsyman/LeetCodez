class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if None == strs or 0 == len(strs):
			return ""
		Candidate = min(strs, key=len)
		strs.remove(Candidate)
		CandidateLen = len(Candidate)
		CheckmateCount = 0
		StrListCount = len(strs)
		while CandidateLen > 0:
			for Otherstr in strs:
				if 0 != Otherstr.find(Candidate):
					Candidate = Candidate[0:CandidateLen - 1]
					CandidateLen = CandidateLen - 1
				else:
					CheckmateCount += 1
			if CheckmateCount == StrListCount:
				return Candidate
			else:
				CheckmateCount = 0
		return Candidate