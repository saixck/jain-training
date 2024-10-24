#!/usr/bin/env python
# coding: utf-8

#  Python code to calculate the total cost of Anil's food order, including a 10% discount if the order exceeds Rs. 500:
# 

# In[4]:


menu = {
    1: {'item': 'Pizza', 'price': 200},
    2: {'item': 'Burger', 'price': 100},
    3: {'item': 'Dosa', 'price': 150},
    4: {'item': 'Briyani', 'price': 250},
    5: {'item': 'Chicken rice', 'price': 200}
}

#input for choice and quantity
choice = int(input("Enter your choice (1-5): "))
quantity = int(input("Enter quantity: "))

# Calculating the total cost before discount
item_price = menu[choice]['price']
total_cost = item_price * quantity

# Applying discount if the total cost exceeds Rs. 500
if total_cost > 500:
    discount = total_cost * 0.10  # 10% discount
else:
    discount = 0

# Calculating the final cost after discount
final_cost = total_cost - discount

# Display the results
print(f"Total cost before discount: Rs. {total_cost}")
print(f"Discount applied: Rs. {discount}")
print(f"Total cost after discount: Rs. {final_cost}")


# In[ ]:




