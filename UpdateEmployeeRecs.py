'''
Finding Updated Records (https://platform.stratascratch.com/coding/10299-finding-updated-records?python=1)
We have a table with employees and their salaries, however, some of the records are old and 
contain outdated salary information. Find the current salary of each employee assuming that 
salaries increase each year. Output their id, first name, last name, department ID, and current salary.
Order your list by employee ID in ascending order.

ms_employee_salary  
id                   int64
first_name           object
last_name            object
salary               int64
department_id        int64

'''

import pandas as pd

# Start writing code
ms_employee_salary.head()
print(ms_employee_salary.shape)

#finding max salary
max_sal =ms_employee_salary.groupby('id').agg({'salary':'max'})
max_sal
print("Max Sal:",max_sal.shape)

#dropping duplicates
newdf = ms_employee_salary.drop_duplicates(
    subset = ['id', 'first_name','last_name','department_id'],
  keep = 'last').reset_index(drop = True)
print("New DF:",newdf.shape)

# assigning the max salary
newdf['salary'] = max_sal

newdf.head()