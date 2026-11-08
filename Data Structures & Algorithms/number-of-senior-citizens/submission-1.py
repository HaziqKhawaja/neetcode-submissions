class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for s in details:
            if int(s[11]) > 6 or (int(s[11]) == 6 and int(s[12]) > 0):
                count += 1
        return count 