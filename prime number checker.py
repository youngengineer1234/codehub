#!/usr/bin/env python
# coding: utf-8

# In[2]:


num = int(input("Enter a number: "))
flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
            
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")


# In[ ]:




