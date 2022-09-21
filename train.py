import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split, RandomizedSearchCV, GridSearchCV, cross_val_score
import math
import seaborn as sns
import xgboost as xgb
from skopt import BayesSearchCV

df = pd.read_csv('train.csv', index_col='Date', parse_dates=True, low_memory=False)
df.sort_values(by='Date', inplace=True)