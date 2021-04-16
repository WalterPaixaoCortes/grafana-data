import datadotworld as dw

ds = dw.load_dataset('jonloyens/intermediate-data-world', auto_update=True)
shootings_df = ds.dataframes['fatal-police-shootings-data']
