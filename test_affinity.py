import numpy as np
dataset_filename = "affinity_dataset.csv"
X = np.loadtxt(dataset_filename)
n_samples, n_features = X.shape
print(f"This dataset has {n_samples} samples and {n_features} features.")

# The names of the features
features = ["bread", "milk", "cheese", "apples", "bananas"]

print("First 5 samples:")
print(features)
print(X[:5])

# The names of the features
features = ["bread", "milk", "cheese", "apples", "bananas"]

# to compute the support and confidence of the rule
# "If a person buys apples, they also buy bananas."

# to count # of rows containing our premise: that a person is buying apples
num_apple_purchases = 0
for sample in X:
    if sample[3] == 1:
        num_apple_purchases += 1

print(f"{num_apple_purchases} people bought Apples.")

