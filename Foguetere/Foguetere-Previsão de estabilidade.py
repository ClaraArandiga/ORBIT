import numpy as np
from sklearn.linear_model import LinearRegression

modelo = LinearRegression()
X_treino = np.array([[500, 300, 1.5, 45], [1000, 400, 2.0, 60]])
y_treino = np.array([0.8, 0.9])

modelo.fit(X_treino, y_treino)

def prever_estabilidade(params):
    X_novo = np.array([[params['volume'], params['pressao'], params['massa'], params['angulo']]])
    return float(modelo.predict(X_novo))
