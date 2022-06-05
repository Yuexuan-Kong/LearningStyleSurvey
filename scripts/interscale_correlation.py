import pandas as pd
import numpy as np
from read_data import read_data
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import pandas as pd

def calculate_pvalues(df):
    df = df.dropna()._get_numeric_data()
    dfcols = pd.DataFrame(columns=df.columns)
    pvalues = dfcols.transpose().join(dfcols, how='outer')
    for r in df.columns:
        for c in df.columns:
            pvalues[r][c] = round(pearsonr(df[r], df[c])[1], 4)
    return pvalues

all, dim, all_Q_index = read_data('../data/')
for dimension in dim.keys():
    all[dimension] = all[dim[dimension]].sum(axis=1)

corr = all[dim.keys()].corr()
pvalues = calculate_pvalues(all[dim.keys()])
print(corr,"\n", pvalues)

# no obvious interscale's correlations
# no correlation between sensing and sequential anymore because I removed several questions
# An α of 0.05 indicates that the risk of concluding that a correlation exists—when, actually, no correlation exists—is 5%
