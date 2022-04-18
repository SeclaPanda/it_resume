class Answer:
    def minOperations(self, nums):
        count = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                count += (prev + 1 - nums[i])
                prev += 1
            else:
                prev = nums[i]
        return count
nums = [1, 5, 2, 4, 1]
print(Answer.minOperations(Answer, nums))