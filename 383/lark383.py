ass Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        
        for i in ransomNote:
            if i not in magazine:
                return False
            elif ransomNote.count(i) > magazine.count(i):
                return False
            else:
                continue
            
            
        return True
