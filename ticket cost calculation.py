#!/usr/bin/env python
# coding: utf-8

# In[43]:


age = int(input("Enter your age: "))
num_tickets = int(input("Enter number of tickets: "))

# Set price based on age
if age <= 12:
    price = 20
elif age >= 60:
    price = 30
else:
    price = 50

# Calculate total cost
total_cost = price * num_tickets

# Display the result
print(f"Total cost for {num_tickets} tickets: {total_cost}")

