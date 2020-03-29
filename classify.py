import numpy as np
from sklearn.datasets import load_iris

dataset = load_iris()
X = dataset.data
y = dataset.target

print(dataset.DESCR)
n_samples, n_features = X.shape

attribute_means = X.mean(axis=0)
assert attribute_means.shape == (n_features, )
X_d = np.array(X >= attribute_means, dtype = 'int')

# to split into a training set and test set
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split

random_state = 14
X_train, X_test, y_train, y_test = train_test_split(X_d, y, random_state = random_state)
print(f"There are {y_train.shape} training samples.")
print(f"There are {y_test.shape} training samples.")


