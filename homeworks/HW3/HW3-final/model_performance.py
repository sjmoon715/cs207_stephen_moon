import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from Regression import Regression as rg
from Regression import LinearRegression as LR
from Regression import RidgeRegression as RR

dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'],dataset['target'],test_size=0.2,random_state=42)
alpha = np.arange(0.05, 1, 0.1)

models = [LR(X_train, y_train), RR(X_train,y_train, alpha)]
# Creating empty list in order to graph LR scores
LR_scores = [0]*len(alpha)
for i in range(len(alpha)):
    models[0].fit(X_train, y_train)
    # Storing Linear Regression R^2 scores in list
    LR_scores[i] = models[0].score(X_test,y_test)

RR_scores = [0]*len(alpha)
for i in range(len(alpha)):
    # Changing alpha value each time through for loop
    models[1].set_params(alpha=alpha[i])
    models[1].fit(X_train, y_train)
    # Storing Ridge Regression R^2 scores in list
    RR_scores[i] = models[1].score(X_test, y_test)

plt.plot(alpha, RR_scores, label="Ridge Regression")
plt.plot(alpha, LR_scores, label="Linear Regression")
plt.xlabel("Alpha Values")
plt.ylabel("R^2 Score")
plt.plot(marker='o', color='b')
plt.legend()

plt.show()
