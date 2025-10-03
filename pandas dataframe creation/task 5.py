'''Task 5 – Custom Index & Column Order
Problem:
Using Task 1 data, create a DataFrame with
 index ['item1','item2','item3'] and 
 order columns as ['Brand','Product','Price'].

Output:

        Brand Product  Price
item1    Dell  Laptop  60000
item2 Samsung  Tablet  30000
item3   Redmi  Mobile  15000'''

import pandas as pd
d={
     'Product': ['Laptop', 'Tablet', 'Mobile'],
    'Price': [60000, 30000, 15000],
    'Brand': ['Dell', 'Samsung', 'Redmi']
    }
data=pd.DataFrame(d,index=['item1','item2','item3'],
                  columns=('Brand', 'Product' ,'Price'))
print(data)
