class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        Prefix = strs[0]
        Length = len(Prefix)

        for i in range(1, len(strs)):
            for j in range(min(len(strs[i]), Length)):
                #print(i, j)
                if strs[i][j] != Prefix[j]:
                    Prefix = Prefix[:j]      
                    Length = len(Prefix)
                    #print(Prefix, Length)
                    break
            if len(strs[i]) <= Length:
                Prefix = strs[i]
                Length = len(Prefix)
        return Prefix


strs0 = ["flower","flow","flight"]
strs1 = ["dog","racecar","car"]
sol = Solution()
print(sol.longestCommonPrefix(strs0))
print(sol.longestCommonPrefix(strs1))


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        '''
        min, max string list compare alphabetically
        '''
        Min = min(strs)
        Max = max(strs)
        #print(Min, Max)

        for i in range(len(Min)):
            if Min[i] != Max[i]:
                return Min[:i]
        return Min


strs0 = ["flower","flow","flight"]
strs1 = ["dog","racecar","car"]
sol = Solution()
print(sol.longestCommonPrefix(strs0))
print(sol.longestCommonPrefix(strs1))
