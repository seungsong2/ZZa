import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
header = ['preg', 'plas', 'pres', 'skin',
          'test', 'mass', 'pedi','age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names = header)

array = data.values
X = array[:,0:8]
Y = array[:,8]
print(X.shape, Y.shape)




#scaler = StandardScaler()
#scaler = MinMaxScaler(feature_range=(0,1))
#rescales_X = scaler.fit_transform(X)


