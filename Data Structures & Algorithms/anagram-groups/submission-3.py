class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prevMap = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            prevMap[tuple(count)].append(word)
        return list(prevMap.values())
            