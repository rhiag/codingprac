'''
Count the unique origin airports
Find how many different origin airports exist?
https://platform.stratascratch.com/coding/9672-count-the-unique-origin-airports?python=1
'''
# Import your libraries
import pandas as pd

# Start writing code
us_flights.head()
distinct_flights=us_flights['origin'].unique()
flts = len(distinct_flights)
flts