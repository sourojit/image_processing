
# coding: utf-8

# In[1]:




# In[2]:




# In[43]:

import numpy as np
import matplotlib.pyplot as plt
import os


# In[4]:

cwd=os.getcwd()


# In[5]:




# In[6]:

image_dir=os.path.join(cwd,'image_series')


# In[7]:

image_dir


# In[14]:

files= [f for f in os.listdir(image_dir) if f.endswith('.jpg')]


# In[15]:

files


# In[16]:

redperimage=[]


# In[17]:

greperimage=[]


# In[18]:

for image in files:
    img=plt.imread(os.path.join(image_dir,image))
    reds=img[:,:,0]
    redperimage.append(np.sum(reds))
    greens=img[:,:,1]
    greperimage.append(np.sum(greens))


# In[19]:

redperimage=np.array(redperimage,dtype=float)
greperimage=np.array(greperimage,dtype=float)


# In[20]:

ratio=redperimage/greperimage


# In[38]:

plt.subplot(211)


# In[39]:

plt.plot(range(0,len(redperimage)),redperimage,'ro')
plt.plot(range(0,len(greperimage)),greperimage,'go')


# In[40]:

plt.subplot(212)


# In[41]:

plt.plot(range(0,len(ratio)),ratio,'ko')


# In[42]:

plt.show()


# In[ ]:



