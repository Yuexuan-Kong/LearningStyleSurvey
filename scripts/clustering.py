import pandas as pd
import numpy as np
from read_data import read_data
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE

def choose_k(all):
    clusters = []
    for i in range(10, 20):
        km = KMeans(n_clusters=i).fit(all)
        clusters.append(km.inertia_)

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.lineplot(x=list(range(10, 20)), y=clusters, ax=ax)
    ax.set_title('Searching for Elbow')
    ax.set_xlabel('Clusters')
    ax.set_ylabel('Inertia')
    plt.show()

def plot_two_dim(all, k=16):
    km16 = KMeans(n_clusters=k).fit(all)
    all['Labels'] = km16.labels_
    plt.figure(figsize=(12, 8))
    sns.scatterplot(all["Act_Ref"], all["Sen_Int"], hue=all['Labels'],
                    palette=sns.color_palette('hls', 16))
    plt.title('KMeans with 18 Clusters')
    plt.show()
    return km16

def plot_each_dim(all):
    fig = plt.figure(figsize=(20,8))
    ax = fig.add_subplot(231)
    sns.swarmplot(x='Labels', y='Act_Ref', data=all, ax=ax)
    ax.set_title('Labels According to act_ref')
    ax = fig.add_subplot(232)
    sns.swarmplot(x='Labels', y='Sen_Int', data=all, ax=ax)
    ax.set_title('Labels According to sen_int')
    ax = fig.add_subplot(233)
    sns.swarmplot(x='Labels', y='Vis_Ver', data=all, ax=ax)
    ax.set_title('Labels According to vis_ver')
    ax = fig.add_subplot(234)
    sns.swarmplot(x='Labels', y='Seq_Glo', data=all, ax=ax)
    ax.set_title('Labels According to seq_glo')
    ax = fig.add_subplot(235)
    sns.swarmplot(x='Labels', y='Ded_Ind', data=all, ax=ax)
    ax.set_title('Labels According to ded_ind')
    ax = fig.add_subplot(236)
    sns.swarmplot(x='Labels', y='Lea_Per', data=all, ax=ax)
    ax.set_title('Labels According to lea_per')
    plt.show()

all, dim, all_Q_index = read_data('../data/')
for d in dim.keys():
    all[d] = all[dim[d]].sum(axis=1)
    all[d+"_normalized"] = (all[d]-all[d].mean())/all[d].std()


# choose_k(all)
km16 = plot_two_dim(all)
# plot_each_dim(all)
center = []
for d in dim.keys():
    c = km16.cluster_centers_[:, np.where(km16.feature_names_in_ == d+"_normalized")].flatten()
    center.append(c)
center = pd.DataFrame(np.array(center))
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(center)




