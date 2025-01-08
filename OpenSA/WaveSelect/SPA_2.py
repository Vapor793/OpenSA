import numpy as np
import matplotlib.pyplot as plt
 
def successive_projections_algorithm(X, num_variables):
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
    return selected_variables
 
# 模拟一些数据作为示例
np.random.seed(0)
num_samples = 200
num_features = 100
X = np.random.rand(num_samples, num_features)  # 模拟的光谱数据
 
# 使用SPA选择特征
num_selected_variables = 10  # 你希望选择的特征数量
selected_wavelengths = successive_projections_algorithm(X, num_selected_variables)
 
# 绘图以显示原始光谱数据和选定的特征波长
average_spectrum = np.mean(X, axis=0)
wavelengths = np.arange(num_features)  # 假设波长是连续的整数值
 
plt.figure(figsize=(12, 6))
plt.plot(wavelengths, average_spectrum, label='Average Spectrum')
plt.scatter(wavelengths[selected_wavelengths], average_spectrum[selected_wavelengths], color='red', label='Selected Wavelengths')
plt.xlabel('Wavelength')
plt.ylabel('Intensity')
plt.title('Spectral Data with Selected Features by SPA')
plt.legend()
plt.show()