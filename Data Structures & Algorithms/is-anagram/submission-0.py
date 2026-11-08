class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictionary1 = {}
        dictionary2 = {}
        for i in range(len(s)):
            if s[i] not in dictionary1:
                dictionary1[s[i]] = 1
            else:
                dictionary1[s[i]] += 1
            if t[i] not in dictionary2:
                dictionary2[t[i]] = 1
            else:
                dictionary2[t[i]] += 1
        return dictionary1 == dictionary2