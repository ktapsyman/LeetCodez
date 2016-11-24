class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if p:
            len_s = len(s)
            len_p = len(p)
            if len_s < len_p:
                return []

            MAX_LEN_LIMIT = 20100
            if len_s > MAX_LEN_LIMIT or len_p > MAX_LEN_LIMIT:
                return False
            
            # charCnt_s = {}
            charCnt_p = {}
            for i in range(0, len_p):
                try:
                    charCnt_p[p[i]] += 1
                except:
                    charCnt_p[p[i]] = 1

            res = []
            left = 0; right = 0; cnt = len_p
            backup_charCnt_p = dict(charCnt_p)
            while right < len_s:
                try:
                    if charCnt_p[s[right]] > 0:
                        cnt -= 1
                    charCnt_p[s[right]] -= 1
                except:
                    right += 1
                    left = right
                    charCnt_p = dict(backup_charCnt_p)
                    cnt = len_p
                    continue
                right += 1

                if cnt == 0:
                    res.append(left)
                
                if right - left == len_p:
                    charCnt_p[s[left]] += 1
                    if charCnt_p[s[left]] > 0:
                        cnt += 1
                    left += 1
                        
            # last_idx = len_s - len_p
            # for i in range(0, last_idx):
            #     if charCnt_s == charCnt_p:
            #         res.append(i)

            #     if charCnt_s[s[i]] == 1:
            #         del charCnt_s[s[i]]
            #     else:
            #         charCnt_s[s[i]] -= 1
            #     temp_idx = i + len_p
            #     try:
            #         charCnt_s[s[temp_idx]] += 1
            #     except:
            #         charCnt_s[s[temp_idx]] = 1
            # if charCnt_s == charCnt_p:
            #     res.append(last_idx)

            return res