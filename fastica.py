from sklearn.datasets import load_digits
from sklearn.decomposition import FastICA

matr = FastICA(14)
print(type(matr))
X, _ = load_digits(return_X_y=True)
transformer = FastICA(n_components=7, random_state=0)
X_transformed = transformer.fit_transform(X)
X_transformed.shape
(1797, 7)
