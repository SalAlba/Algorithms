class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []


##
nums = [3, 4, 5, 6, 3]
target = 7
output = [0, 1]

# ##
# nums = [5, 5]
# target = 10
# output = [0, 1]

# ##
# nums = [1, 3, 4, 2]
# target = 6
# output = [2, 3]

r = Solution().twoSum(nums, target)

print(f"Is correct answer : {output == r}")
