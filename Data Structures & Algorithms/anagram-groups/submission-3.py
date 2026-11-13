class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for s in strs:
            freq_array = [0] * 26
            for c in s:
                freq_array[(ord('a') - ord(c))] += 1
            mp[tuple(freq_array)].append(s)
        return list(mp.values())
        
