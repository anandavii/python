import unittest
def twosum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return[i,j]  
            
if __name__ == "__main__":
    class TestTwoSum(unittest.TestCase):
        def test_case1(self):
            nums = [2, 7, 11, 15]
            target = 9
            result = twosum(nums, target)
            self.assertEqual(twosum(nums, target), [0, 1])
            print("Test case 1 passed. Result:", result)
    
        def test_case2(self):
            nums = [3, 2, 4]
            target = 6
            result = twosum(nums, target)
            self.assertEqual(twosum(nums, target), [1, 2])
            print("Test case 2 passed. Result:", result)

unittest.main()