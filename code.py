import pandas as pd
#Importing data from csv
inventory = pd.read_csv("inventory.csv")
#Inspecting first 10 elements in the file
inventory.head(10)
# selecting 10 rows into staten_island
staten_island=inventory[inventory["location"]=="Staten Island"]
print(staten_island)
# Customer request of products sold in Staten Island
product_request = staten_island.product_description
print(product_request)
# Add a column in_stock
in_stock= lambda row: "True" if row["quantity"]>0 else "False"
inventory["in_stock"]=inventory.apply(in_stock, axis = 1)
print(inventory.in_stock)
