def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:        
    merged_nums = nums1 + nums2
    merged_nums.sort()

    num_size = len(merged_nums)

    if num_size == 1:
        return merged_nums[0]

    if num_size % 2 == 1:
        middle = int((num_size / 2) - 0.5)
        return merged_nums[middle]

    if num_size % 2 == 0:
        left = int((num_size / 2) - 1)
        right = int((num_size / 2))
        return (merged_nums[left] + merged_nums[right]) / 2

    return merged_nums
