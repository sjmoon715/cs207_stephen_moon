import sqlite3
import pandas as pd
import numpy as np
import re

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer

db = sqlite3.connect('regression.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS model_params")
cursor.execute("DROP TABLE IF EXISTS model_coefs")
cursor.execute("DROP TABLE IF EXISTS model_results")
cursor.execute("PRAGMA foreign_keys=1")

# Creating tables in sql database
cursor.execute('''CREATE TABLE model_params (
                id INTEGER PRIMARY KEY NOT NULL,
                desc TEXT,
                param_name TEXT,
                value TEXT)''')
db.commit()

cursor.execute('''CREATE TABLE model_coefs (
                id INTEGER PRIMARY KEY NOT NULL,
                desc TEXT,
                feature_name TEXT,
                value TEXT)''')
db.commit()

cursor.execute('''CREATE TABLE model_results (
                id INTEGER PRIMARY KEY NOT NULL,
                desc TEXT,
                train_score FLOAT,
                test_score FLOAT)''')
db.commit()

# Load data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=87)

def save_to_database(model_id, model_desc, db, model, X_train, X_test, y_train, y_test):
    database = sqlite3.connect(db)
    cursor = database.cursor()
    
    # Entries for model_params table
    params = model.get_params()
    param_names = str(list(params.keys()))
    param_values = str(list(params.values()))

    cursor.execute('''INSERT INTO model_params
                (id, desc, param_name, value)
                VALUES(?,?,?,?)''',(model_id, model_desc, param_names, param_values))
    database.commit()

    # Entires for model_coefs table
    feature_name = list(X_train.columns)
    coef = model.coef_
    intercept = model.intercept_
    feature_name.append("intercept")
    feature_name = str(feature_name)
    feature_value = str(np.append(coef, intercept).tolist())

    cursor.execute('''INSERT INTO model_coefs
                (id, desc, feature_name, value)
                VALUES(?,?,?,?)''',(model_id, model_desc, feature_name, feature_value))
    database.commit()

    # Entries for model_results table
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)

    cursor.execute('''INSERT INTO model_results
                (id, desc, train_score, test_score)
                VALUES(?,?,?,?)''',(model_id, model_desc, train_score, test_score))
    database.commit()

# Baseline Model
baseline_model = LogisticRegression(solver='liblinear')
baseline_model.fit(X_train, y_train)
save_to_database(1, "Baseline model", 'regression.sqlite', baseline_model, X_train, X_test, y_train, y_test)

# Reduced Model
feature_cols = ["mean radius",
                "texture error",
                "worst radius",
                "worst compactness",
                "worst concavity"]
X_train_reduced = X_train[feature_cols]
X_test_reduced = X_test[feature_cols]
reduced_model = LogisticRegression(solver="liblinear")
reduced_model.fit(X_train_reduced, y_train)
save_to_database(2, "Reduced model", "regression.sqlite", reduced_model, X_train_reduced, X_test_reduced, y_train, y_test)

# Penalized Model
L1_penalty_model = LogisticRegression(solver="liblinear", penalty="l1", max_iter=1000)
L1_penalty_model.fit(X_train, y_train)
save_to_database(3, "L1 penalty model", 'regression.sqlite', L1_penalty_model, X_train, X_test, y_train, y_test)

# Query selects id and test score of best model from model_results table
cursor.execute('''SELECT id, test_score FROM model_results ORDER BY test_score DESC LIMIT 1''')
query = cursor.fetchall()   
print("Best Model ID: " + str(query[0][0])) 
print("Best Validation Score: " + str(query[0][1]))

# Query selects feature names and values from model_coefs table
cursor.execute('''SELECT feature_name, value FROM model_coefs''')
query1 = cursor.fetchall()
feature_names = query1[0][0]
coefs = query1[0][1]
feature_list = re.split("[',']", feature_names)[1::3]
coefs_list = [float(x.strip()) for x in coefs[1:-1].split(',')]
for i in range(len(feature_list)):
    print(str(feature_list[i]) + ": " + str(coefs_list[i]))

# Recreating best model using extracted coefficients
Part_C_model = LogisticRegression(solver="liblinear", penalty="l1", max_iter=1000)
Part_C_model.fit(X_train, y_train)
Part_C_model.coef_ = np.asarray([coefs_list[:-1]])
Part_C_model.intercept_ = np.asarray([coefs_list[-1]])
model_score = Part_C_model.score(X_test, y_test)
print("Prob 2 Part C Model Score: " + str(model_score))

db.close()