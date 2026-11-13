class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        res = []
        for i in range(len(strs)):
            freq_array = [0] * 26
            for c in strs[i]:
                freq_array[(ord('a') - ord(c))] += 1
            mp[tuple(freq_array)].append(i)
        for value in mp.values():
            temp = []
            for v in value:
                temp.append(strs[v])
            res.append(temp)
        return res
        
