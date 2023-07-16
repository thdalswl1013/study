"""
input string : information-technology
input number : 12
"""

arr_str = input('input String :').split('-') # arr_str[0] : infomation
                                             # arr_str[1] : technology

arr_len = int(input('input number : ')) 
arr_val = list(range(0,arr_len,2)) # 0,2,4,6,8,10
arr_val.remove(4) # 0,2,6,8,10
print(arr_str[1].find('i') + arr_val[2]) # (-1) +6