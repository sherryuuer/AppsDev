nums = [1, 1, 2]
# [1, 2, 3, 4]
# print(len(nums))

new_list = []
while len(nums) != 0:
    new_nums = []
    n = nums[0]
    new_list.append(n)
    for x in nums:
        if x != n:
            new_nums.append(x)
    nums = new_nums
print(len(new_list))

# little g
nums = [1, 1, 3, 2, 3, 3, 3, 4, 4]
new_list = []

# 遍历有序列表
for i in range(len(nums)):
    # 如果当前元素与前一个元素不相等，将其添加到新列表中
    if i == 0 or nums[i] != nums[i - 1]:
        new_list.append(nums[i])

# 输出删除重复项后的列表
print(new_list)
print(len(new_list))

# PS C:\Users\sherr\Desktop\SallyFolder> & C:/Users/sherr/AppData/Local/Programs/Python/Python311/python.exe c:/Users/sherr/Desktop/SallyFolder/LEETCODE/26.py
# 1
# 1
# 2
# [2]
# [2]
# 2
# []
# [1, 2]
# PS C:\Users\sherr\Desktop\SallyFolder> & C:/Users/sherr/AppData/Local/Programs/Python/Python311/python.exe c:/Users/sherr/Desktop/SallyFolder/LEETCODE/26.py
# [1, 2]
# PS C:\Users\sherr\Desktop\SallyFolder> & C:/Users/sherr/AppData/Local/Programs/Python/Python311/python.exe c:/Users/sherr/Desktop/SallyFolder/LEETCODE/26.py
# 2

# leetcode
# [1, 1]
