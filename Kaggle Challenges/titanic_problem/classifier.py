import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from patsy import dmatrices
import sklearn.ensemble as ske


df = pd.read_csv('train.csv')

# removing low quality feature that has lots of NaNs
df = df.drop(['Ticket','Cabin'], axis=1) 

# removing NaNs values
df = df.dropna()

formula_ml = 'Survived ~ C(Pclass) + C(Sex) + Age + SibSp + Parch + C(Embarked)'

# Create the random forest model and fit the model to our training data
y, x = dmatrices(formula_ml, data=df, return_type='dataframe')
# RandomForestClassifier expects a 1 demensional NumPy array, so we convert
y = np.asarray(y).ravel()

results_rf = ske.RandomForestClassifier(n_estimators=100).fit(x, y)

# Score the results
score = results_rf.score(x, y)
print "Mean accuracy: {0}".format(score)

