class Solution(object):
  def isIsomorphic(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
      return False
    # if it is a large {key: value} in dict, the list way is slower than dict way
    # usedList = []
    hashTable = {}
    valueTable = {}
    for i in range(len(s)):
      if s[i] in hashTable:
        if hashTable[s[i]] != t[i]:
          return False
        else:
          continue
      else:
        # if t[i] in usedList:
        if t[i] in valueTable:
          return False
        # usedList.append(t[i])
        hashTable[s[i]] = t[i]
        valueTable[t[i]] = s[i]
    return True

if __name__ == "__main__":
  s = 'egg'
  t = 'add'
  res = Solution()
  print(res.isIsomorphic(s, t))
