# import necessary libraries
from sklearn import tree
import database

# create empty lists to hold car information
x = []
y = []

# get all car information from the database and split it into features (x) and target (y)
for i in database.get_car():
    i = list(i[:])
    x.append(i[1:]) # append all columns except the first (car name) to x
    y.append(i[0]) # append the car name to y

# train a decision tree classifier on the data
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

# prompt the user to input car information to predict
print('Enter car information:')
m = int(input('Miles: '))
p = int(input('Price: '))

# create a new data point to predict on
new_data = [[m, p]]

# use the trained classifier to predict the car name
prediction = clf.predict(new_data)

# print the predicted car name
print(f'Predicted car is: {prediction[0]}')
