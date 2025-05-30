# importing pandas and numpy
import pandas as pd
import numpy as np

# dictionary of lists
dict = {
    "First Score": [100, 90, np.nan, 95],
    "Second Score": [30, 45, 56, np.nan],
    "Third Score": [np.nan, 40, 80, 98],
}

# creating a dataframe from list
df = pd.DataFrame(dict)

# using isnull() function
print(df.isnull())

# using notnull() function
print(df.notnull())
