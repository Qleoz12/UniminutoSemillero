def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    swappedTimes=0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                swappedTimes+=1
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True
    return swappedTimes