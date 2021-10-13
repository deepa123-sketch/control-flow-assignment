#!/usr/bin/env python
# coding: utf-8

# ---
# ---
# 
# <center><h1>📍 📍 Assignment: Control Flow 📍 📍</h1></center>
# 
# ---
# 
# ***Take 3 inputs from the user***
# 
#  -  **What is your Age?**    (Answer will be an Intger value)
#  -  **Do you eat Pizza?**    (Yes/No)
#  -  **Do you do exercise?**  (Yes/No)
# 
# #### `Write the if else condition for the given flow chart.`
# 
# ![](image/control-flow.png)

# In[58]:


# take input from the user: age
age = int(input("What is your Age? "))


# In[59]:


pizza = input("Do you eat Pizza? ")


# In[60]:


exercise = input("Do you do exercise? ")


# In[61]:


if age<30:
    if pizza=="yes":
        if exercise=="yes":
            print("You are fit")
        else:
            print("You are unfit")          
        
    else:
        print("You are fit")
else:
    if pizza=="yes":
        print("You are unfit")
        if exercise=="Yes":
            print("you are fit")
        else:
            print("You are not fit")
        
    else:
        print("You are fit")
     


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




