# Swap first and last

nums = [1,2,3,4,5]
temp = nums[0]

print(f"Original list is: {nums}")

nums[0] = nums[-1]
nums[-1] = temp

print(f"New list is: {nums}")