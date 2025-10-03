'''Task 1 – DataFrame from Dictionary of Lists (Basic)

Problem: Create a DataFrame of products.
Data:

data = {
    'Product': ['Laptop', 'Tablet', 'Mobile'],
    'Price': [60000, 30000, 15000],
    'Brand': ['Dell', 'Samsung', 'Redmi']
}
Instructions:
Create a DataFrame.
Print the DataFrame.
Add custom index labels: ['p1','p2','p3'].

Expected Output:

   Product  Price   Brand
p1  Laptop  60000    Dell
p2  Tablet  30000 Samsung
p3  Mobile  15000   Redmi'''

import pandas as pd
d={
     'Product': ['Laptop', 'Tablet', 'Mobile'],
    'Price': [60000, 30000, 15000],
    'Brand': ['Dell', 'Samsung', 'Redmi']
}
data=pd.DataFrame(d,index=['p1','p2','p3'])
print(data)
