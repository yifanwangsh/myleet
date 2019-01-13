def search(nums, target):
    def divide(left_index,right_index,target):
        if nums[left_index] == target:
            return left_index
        elif nums[right_index] == target:
            return right_index
        elif nums[left_index] == nums[right_index]:
            return -1
        # elif nums[left_index] > nums[right_index]:
        #     if target > nums[left_index]:
        #        return -1
        #     elif target < nums[left_index]:
        #         divide(right_index,
        elif target > nums[left_index] 