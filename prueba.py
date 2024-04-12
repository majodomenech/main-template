import pandas as pd

# Create a list
data = ['John','Alice','Bob']

# Create a DataFrame from the list
df = pd.DataFrame(data, columns=['Name'])

print(df)