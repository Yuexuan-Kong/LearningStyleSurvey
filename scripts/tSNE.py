from sklearn.manifold import TSNE
from numpy import reshape
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from read_data import read_data

sns.set(rc={'figure.figsize':(11.7,8.27)})
palette = sns.color_palette("bright", 10)

all, dim, all_Q_index = read_data('../data/')
tsne = TSNE(init= "random", n_components=2, verbose=1, random_state=123)
X_embedded = tsne.fit_transform(all)
sns.scatterplot(X_embedded[:,0], X_embedded[:,1], legend='full', palette=palette)
plt.show()