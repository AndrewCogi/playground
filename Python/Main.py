import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import chi2

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')

corrmat = train.corr()

corr_features = corrmat.index

print(corr_features)
