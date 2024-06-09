# Count Digits Problem

[GFG Link for the Problem](https://www.geeksforgeeks.org/problems/count-digits5716/1)

## Problem Statement
Given a number `N`, count the number of digits in `N` which evenly divide `N`.

**Note:** "Evenly divides" means that `N` is divisible by a digit if it leaves a remainder of 0 when divided by that digit.

## Examples

### Example 1
**Input:**  
`N = 12`  
**Output:**  
`2`  
**Explanation:**  
1 and 2 both divide 12 evenly.

### Example 2
**Input:**  
`N = 23`  
**Output:**  
`0`  
**Explanation:**  
Neither 2 nor 3 divide 23 evenly.

## Your Task
You don't need to read input or print anything. Your task is to complete the function `evenlyDivides()` which takes an integer `N` as input parameters and returns an integer representing the total number of digits in `N` which divide `N` evenly.

## Expected Complexity
- **Time Complexity:** O(log N)
- **Space Complexity:** O(1)

## Constraints
- \(1 \leq N \leq 10^5\)

## Testing
You can test the function with the provided examples or add more test cases to ensure its correctness:

```python
assert evenlyDivides(12) == 2
assert evenlyDivides(23) == 0
```

Feel free to modify the function or add additional comments for clarity as needed.