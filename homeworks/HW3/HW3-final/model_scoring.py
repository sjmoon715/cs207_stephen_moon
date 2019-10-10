from sklearn import datasets
from sklearn.model_selection import train_test_split
from Regression import Regression as rg
from Regression import LinearRegression as LR
from Regression import RidgeRegression as RR

dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'],dataset['target'],test_size=0.2,random_state=42)

# Initializing alpha at 0
alpha = 0
models = [LR(X_train, y_train), RR(X_train,y_train, alpha)]
models[1].set_params(alpha=0.1)

# Initializing empty list in order to compare R^2 scores
R2_scores = [0]*len(models)

# Training and scoring models in a for loop
for i in range(len(models)):
    models[i].fit(X_train, y_train)
    R2_score = models[i].score(X_test, y_test)
    # Using for loop to store R^2 scores
    R2_scores[i] = R2_score
    print(str(models[i].__class__.__name__)+" R^2 Score: "+str(R2_score))

# Comparing R^2 scores for different models and printing params of best one using get_params method
if R2_scores[0] > R2_scores[1]:
    print("Parameters of Best Model: " + str(models[0].get_params()))
else:
    print("Parameters of Best Model: "+ str(models[1].get_params()))

