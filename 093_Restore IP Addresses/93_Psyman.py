class Solution(object):
	PermutationOfLen = {}
	def __init__(self):
		self.PermutationOfLen[4] = [
			[1,1,1,1],
			]
		self.PermutationOfLen[5] = [
			[2,1,1,1],
			[1,2,1,1],
			[1,1,2,1],
			[1,1,1,2],
			]
		self.PermutationOfLen[6] = [
			[2,2,1,1],
			[2,1,2,1],
			[2,1,1,2],
			[1,1,2,2],
			[1,2,1,2],
			[1,2,2,1],
			[3,1,1,1],
			[1,3,1,1],
			[1,1,3,1],
			[1,1,1,3],			
			]
		self.PermutationOfLen[7] = [
			[3,2,1,1],
			[3,1,2,1],
			[3,1,1,2],
			[2,1,1,3],
			[2,1,3,1],
			[2,3,1,1],
			[1,1,2,3],
			[1,1,3,2],
			[1,2,3,1],
			[1,2,1,3],
			[1,3,2,1],
			[1,3,1,2],
			[1,2,2,2],
			[2,1,2,2],
			[2,2,1,2],
			[2,2,2,1],
			]
		self.PermutationOfLen[8] = [
			[2,2,2,2],
			[3,3,1,1],
			[3,1,3,1],
			[3,1,1,3],
			[1,3,3,1],
			[1,3,1,3],
			[1,1,3,3],
			[3,2,2,1],
			[3,2,1,2],
			[3,1,2,2],
			[2,1,2,3],
			[2,1,3,2],
			[2,2,1,3],
			[2,2,3,1],
			[2,3,1,2],
			[2,3,2,1],
			[1,3,2,2],
			[1,2,3,2],
			[1,2,2,3],
			]
		self.PermutationOfLen[9] = [
			[3,3,2,1],
			[3,3,1,2],
			[3,2,1,3],
			[3,2,3,1],
			[3,1,2,3],
			[3,1,3,2],
			[2,1,3,3],
			[2,3,1,3],
			[2,3,3,1],
			[1,2,3,3],
			[1,3,2,3],
			[1,3,3,2],
			[3,2,2,2],
			[2,3,2,2],
			[2,2,3,2],
			[2,2,2,3],
			]
		self.PermutationOfLen[10] = [
			[3,3,2,2],
			[3,2,2,3],
			[3,2,3,2],
			[2,2,3,3],
			[2,3,3,2],
			[2,3,2,3],
			[1,3,3,3],
			[3,1,3,3],
			[3,3,1,3],
			[3,3,3,1],			  
			]
		self.PermutationOfLen[11] = [
			[3,3,3,2],
			[3,2,3,3],
			[3,3,2,3],
			[2,3,3,3],
			]
		self.PermutationOfLen[12] = [
			[3,3,3,3],
			]
	def IPChecker(self, IpComponentList):
		if 4 != len(IpComponentList):
			return False
		for Component in IpComponentList:
			if 0 > Component or 255 < Component:
				return False
		return True
	def CheckInvalidZeros(self, Numstr):
		Len = len(Numstr)
		Num = int(Numstr)
		if 1 != Len and 10 > Num:
			return False
		elif 3 == len(Numstr) and 100 > Num:
			return False
		return True
	def restoreIpAddresses(self, IpString):
		"""
		:type s: str
		:rtype: List[str]
		"""
		IPLen = len(IpString)
		if 4 > IPLen or 12 < IPLen:
			return []
		TargetTable = self.PermutationOfLen[IPLen]
		RetIPDic = {}
		#RetList = []
		for SplitPositionList in TargetTable:
			DotPos1 = SplitPositionList[0]
			DotPos2 = SplitPositionList[0] + SplitPositionList[1]
			DotPos3 = SplitPositionList[0] + SplitPositionList[1] + SplitPositionList[2]
			DotPos4 = SplitPositionList[0] + SplitPositionList[1] + SplitPositionList[2] + SplitPositionList[3]
			IpShred1 = IpString[0:DotPos1]
			IpShred2 = IpString[DotPos1:DotPos2]
			IpShred3 = IpString[DotPos2:DotPos3]
			IpShred4 = IpString[DotPos3:DotPos4]
			if False == (self.CheckInvalidZeros(IpShred1) and self.CheckInvalidZeros(IpShred2) and self.CheckInvalidZeros(IpShred3) and self.CheckInvalidZeros(IpShred4)):
				continue;
			ComponentList = [ 
				int(IpShred1), 
				int(IpShred2),
				int(IpShred3),
				int(IpShred4)
				]
			if True == self.IPChecker(ComponentList):
				#RetList.append('.'.join(str(IpComp) for IpComp in ComponentList))
				ConstructedIPStr = '.'.join(str(IpComp) for IpComp in ComponentList)
#				if False == RetIPDic.has_key(ConstructedIPStr):
				RetIPDic[ConstructedIPStr] = ""
		return list(RetIPDic.keys())
			