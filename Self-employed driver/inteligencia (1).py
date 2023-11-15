import numpy as np
import pickle
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
import matplotlib as mpl

mpl.use("Qt5Cairo")

datos = np.loadtxt("./datos.txt")

idxRayInicio = 6
numRays = 24
idxRayFinal = idxRayInicio + numRays

idx = np.r_[0:2, idxRayInicio:idxRayFinal]
X = datos[:, idx]

y = datos[:, idxRayFinal:]
y = y[:, 3]

datasets = train_test_split(X, y, test_size=0.2)

train_X, test_X, train_y, test_y = datasets

mlp = MLPRegressor(hidden_layer_sizes=(8,8,8),
                   solver='adam', tol=1e-15,
                   learning_rate='adaptive',
                   max_iter=580000000,
                   activation='identity')

mlp.fit(train_X, train_y)

y_pred = mlp.predict(test_X)

puntos = mlp.score(test_X, test_y)

nombreArchivo = 'red_neuronal.drv'
pickle.dump(mlp, open(nombreArchivo, 'wb'))