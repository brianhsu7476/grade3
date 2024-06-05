import numpy as np
import matplotlib.pyplot as plt

"""
Implementation of Principal Component Analysis.
"""
class PCA:
	def __init__(self, n_components: int) -> None:
		self.n_components = n_components
		self.mean = None
		self.components = None

	def fit(self, X: np.ndarray) -> None:
		#TODO: 10%
		self.mean=np.mean(X, axis=0)
		cov=np.cov(X-self.mean, rowvar=False)
		val, vec=np.linalg.eigh(cov)
		self.components=vec[:, np.argsort(val)[-1:-self.n_components-1:-1]]
		# raise NotImplementedError

	def transform(self, X: np.ndarray) -> np.ndarray:
		#TODO: 2%
		return np.dot(X-self.mean, self.components)
		# raise NotImplementedError

	def eigenface(self, X: np.ndarray, ith) -> None:
		#self.mean=np.mean(X, axis=0)
		#cov=np.cov(X-self.mean, rowvar=False)
		#val, vec=np.linalg.eigh(cov)
		#self.components=vec[:, np.argsort(val)[-ith:-ith-1:-1]]
		if ith:
			components=self.components[:, ith-1:ith]
		else:
			components=self.mean
		res=components
		#res=np.dot(np.dot(X-self.mean, components), components.T)+self.mean
		#i0=X.reshape((61, 80))
		i1=res.reshape((61, 80))
		#plt.figure(figsize=(10, 5))
		#plt.subplot(1, 2, 1)
		#plt.title('PCA Original')
		#plt.imshow(i0, cmap='gray')
		#plt.subplot(1, 2, 2)
		if ith==0:
			plt.title('PCA Mean')
		else:
			plt.title('PCA '+str(ith)+'-th Eigenvector')
		plt.imshow(i1, cmap='gray')
		plt.savefig('PCA_Eigen'+str(ith)+'.png')
		plt.close()

	def reconstruct(self, X):
		for i in range(5):
			self.eigenface(X, i)
		res=np.dot(self.transform(X), self.components.T)+self.mean
		i0=X.reshape((61, 80))
		i1=res.reshape((61, 80))
		plt.figure(figsize=(10, 5))
		plt.subplot(1, 2, 1)
		plt.title('PCA Original')
		plt.imshow(i0, cmap='gray')
		plt.subplot(1, 2, 2)
		plt.title('PCA Reconstructed')
		plt.imshow(i1, cmap='gray')
		plt.savefig('PCA_Compare.png')
		plt.close()
		# plt.show()
		return res
		# raise NotImplementedError
		#TODO: 2%
