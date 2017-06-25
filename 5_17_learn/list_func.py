
nums = [1,3,2,5,6,4,8,7]
print("nums's length:")

#list 自身的方法
nums.append(9)
nums.remove(1)

print(nums.count(1))

print(nums)

# 排序 --默认递增
nums_sorted = sorted(nums)
print(nums_sorted)

# 反转
nums_reversed = list(reversed(nums_sorted))
print(nums_reversed)

#排序--递减
nums_sorted_desc = sorted(nums, reverse=True)
print(nums_sorted_desc)

# 删除元素
# nums.pop(index);
# nums.remove(element)


# len()是Python内置的函数
print(len(nums))

#使用map方法
nums_maped = list(map(lambda x:x+5,nums))
print(nums_maped)

#使用filter方法
nums_filtered = list(filter(lambda x : x %2 == 0,nums))
print(nums_filtered)

