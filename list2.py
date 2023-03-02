def remove_adjacent(nums):
    nums1 = list()
    nums1.append(nums[0])
    for item in nums:
        if item != nums1[-1]:
            nums1.append(item)
    return nums1

def linear_merge(list1, list2):
    iter1, iter2 = 0, 0
    finl = list()
    while (iter1 < len(list1)) & (iter2 < len(list2)):
        if list1[iter1] < list2[iter2]:
            finl.append(list1[iter1])
            iter1 += 1
        elif list1[iter1] == list2[iter2]:
            finl.append(list2[iter2])
            iter2 += 1
            iter1 += 1
        else:
            finl.append(list2[iter2])
            iter2 += 1

    while iter1 < len(list1):
        finl.append(list1[iter1])
        iter1 += 1
    while iter2 < len(list2):
        finl.append(list2[iter2])
        iter2 += 1
    return finl


print(linear_merge(['aa', 'xx', 'zz'],['bb', 'cc', 'zz']))
print(linear_merge(['aa', 'xx'],['bb', 'cc', 'zz']))
print(linear_merge(['aa', 'aa'],['bb', 'bb']))




