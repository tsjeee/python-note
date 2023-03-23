#!/usr/bin/env python
# coding: utf-8

# # 列表

# In[4]:


l = []
print(type(l))


# In[3]:


l=list()
print(type(l))


# In[9]:


l=[l,"l",l.]
print(type(l[0]))
print(type(l[1]))
print(type(l[2]))
print(type(1[3]))
print(type(l[0:2]))


# In[7]:


l=list(range(0,25))
print(l)


# In[10]:


l=list("python")
print(l)


# In[12]:


# append 末尾添加元素
l=[]
s=list(range(0,12))

for i in s:
    m=i**2
    l.append(m)
print(l)


# In[15]:


s=list(range(0,12))
def f(x):
    return x**2
l=map(f,s)
print(list(l))


# In[16]:


l=list(map(lambda x:x**2,range(0,12)))
print(l)


# In[17]:


#列表的组合
l=list(range(0,5))
s=list(range(5,9))

m=l[0:2]+s[0:2]
print(m)


# In[18]:


#列表删除数据-A删除指定值
l=[0,1,2,3,4,5,6,8,9,10,11,7]
print(l)
print(l.remove(7))
print(l)


# In[19]:


#列表删除数据

l=[0,1,2,3,4,5,6,8,9,10,11,7]
print(l)
print(l.pop(7))    #给定index参数是，删除指定位置的值，没有参数时末位删除
print(l)


# In[20]:


l=[0,1,2,3,4,5,6,8,9,10,11,7]
s=enumerate(l)
print(list(s))


# In[21]:


l=[0,1,2,3,4,5,6,8,9,10,11,7]
l.reverse()
print(l)


# In[30]:


l=[0,1,2,3,4,5,6]
l[l]=3
l[3:]=[6,6,6,6]
print(l)


# In[ ]:


# 列表是一个组合数据，里面可以存任何数据，列表里面的值可以增删改查，元组数据不可以修改


# In[ ]:




