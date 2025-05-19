import pandas as pd
import numpy as np

test_scores = np.random.randint(70,100,size=(10))
test_scores = pd.Series(test_scores)

test_scores.index = ['September', 'October', ' November', 'December', 'January', 'February', 'March', 'April', 'May', 'June']

# Year Avg Test Score
year_avg = test_scores.mean()

# Avg Test Score for first 5 months
first_avg = test_scores.iloc[:6].mean()

# Avg Test Score for last 5 months
last_avg = test_scores.iloc[6:].mean()

# Student Improvement
improvement = last_avg - first_avg

# Student highest score month
highest_score_month = test_scores.idxmax()

# Student five highest scores
highest_scores = test_scores.nlargest(5)

# Student scores rounded
rounded_scores = test_scores.round(decimals=-1)
print(rounded_scores)
