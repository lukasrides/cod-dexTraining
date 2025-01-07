"""Write a function two_sum(nums: list[int], target: int) -> list[int] that finds two numbers in the nums list that add up to the target. 
Return their indices as a list [index1, index2]."""

def twoSum(nums,target):
    for num1 in nums:
        for num2 in nums:
            if nums.index(num1)==nums.index(num2): 
                continue
            elif num1+num2 == target:
                return [nums.index(num1),nums.index(num2)]
            
def twoSumOpt(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):  # Start from i + 1 to avoid duplicate pairs
            if nums[i] + nums[j] == target:
                return [i, j]  # Return the indices directly

# Test cases
print(twoSum([2, 7, 11, 15], 9))       # Output: [0, 1]
print(twoSum([3, 2, 4], 6))            # Output: [1, 2]
print(twoSum([3, 3], 6))               # Output: [0, 1]
print(twoSum([1, 5, 4, 6], 10))        # Output: [1, 3]



print(twoSumOpt([2, 7, 11, 15], 9))       # Output: [0, 1] (2 + 7 = 9)
print(twoSumOpt([3, 2, 4], 6))            # Output: [1, 2] (2 + 4 = 6)
print(twoSumOpt([3, 3], 6))               # Output: [0, 1] (3 + 3 = 6)
print(twoSumOpt([1, 5, 4, 6], 10))        # Output: [1, 3] (5 + 6 = 10)

    