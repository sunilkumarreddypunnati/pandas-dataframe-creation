'''Task 2 – Dictionary of Lists with Mixed Data Types
Problem: Create a DataFrame for student results.
Data:
data = {
    'Student': ['Sunil', 'Ravi', 'Anu', 'Kiran'],
    'Score': [85.5, 90, 78, 88],
    'Passed': [True, True, False, True]
}
Instructions:
Create the DataFrame.
Display the DataFrame.
Print data types using .dtypes.
Expected Output:
 Student  Score  Passed
0   Sunil   85.5   True
1    Ravi   90.0   True
2     Anu   78.0  False
3   Kiran   88.0   True

Student     object
Score      float64
Passed        bool
dtype: object'''

import pandas as pd
data = {
    'Student': ['Sunil', 'Ravi', 'Anu', 'Kiran'],
    'Score': [85.5, 90, 78, 88],
    'Passed': [True, True, False, True]
}
df=pd.DataFrame(data)
print(df,'\n')
print(df.dtypes)