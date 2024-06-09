# Two Sum Problem

[Leetcode Link for the Problem](https://leetcode.com/problems/two-sum/)

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Examples

### Example 1
**Input:** `nums = [2,7,11,15]`, `target = 9`  
**Output:** `[0, 1]`  
**Explanation:** Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

### Example 2
**Input:** `nums = [3,2,4]`, `target = 6`  
**Output:** `[1, 2]`  
**Explanation:** Because `nums[1] + nums[2] == 6`, we return `[1, 2]`.

### Example 3
**Input:** `nums = [3,3]`, `target = 6`  
**Output:** `[0, 1]`  
**Explanation:** Because `nums[0] + nums[1] == 6`, we return `[0, 1]`.

## Constraints
- Each input would have exactly one solution.
- You may not use the same element twice.
- The solution can be returned in any order.

## Testing
You can test the function with the provided examples or add more test cases to ensure its correctness:

```python
assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]
```

Feel free to modify the function or add additional comments for clarity as needed.