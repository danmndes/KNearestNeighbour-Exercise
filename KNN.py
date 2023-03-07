import numpy as np
import pandas as pd
from sklearn import linear_model, preprocessing
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('car.data')
new_data = pd.DataFrame()

le = preprocessing.LabelEncoder()
for i in data.columns:
    new_data[i] = le.fit_transform(list(data[i]))

features = ['buying','maint','door','persons','lug_boot','safety']
X = new_data[features]
y = new_data.clas

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

model = KNeighborsClassifier(n_neighbors=9)

model.fit(x_train, y_train)
acc = model.score(x_test,y_test)
print(acc)

# for t in x_test:
#     print(x_test[[t]])
prediction = model.predict(x_test)

y_list = []

for index, row in y_test.iteritems():
    y_list.append(row)

for i,x in enumerate(prediction):
    print('Predicion: ', prediction[i], 'Actual: ', y_list[x])
