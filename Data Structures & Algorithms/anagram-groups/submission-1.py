class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_counter = defaultdict(list)
        for s in strs:
            alphabet_list = [0] * 26
            for c in s:
                alphabet_list[ord(c) - ord('a')] += 1
            string_counter[tuple(alphabet_list)].append(s)
        return list(string_counter.values())
