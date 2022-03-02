import numpy as np
import matplotlib.pyplot as plt

sales_data = {'Kolkata':20, 'Mumbai':15, 'Hyderabad':30, 'Bangalore':35, 'Delhi':10}
locations = list(sales_data.keys())
items = list(sales_data.values())

fig = plt.figure(figsize = (10, 5))

plt.bar(locations, items, color ='maroon', width = 0.5)

plt.xlabel("Location")
plt.ylabel("Item count")
plt.title("Item sales in different locations")
plt.show()
