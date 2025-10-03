'''Task 3 – DataFrame from Dictionary of Dictionaries (Basic)
Problem: Create a DataFrame of subject marks.

Data:

data = {
    'Maths': {'s1': 90, 's2': 85, 's3': 88},
    'Science': {'s1': 95, 's2': 80, 's3': 89}
}
Instructions:

Create a DataFrame.
Print the DataFrame.
Observe how row indexes are created.

Expected Output:

    Maths  Science
s1     90       95
s2     85       80
s3     88       89'''

import pandas as pd
data = {
    'Maths': {'s1': 90, 's2': 85, 's3': 88},
    'Science': {'s1': 95, 's2': 80, 's3': 89}
}
df=pd.DataFrame(data)
print(df)