class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            newword = "".join(sorted(word))

            if newword not in groups:
                groups[newword] = []

            groups[newword].append(word)

        return list(groups.values())