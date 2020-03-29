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

# how many of the cases that a person bought apples involved 
# the people purchasing bananas too?
# record the cases where the rule is valid and invalid
rule_valid = 0
rule_invalid = 0
for sample in X:
    if sample[3] == 1:
        if sample[4] == 1:
            rule_valid += 1    # the person who bought both apples and bananas
        else:
            rule_invalid += 1  # the person who bought apples, but not bananas

print(f"{rule_valid} cases of the rule being valid were discovered.")
print(f"{rule_invalid} cases of the rule being invalid were discovered.")

# to compute support and confidece
support = rule_valid
confidence = rule_valid / num_apple_purchases

print(f"The support of the rule is {support}.")
print("The confidende of the rule is {0:.1f}%.".format(100 * confidence))

from collections import defaultdict
# to compute all possible rules

valid_rules = defaultdict(int)
invalid_rules = defaultdict(int)
num_occurances = defaultdict(int)

for sample in X:
    for premise in range(n_features):
        if sample[premise] == 0: continue
        # record that the premise was bought in another transaction
        num_occurances[premise] += 1
        for conclusion in range(n_features):
            if premise == conclusion: continue            # little sense to measure if X->X
            if sample[conclusion] == 1:
                valid_rules[(premise, conclusion)] += 1   # the person also bought the conclusion 
            else:
                invalid_rules[(premise, conclusion)] += 1 # the person bought the premise, but not conclusion

support = valid_rules
confidence = defaultdict(float)
for premise, conclusion in valid_rules.keys():
    confidence[(premise, conclusion)] = valid_rules[(premise, conclusion)] / num_occurances[premise]

#print("valid_rules keys:", valid_rules.keys())
#print("valid_rules items:", valid_rules.items())

if 0:
    print("num_occurances:", num_occurances)
    print("support:", support)
    print("confidence: ", confidence)


    for premise, conclusion in confidence:
        premise_name = features[premise]
        conclusion_name = features[conclusion]
        print(f"Rule: If a person buys {premise_name}, s/he also buys {conclusion_name}:")
        print(f"Support: {support[(premise, conclusion)]}")
        print(f"Confidence: {confidence[(premise, conclusion)]:.3f}")

def print_rule(premise, conclusion, support, confidence, features):
    premise_name = features[premise]
    conclusion_name = features[conclusion]
    print(f"Rule: If a person buys {premise_name}, s/he also buys {conclusion_name}:")
    print(f"Support: {support[(premise, conclusion)]}")
    print(f"Confidence: {confidence[(premise, conclusion)]:.3f}")

premise = 1
conclusion = 3
print_rule(premise, conclusion, support, confidence, features)

from pprint import pprint
pprint(list(support.items()))

# Check the sorted confidence based on support order
from operator import itemgetter
sorted_support = sorted(support.items(), key = itemgetter(1), reverse = True)

for index in range(5):
    print(f"Rule{index + 1}:")
    (premise, conclusion) = sorted_support[index][0]
    print_rule(premise, conclusion, support, confidence, features)

print("\n\n\n")

# check the sorted confidence based on confidence order
sorted_confidence = sorted(confidence.items(), key = itemgetter(1), reverse = True)

for index in range(5):
    print(f"Rule{index + 1}:")
    (premise, conclusion) = sorted_confidence[index][0]
    print_rule(premise, conclusion, support, confidence, features)

