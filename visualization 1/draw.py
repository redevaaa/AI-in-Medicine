import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("whitegrid")

sns.set_palette("Set2")
#sns.cubehelix_palette(8)

splitter = sns.load_dataset("splitter")
feature = sns.load_dataset("feature")
hh = sns.load_dataset("3")

sns.barplot(x="VALUE", y="SET", hue="METHOD", data=splitter)
plt.show()
sns.barplot(x="VALUE", y="SET", hue="METHOD",data=feature)
plt.show()
sns.barplot(x="VALUE", y="SET", hue="METHOD", data=hh)
plt.show()

#palette=sns.hls_palette(8, l=.8, s=.8),