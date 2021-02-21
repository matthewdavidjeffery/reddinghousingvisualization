import pandas as pd

# Home Ownership Data, from US Census B

df = pd.read_csv("data/yearlyhousingdatabystate.txt", delim_whitespace=True)

dftx = pd.DataFrame(columns=['state', 'year', 'percent'])

#get column header list
yearlist = list(df.keys())
print(yearlist)
#take state column out
del yearlist[0]
print(yearlist)

#get each state
statelist = df['STATE'].tolist()
print(statelist)

# with each state, get all year data and add entries for each
entrylist = [['STATE', 'YEAR', 'PERCENT']]
for state in statelist:

    percforstate = df.query("STATE == '" + state + "'")

    for year in yearlist:
        percforyear = percforstate[year].tolist()[0]
        entrylist.append([state, year, percforyear])

entriesbystate = pd.DataFrame(data=entrylist)
entriesbystate.to_csv("data/housingdataconditioned.csv")
