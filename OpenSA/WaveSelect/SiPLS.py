import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import cross_val_score
 
# 生成模拟光谱数据
def generate_spectral_data(samples, features, noise_level=0.1):
    np.random.seed(0)
    # 生成波长
    wavelengths = np.linspace(400, 2500, features)
    # 生成光谱数据，基于某些波长的线性组合加噪声
    X = np.random.randn(samples, features) + np.sin(wavelengths) * 10
    # 生成响应变量，同样是波长的线性组合加噪声
    Y = np.dot(X, np.sin(wavelengths)) * 0.5 + np.random.randn(samples) * noise_level
    return X, Y, wavelengths
 
# SiPLS算法
def SiPLS(X, Y, wavelengths, interval_length=10):
    n_intervals = X.shape[1] // interval_length
    scores = []
    
    for i in range(n_intervals):
        start = i * interval_length
        end = start + interval_length
        pls = PLSRegression(n_components=2)
        score = -np.mean(cross_val_score(pls, X[:, start:end], Y, cv=5, scoring='neg_mean_squared_error'))
        scores.append(score)
        
    # 返回每个区间的性能评分
    return np.array(scores), wavelengths[:n_intervals*interval_length:interval_length]
 
# 主函数
def main():
    samples = 100
    features = 200
    X, Y, wavelengths = generate_spectral_data(samples, features)
    
    # 应用SiPLS
    scores, selected_wavelengths = SiPLS(X, Y, wavelengths)
    
    # 绘图展示原始数据
    plt.figure(figsize=(15, 6))
    plt.subplot(2, 1, 1)
    plt.plot(wavelengths, X.T, color='grey', alpha=0.5)
    plt.title("Simulated Spectral Data")
    
    # 绘图展示SiPLS区间评分
    plt.subplot(2, 1, 2)
    plt.plot(selected_wavelengths, scores, marker='o')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('MSE Score')
    plt.title('SiPLS Interval Scores')
    plt.tight_layout()
    plt.show()
 
if __name__ == "__main__":
    main()