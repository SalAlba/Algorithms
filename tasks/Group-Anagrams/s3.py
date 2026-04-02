from collections import defaultdict


##
## The best !
##
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            _s = "".join(sorted(2))
            res[_s].append(s)

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

Time & Space Complexity
Time complexity:  O(m∗nlogn)
Space complexity:  O(m∗n)

Where  m is the number of strings and n is the length of the longest string.

"""
