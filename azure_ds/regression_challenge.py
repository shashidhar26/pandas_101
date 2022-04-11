
import pandas as pd
import numpy as np

# load the training dataset
data = pd.read_csv('C:/Work/Learnings/Azure_DS/real_estate.csv')
data.head()

# Check more:
data.shape
data['local_convenience_stores'].unique()

# Numeric features: 
numeric_features = ['house_age', 'transit_distance','latitude','longitude']
data[numeric_features + ['price_per_unit']].describe()

# Plot numeric features: 
for col in numeric_features:
    fig = plt.figure(figsize=(9, 6))
    ax = fig.gca()
    feature = data[col]
    feature.hist(bins=100, ax = ax)
    ax.axvline(feature.mean(), color='magenta', linestyle='dashed', linewidth=2)
    ax.axvline(feature.median(), color='cyan', linestyle='dashed', linewidth=2)
    ax.set_title(col)
plt.show()


# plot a bar plot for each categorical feature count
categorical_features = ['transaction_date','local_convenience_stores']

for col in categorical_features:
    counts = data[col].value_counts().sort_index()
    fig = plt.figure(figsize=(9, 6))
    ax = fig.gca()
    counts.plot.bar(ax = ax, color='steelblue')
    ax.set_title(col + ' counts')
    ax.set_xlabel(col) 
    ax.set_ylabel("Frequency")
plt.show()

############################################################
# Correlation / Scatter plots
############################################################
for col in numeric_features:
    fig = plt.figure(figsize=(9, 6))
    ax = fig.gca()
    feature = data[col]
    label = data['price_per_unit']
    correlation = feature.corr(label)
    plt.scatter(x=feature, y=label)
    plt.xlabel(col)
    plt.ylabel('Price per unit')
    ax.set_title('price vs ' + col + '- correlation: ' + str(correlation))
plt.show()

############################################################
# Boxplot for categorical features
############################################################
# plot a boxplot for the label by each categorical feature
for col in categorical_features:
    fig = plt.figure(figsize=(9, 6))
    ax = fig.gca()
    data.boxplot(column = 'price_per_unit', by = col, ax = ax)
    ax.set_title('Label by ' + col)
    ax.set_ylabel("Price per unit")
plt.show()