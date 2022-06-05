## https://www.datacamp.com/community/tutorials/introduction-factor-analysis

import pandas as pd
import numpy as np
from read_data import read_data
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo

def find_n_maxi_values(all, n):
       all = all.transpose() # each row is for each factor
       first_n_index = (-all).argsort()[:,:n]
       mask = np.ones(all.shape, dtype=bool)  # np.ones_like(a,dtype=bool)
       for n, row in enumerate(mask):
              row[first_n_index[n]] = False
       all[mask] = 0
       return all.transpose()

## Bartlett’s test
def bartlett(all):
       chi_square_value,p_value=calculate_bartlett_sphericity(all)
       print(chi_square_value, p_value) # p value is inferior than 0.05, which is the critical statistically significant

## Kaiser-Meyer-Olkin (KMO) Test
def KMO(all):
       kmo_all, kmo_model = calculate_kmo(all)
       print(kmo_model) # Value of KMO less than 0.6 is considered inadequate.

def create_fa(all):
       # Create factor analysis object and perform factor analysis
       fa = FactorAnalyzer(n_factors=7, rotation="varimax")
       fa.fit(all)
       # # Check Eigenvalues
       ev, v = fa.get_eigenvalues()
       plt.plot(ev)
       plt.show
       print(ev)
       return fa

def plot_hmap(all): # all must be all numeric values
       fig, ax = plt.subplots()
       c = ax.pcolor(all)
       fig.colorbar(c, ax=ax)
       ax.set_yticks(np.arange(fa.loadings_.shape[0])+0.5, minor=False)
       ax.set_xticks(np.arange(fa.loadings_.shape[1])+0.5, minor=False)
       ax.set_xticklabels(['F1', "F2", "F3", "F4", "F5", "F6","F7"])
       ax.set_yticklabels(all_Q_index)
       plt.show()


all, dim, all_Q_index = read_data('../data/')
fa = create_fa(all)
Z = np.abs(fa.loadings_)
first_5 = find_n_maxi_values(Z, 5)
plot_hmap(first_5)


## confirmatory exploratory analysis

# model_spec = ModelSpecificationParser.parse_model_specification_from_dict(all, dim)
# cfa = ConfirmatoryFactorAnalyzer(model_spec, disp=False)
# cfa.fit(all.values)
# print(cfa.loadings_, cfa.factor_varcovs_)


# factors = pd.DataFrame(fa.loadings_)
# factors["Q_index"] = all_Q_index
# num = factors._get_numeric_data()
# # num[num<0.35] = 0
# plot_hmap(num)