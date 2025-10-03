'''Task 6 – Comparison
Problem:
Create employee DataFrames in two ways 
with fields Name, Age, Dept for ['E1','E2','E3']:

Dict of Lists
Dict of Dicts (employee id as index)

Output:
📌 Dict of Lists → Columns first
📌 Dict of Dicts → Row indexes first'''

import pandas as pd
data_list={
'Name':['E1','E2','E3'],
'Age':[23,21,22],
"Dept": ["HR", "IT", "Finance"]
}
print("Dict of Lists DataFrame:\n",pd.DataFrame(data_list),'\n')
data_dicts={
    'E1':{'Name':'E1','Age':23,'Dept':'HR'},
    'E2':{'Name':'E2','Age':21,'Dept':'IT'},
    'E3':{'Name':'E3','Age':22,'Dept':'Finance'}
    }
print("Dict of Dicts DataFrame:\n",pd.DataFrame(data_dicts))