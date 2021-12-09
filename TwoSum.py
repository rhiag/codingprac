'''

'''

def two_sum(nums, target):
    # Your code here
    for i in range(len(nums)):
        sum= nums[i] + nums[i+1]
        if sum == target:
            return [i,i+1]