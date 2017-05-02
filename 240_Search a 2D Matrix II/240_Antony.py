class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #import numpy as np
        #k = np.ravel(matrix)
        k = [x for y in matrix for x in y]

        if target in k:
            return True
        else:
            return False
