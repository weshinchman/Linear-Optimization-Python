#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Wesley Hinchman EVE 310
#Lecture #23: Linear Optimization with Python

#Import packages
import numpy as np
from scipy.optimize import linprog


# In[17]:


#Establish sample arrays and define
c = np.array([35,35])
A_ineq = np.array([(0.2,0.3),(-0.05,-0.15)])
b_ineq = np.array([6000,-1500])
bnd = np.array([(0,10000),(0,20000)])
res = linprog(c, A_ub= A_ineq, b_ub=b_ineq, bounds=bnd)


# In[18]:


#Print results
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
print('Succes = {:}'.format(res.success))
print('Status = {:}'.format(res.status))
print('Optimal Value = {: .2f}'.format(res.fun))
print('Optimal Solution ={:}'.format(res.x))
print('Slack = {:}'.format(res.slack))


# In[ ]:




