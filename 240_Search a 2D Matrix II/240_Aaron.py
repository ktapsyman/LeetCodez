class Solution(object):
  def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix:
      return False
    rowCnt = len(matrix)
    colCnt = len(matrix[0])
    
    rowIdx = 0
    colIdx = colCnt - 1    
    while colIdx >= 0 and rowIdx < rowCnt:
      if target == matrix[rowIdx][colIdx]:
        return True
      elif target < matrix[rowIdx][colIdx]:
        colIdx -= 1
      else:
        rowIdx += 1
    return False


if __name__ == "__main__":
  res = Solution()
  matrix = [
    [1,2,3,4,5],
    [2,4,5,7,8],
    [4,5,7,8,9]
  ]
  target = 6
  print(res.searchMatrix(matrix, target))
