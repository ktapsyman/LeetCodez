class Solution(object):
	def Heapify(self, DataList, Size):
		Layer = 1
		ParentIndex = 1
		while ParentIndex < Size:
			ParentIndex = ParentIndex << 1
			Layer += 1
		ParentIndex = 2**(Layer-1) - 2
		while ParentIndex >= 0:
			LeftIndex = 2 * ParentIndex + 1
			if LeftIndex < Size:
				TmpParent = ParentIndex
				TmpChildL = LeftIndex
				TmpChildR = TmpChildL + 1
				while TmpChildL < Size:
					if DataList[TmpChildL] > DataList[TmpParent]:
						if TmpChildR < Size and DataList[TmpChildL] < DataList[TmpChildR]:
							DataList[TmpParent] , DataList[TmpChildR] = DataList[TmpChildR] , DataList[TmpParent]
							TmpParent = TmpParent * 2 + 2
							TmpChildL = TmpChildR * 2 + 1
						else:
							DataList[TmpParent] , DataList[TmpChildL] = DataList[TmpChildL] , DataList[TmpParent]
							TmpParent = TmpParent * 2 + 1
							TmpChildL = TmpChildL * 2 + 1
					elif TmpChildR < Size and  DataList[TmpChildR] > DataList[TmpParent]:
						DataList[TmpParent] , DataList[TmpChildR] = DataList[TmpChildR] , DataList[TmpParent]
						TmpParent = TmpParent * 2 + 2
						TmpChildL = TmpChildR * 2 + 1
					else:
						break
					TmpChildR = TmpChildL + 1
			ParentIndex = ParentIndex - 1
		
	def HeapSort(self, DataList):
		Size = len(DataList)
		Iterator = len(DataList)
		self.Heapify(DataList, Size)
		while(Size > 0):
			DataList[0], DataList[Size - 1] = DataList[Size - 1], DataList[0]
			Size = Size - 1
			self.Heapify(DataList, Size)

	def sortColors(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		self.HeapSort(nums)
