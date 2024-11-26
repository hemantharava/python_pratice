#!/usr/bin/env python
# coding: utf-8

# In[1]:


a='hemanth'
print(len(a))


# In[13]:


#to find the middle element
a=[12,3,4,5,7,99,100,111]
b=len(a)//2
if b%2==1:
    print(a[b])
else:
    print(a[b-1],a[b])


# In[14]:


a='hemanth'
print(isinstance(a,str))


# In[15]:


a=[1,2]
print(isinstance(a,str))


# In[16]:


#element is float or not
a=16.5
print(isinstance(a,float))


# In[19]:


#list is empty or not
a=[]
b=len(a)
print(b==0)


# In[20]:


#list is empty or not
a=[1,2]
b=len(a)
print(b==0)


# In[27]:


#program to check the data is number or special character
a=16.2
if isinstance(a,(int,float)):
    print('Number')
elif isinstance(a, str) and not a.isalnum():
    print("Special Character")
else:
    print("Unknown")


# In[29]:


#positive or negative
a=-2
if a>=1:
    print("positive")
else:
    print("negative")


# In[34]:


#program to check smallest number in user input
a=list(map(int,input().split()))
print(a)
b=min(a)
print(b)


# In[32]:


def find_smallest_number():
    # Prompt the user to enter numbers separated by spaces
    user_input = input("Enter numbers separated by spaces: ")
    
    # Convert the input string to a list of numbers
    numbers = list(map(float, user_input.split()))
    
    # Find the smallest number in the list
    smallest_number = min(numbers)
    
    # Print the smallest number
    print(f"The smallest number is: {smallest_number}")

# Example usage:
find_smallest_number()


# In[36]:


#program to check tuple is empty or not
a=(1,)
print(len(a)==0)


# In[37]:


# program to check number is divisible by 5 and 8
a=40
if a%5==0 and a%8==0:
    print('divisible')
else:
    print('not divisible')


# In[39]:


a=int(input("enter the marks"))
if a>90:
    print("A")
elif a>80:
    print("B")
elif a>70:
    print("c")
else:
    print('D')


# In[ ]:





# In[ ]:





# In[52]:


b=10%5
print(b)


# In[79]:


#armstrong number
a=152
b=str(a)
c=len(b)
sum=0
for i in b:
    sum=sum+int(i)**c
if sum==a:
    print('AS')
else:
    print('Not')


# In[83]:


#prime or not
n = 10
if n < 2:
    print(f"{n} is not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print('false')
            break
    else:
        print('true')


# In[86]:


#factorial of a number
a=5
b=1
for i in range(1,a+1):
    b=b*i
print(b)


# In[ ]:





# In[ ]:





# In[ ]:




