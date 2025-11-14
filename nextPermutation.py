class Solution:
  def nextPermutation(self, nums: list[int]) -> None:
    def reverse(arr, start):
        end = len(arr) - 1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    n = len(nums)
    if n < 2:
        return

    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i < 0:
        reverse(nums, 0)
        return
    
    j = n - 1
    while j > i and nums[j] <= nums[i]:
        j -= 1
    
    nums[i], nums[j] = nums[j], nums[i]
    
    reverse(nums, i + 1)