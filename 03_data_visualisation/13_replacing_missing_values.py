# importing pandas and numpy
import pandas as pd
import numpy as np

# dictionary of lists
dict = {
    "First Score": [100, 90, np.nan, 95],
    "Second Score": [30, 45, 56, np.nan],
    "Third Score": [np.nan, 40, 80, 98],
}

# creating a dataframe from dictionary
df = pd.DataFrame(dict)

# will replace  Nan value in dataframe with value -1
print(df.replace(to_replace=np.nan, value=-1))
