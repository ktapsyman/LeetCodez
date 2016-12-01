class Solution(object):
    def findAnagrams(self, SourceStr, PatternStr):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if None == SourceStr or 0 == len(SourceStr) or len(PatternStr) > len(SourceStr):
            return []
        PatternLen = len(PatternStr)
        SourceLen = len(SourceStr)
        PatternCharDic = {}
        for Character in PatternStr:
            if True == PatternCharDic.has_key( Character ):
                continue
            PatternCharDic[Character] = PatternStr.count( Character )
        RetList = []
        Range = SourceLen - PatternLen + 1
        CharIndex = 0
        LocalCharDic = {}
        FirstSlice = SourceStr[0:PatternLen]
        for Character in FirstSlice:
            LocalCharDic[Character] = FirstSlice.count( Character )
        while CharIndex < SourceLen - PatternLen + 1:
            CurrentSlice = SourceStr[CharIndex:CharIndex+PatternLen]
            IsAnagrams = True
            ShiftCandidate = [1]
            for Key in LocalCharDic:
                if False == PatternCharDic.has_key(Key):
                    IsAnagrams = False
                    ShiftCandidate.append(CurrentSlice.rfind(Key)+1)
                elif LocalCharDic[Key] > PatternCharDic[Key]:
                    IsAnagrams = False
                    ShiftCandidate.append(CurrentSlice.find(Key)+1)
                elif LocalCharDic[Key] < PatternCharDic[Key]:
                    IsAnagrams = False
                    ShiftCandidate.append( PatternCharDic[Key] - LocalCharDic[Key])
            if True == IsAnagrams:
                RetList.append(CharIndex)
                
            SkipStep = max(ShiftCandidate)
            CurrentHead = CharIndex
            while CurrentHead < CharIndex + SkipStep:
                Character = SourceStr[CurrentHead]
                if True == LocalCharDic.has_key( Character ):
                    if 1 == LocalCharDic[Character]:
                        LocalCharDic.pop(Character)
                    else:
                        LocalCharDic[Character] -= 1
                CurrentHead += 1
            CurrentHead = CharIndex + PatternLen
            CharIndex += SkipStep
            CurrentTail = CharIndex + PatternLen
            if CurrentTail <= SourceLen:
                while CurrentHead < CurrentTail:
                    Character = SourceStr[CurrentHead]
                    if True == LocalCharDic.has_key( Character ):
                        LocalCharDic[Character] += 1
                    else:
                        LocalCharDic[Character] = 1
                    CurrentHead += 1
        """
        while CharIndex < Range:
            CurrentSlice = s[CharIndex:CharIndex+PatternLen]
            IsAnagrams = True
            Shift = [1]
            for Key in LocalCharDic:
                if False == PatternCharDic.has_key(Key):
                    IsAnagrams = False
                    Shift.append(CurrentSlice.rfind(Key))
                elif LocalCharDic[Key] > PatternCharDic[Key]:
                    Shift.append(CurrentSlice.find(Key))
                    IsAnagrams = False
                elif LocalCharDic[Key] < PatternCharDic[Key]:
                    Shift.append(CurrentSlice.rfind(Key))
                    IsAnagrams = False
            if True == IsAnagrams:
                RetList.append( CharIndex )
                Shift = PatternLen
            Skip = max(Shift)
            Adjuster = CharIndex+Skip
            Iter = CharIndex
            while Iter < Adjuster:
                Character = s[Iter]
                if True == LocalCharDic.has_key( Character ):
                    if 1 == LocalCharDic[Character]:
                        LocalCharDic.pop( Character )
                    else:
                        LocalCharDic[Character] -= 1
                Iter += 1
            
            CurrentTail = CharIndex + PatternLen
            Iter = CurrentTail
            CharIndex += Skip
            Adjuster = CurrentTail+Skip
            if Adjuster <= TargetLen:
                while Iter < Adjuster:
                    Character = s[Iter]
                    if True == LocalCharDic.has_key( Character ):
                        LocalCharDic[Character] += 1
                    else:
                        LocalCharDic[Character] = 1
                    Iter += 1
            else:
                break
        """
        return RetList