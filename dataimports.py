import pandas as pd

# Home Ownership Data

homeownershipbystate = pd.read_csv("data/yearlyhousingdatabystate.txt", delim_whitespace=True)

print(homeownershipbystate.head())
