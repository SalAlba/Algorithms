# Two Sum

**Difficulty:** Easy

## Problem Description

Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

## Function Description

Complete the function `twoSum` which takes the following parameters:

- `nums`: an array of integers
- `target`: an integer representing the target sum

**Returns:**
- An array of two integers representing the indices of the two numbers that add up to the target

## Input Format

- First line contains an array of integers `nums`
- Second line contains an integer `target`

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists

## Sample Input 0

```
nums = [2, 7, 11, 15]
target = 9
```

## Sample Output 0

```
[0, 1]
```

## Explanation 0

Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

---

## Sample Input 1

```
nums = [3, 2, 4]
target = 6
```

## Sample Output 1

```
[1, 2]
```

## Explanation 1

Because `nums[1] + nums[2] == 6`, we return `[1, 2]`.

---

## Sample Input 2

```
nums = [3, 3]
target = 6
```

## Sample Output 2

```
[0, 1]
```

## Explanation 2

Because `nums[0] + nums[1] == 6`, we return `[0, 1]`.

---

## Follow-up

Can you come up with an algorithm that is less than O(n²) time complexity?
