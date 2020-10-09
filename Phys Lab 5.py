#!/usr/bin/env python
# coding: utf-8

# In[10]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Calculating Inital and final momentums of the two carts (inElastic)

vi_b=0 #initial velocity for still cart (b)
vi_b_uncertainty=0.00124 #uncertainty of cart b
vi_a=0.4194 #initial velocity for still cart a
vi_a_uncertainty=0.01832

vf_b=0.1835 #final velocity for b
vf_b_uncertainty=0.007818 #uncertainty of the final velocity
vf_a=0.1816 #final velocity for a
vf_a_uncertainty=0.005474 #uncertainty of the final velocity

m_cart_a=0.5004 #mass of the cart
m_cart_a_uncertainty=0.0001 #uncertainty of the mass of the cart
m_cart_b=0.4944 #mass of the cart
m_cart_b_uncertainty=0.0001 #uncertainty of the mass of the cart

Pi=vi_b*m_cart_b+vi_a*m_cart_a #calculating the initial momentum
Pi_uncertainty= Pi*((vi_a_uncertainty/vi_a)+(m_cart_a_uncertainty/m_cart_a)) #calculating the uncertainty of initial momentum

Pf=vf_b*m_cart_b+vf_a*m_cart_a #calculating the final momentum for the slowest trail
Pf_uncertainty= Pf*((vf_b_uncertainty/vf_b)+(m_cart_b_uncertainty/m_cart_b)+(vf_a_uncertainty/vf_b)+(m_cart_a_uncertainty/m_cart_a))
#calculating the uncertainty of final momentum

print("Results of inElastic Trial") #Title text

#Make sure the initial momentum and its error show up in the outputs with the proper units
print ("Pi = ", Pi, "(kg*m)/s")
print ("Pi Uncertainty = ", Pi_uncertainty, "(kg*m)/s")

#Make sure the final momentum and its error show up in the outputs with the proper units
print ("Pf = ", Pf, "(kg*m)/s")
print ("Pf Uncertainty = ", Pf_uncertainty, "(kg*m)/s")


# In[ ]:


# In[1]:


print "help"


# In[2]:


print("help")

