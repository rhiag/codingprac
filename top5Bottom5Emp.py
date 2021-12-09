'''
https://platform.stratascratch.com/coding/9979-find-the-top-5-highest-paid-and-top-5-least-paid-employees-in-2012?python=1

Find the top 5 highest paid and top 5 least paid employees in 2012
Find the top 5 highest paid and top 5 least paid employees in 2012.
Output the employee name along with the corresponding total pay with benefits.
Sort records based on the total payment with benefits in ascending order.
DataFrame: sf_public_salaries
Expected Output Type: pandas.DataFrame
'''

import pandas as pd
# Start writing code
sf_public_salaries.head()
sf_public_salaries = sf_public_salaries.sort_values(by='totalpaybenefits')
least_paid = sf_public_salaries.head()
highest_paid = sf_public_salaries.tail()
least = least_paid[['employeename','totalpaybenefits']]
highest = highest_paid[['employeename','totalpaybenefits']]
top_bottom = [highest,least]
top5 = pd.concat(top_bottom).sort_values(by='totalpaybenefits')
top5