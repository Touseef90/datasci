from sklearn import tree

# apple , orange
# [weight, surface]
# feature = [[140, "smooth"], [130, "smooth"], [150, "bumpy"], [170, "bumpy"]]
feature = [[140, 0], [130, 0], [150, 1], [170, 1]]
# label = ["apple", "apple", "orange", "orange"]
label = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(feature, label)
print(clf.predict([[150, 1]]))