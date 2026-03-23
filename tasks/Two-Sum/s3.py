##
## Not working for this  case num = [1, 3, 4, 4, 2], target = 6
##


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


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

##  <------ :) ta dam!
nums = [1, 3, 4, 4, 2]
target = 6
output = [2, 4]


r = Solution().twoSum(nums, target)

print(f"The actual output {r}")
print(f"The expected output {output}")
print(f"Is correct answer : {output == r}")
