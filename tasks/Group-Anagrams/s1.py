class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _hash = {}

        for s in strs:
            hashSet = set()
            frequency = {}

            for c in sorted(s):
                hashSet.add(c)
                frequency[c] = frequency.get(c, 0) + 1

            k = str(frequency)

            if k in _hash:
                _hash[k] = _hash[k] + [s]
            else:
                _hash[k] = [s]

        return list(_hash.values())


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
• Memory: 8.7 MB
• Time: 52ms
• Submitted at: 04/02/2026 18:22


Time complexity : O (n ⋅ m log m)
Space complexity : O(n⋅m)

"""
