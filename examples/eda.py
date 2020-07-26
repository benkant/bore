import pandas as pd
#Message from py37-pandas-0.24.2_1,1:
#
#--
#Install math/py-statsmodels to enable parts of pandas.stats.
#Install devel/py-xarray to enable the to_xarray() function.
import numpy as np
from scipy.stats import trim_mean

state = pd.read_csv('data/state.csv')
state['Population'].mean()
trim_mean(state['Population'], 0.1)
state['Population'].median()
