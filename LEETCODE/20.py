# Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

#  def rw(s):
#     b_list = ["()", "[]", "{}"]
#     divided_s = []
#     if len(s) % 2 != 0:
#         return False
#     else:  # divide s by step 2
#         for i in range(0, len(s), 2):
#             chunk = s[i:i + 2]
#             divided_s.append(chunk)
#         for str in divided_s:
#             if str not in b_list:
#                 return False
#         return True


# "{[]}"
# this should be true??? 
# !!!If I can pop all the () or [] or {}!
s = "()"
# s = "{[]}"  # made it!


def rw(s):
    b_list = ["()", "[]", "{}"]
    len_s = len(s)
    if len_s % 2 != 0:
        return False
    else:
        while len(s) != 0:
            for i in b_list:
                print(f"i:{i}")
                if i in s:
                    s = s.replace(i, "")
                    print(f"s:{s}")
            tmp_s = len(s)
            print(tmp_s)
            if tmp_s == len_s:  # popped nothing
                return False
            else:
                len_s = len(s)
        return True


bool = rw(s)
print(bool)
# def rw(s):
#     for key, b in enumerate(right_list):
#         if b in s:
#             if left_list[key] not in s:
#                 return False
#     for key, b in enumerate(left_list):
#         if b in s:
#             if right_list[key] == s[key + 1]:  # out of range
#                 return True
#             else:
#                 return False
# # must be close!!!



