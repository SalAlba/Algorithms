from collections import defaultdict


##
## The best !
##
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())


##
strs = ["act", "pots", "tops", "cat", "stop", "hat"]
wanted_output = [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]

# strs = [
#     "pots",
#     "tops",
#     "stop",
# ]
# wanted_output = [["stop", "pots", "tops"]]

strs = ["x"]
wanted_output = [["x"]]

strs = [""]
wanted_output = [[""]]

strs = ["ddddddddddg", "dgggggggggg"]
wanted_output = [["ddddddddddg"], ["dgggggggggg"]]


real_output = Solution().groupAnagrams(strs)

print(f"- Input: {strs}")
print(f"- [*] Real Output: {real_output}")
print(f"- Wanted Output: {wanted_output}")
# print(f"- Success: {real_output == wanted_output}")  ## in any order :P


"""

Runtime : 50ms
Memory : 8.5 MB


Time complexity:  O(n⋅k)
Space complexity: O(n⋅k)

n is the number of strings in the input list
k is the maximum length of a string in the input list
"""
