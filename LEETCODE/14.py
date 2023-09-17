# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# strs = ["flower", "flow", "flight"]
strs = ["ab", "a"]
set1 = set()
string = ""
num = min([len(word) for word in strs])  # for string index out of range
for i in range(0, num):
    for word in strs:
        set1.add(word[i])
    print(set1)
    if len(set1) == 1:
        string += set1.pop()
    else:
        break
print(string)
