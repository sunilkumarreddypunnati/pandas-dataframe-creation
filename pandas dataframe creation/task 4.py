'''Task 4 – Dict of Dicts with Missing Values
Problem:
Create a DataFrame from

data = {
    'Age': {'a': 20, 'b': 25},
    'City': {'a': 'Delhi', 'b': 'Mumbai', 'c': 'Chennai'}
}

Output:

    Age     City
a  20.0    Delhi
b  25.0   Mumbai
c   NaN  Chennai
'''

import pandas as pd
data = {
    'Age': {'a': 20, 'b': 25},
    'City': {'a': 'Delhi', 'b': 'Mumbai', 'c': 'Chennai'}
}
print(pd.DataFrame(data))
