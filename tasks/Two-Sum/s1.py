class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _ht = {}
        for i, n in enumerate(nums):
            if n in _ht:
                _ht[n] = _ht[n] + [i]
            else:
                _ht[n] = [i]

        for i in _ht.keys():
            wanted = target - i
            if wanted in _ht:
                i = _ht[i][0]
                j = _ht[wanted][0]

                if i == j:
                    if len(_ht[wanted]) < 2:
                        continue
                    j = _ht[wanted][1]

                if i > j:
                    return [j, i]
                return [i, j]

        return []


##
nums = [3, 4, 5, 6, 3]
target = 7
output = [0, 1]

##
nums = [5, 5]
target = 10
output = [0, 1]

##
nums = [1, 3, 4, 2]
target = 6
output = [2, 3]

r = Solution().twoSum(nums, target)

print(f"The actual output {r}")
print(f"The expected output {output}")
print(f"Is correct answer : {output == r}")


"""
Time spent : 19:20
---
Runtime : 27ms | Beats 100.00%
Memory : 8.1 MB | Beats 87.08%
"""

"""
Time Complexity: O(n)
- First pass: Build hash table mapping numbers to their indices - O(n)
- Second pass: Iterate through hash table keys to find complement - O(n)
- Hash table lookups are O(1) average case
- Total: O(n) where n is the length of nums array

Space Complexity: O(n)
- Hash table stores all elements and their indices in worst case
"""
