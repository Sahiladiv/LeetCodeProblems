class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums2 = list()
        for i in nums:
            nums2.append(i)
        
        for i in nums:
            diff = target - i
            first_indx = nums.index(i)
            print(i, first_indx)
            nums[first_indx] = None
            nums2.remove(i)
            if diff in nums2:
                second_indx = nums.index(diff)
                break
        return [first_indx, second_indx]
