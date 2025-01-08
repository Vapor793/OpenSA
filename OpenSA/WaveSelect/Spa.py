import numpy as np
import matplotlib.pyplot as plt
 
def SPA(X, num_variables):
    num_samples, num_features = X.shape
    selected_variables = []
    P = np.eye(num_samples)
    for i in range(num_variables):
        var_projections = np.dot(X.T, P).T
        var_norms = np.sum(var_projections**2, axis=0)
        next_var = np.argmax(var_norms)
        selected_variables.append(next_var)
        xi = X[:, [next_var]]
        P = P - np.dot(np.dot(P, xi), np.dot(xi.T, P)) / np.dot(np.dot(xi.T, P), xi)
        column = np.arange(X.shape[1])
        Featuresecletidx = column[selected_variables]
    return Featuresecletidx