#!/usr/bin/env python
# coding: utf-8

# Python code to move all the empty chocolate packets (0) to the end of the array:
# 
# 

# In[4]:


def move_zeros_to_end(arr):
    count = 0
    result = []

    for num in arr:
        if num != 0:
            result.append(num)  
        else:
            count += 1  
    result.extend([0] * count)
    return result

arr = [4, 5, 0, 1, 9, 0, 5, 0]
N = len(arr)
new_arr = move_zeros_to_end(arr)
print("Array after moving zeros to the end:", new_arr)



# In[ ]:




