import torch
from tqdm.auto import tqdm
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

"""
Implementation of Autoencoder
"""
cnt=0
typ=1
class Autoencoder(nn.Module):
	def __init__(self, input_dim: int, encoding_dim: int) -> None:
		"""
		Modify the model architecture here for comparison
		"""
		super(Autoencoder, self).__init__() # 4880 -> 488
		global typ
		if typ==0: # Original
			self.encoder = nn.Sequential(
				nn.Linear(input_dim, encoding_dim),
				nn.Linear(encoding_dim, encoding_dim//2),
				nn.ReLU()
			)
			self.decoder = nn.Sequential(
				nn.Linear(encoding_dim//2, encoding_dim),
				nn.Linear(encoding_dim, input_dim),
			)
		if typ==1: # Deeper
			self.encoder=nn.Sequential(
				nn.Linear(input_dim, 128),
				nn.Linear(128, encoding_dim),
				nn.Linear(encoding_dim, encoding_dim//2),
				nn.ReLU()
			)
			self.decoder=nn.Sequential(
				nn.Linear(encoding_dim//2, encoding_dim),
				nn.Linear(encoding_dim, 128),
				nn.Linear(128, input_dim),
			)
		if typ==2:
			self.encoder = nn.Sequential(
				nn.Linear(input_dim, encoding_dim),
				#nn.Linear(encoding_dim, encoding_dim//2),
				nn.ReLU()
			)
			self.decoder = nn.Sequential(
				#nn.Linear(encoding_dim//2, encoding_dim),
				nn.Linear(encoding_dim, input_dim),
			)
	
	def forward(self, x):
		#TODO: 5%
		return self.decoder(self.encoder(x))
		# raise NotImplementedError
	
	def fit(self, X, epochs=10, batch_size=32):
		#TODO: 5%
		cri=nn.MSELoss()
		opt=optim.Adam(self.parameters())
		dset=torch.utils.data.TensorDataset(torch.tensor(X, dtype=torch.float32))
		dload=torch.utils.data.DataLoader(dset, batch_size=batch_size, shuffle=True)
		losses=[]
		for i in range(epochs):
			tt=0
			for data in dload:
				ins=data[0]
				opt.zero_grad()
				outs=self(ins)
				loss=cri(outs, ins)
				loss.backward()
				opt.step()
				tt+=loss.item()
			losses.append(tt/len(dload))
		plt.plot(losses)
		plt.xlabel('Epoch')
		plt.ylabel('Averaged Squared Error')
		plt.title('Autoencoder')
		plt.savefig('Autoencoder_Error.png')
		plt.close()
		# plt.show()
		# raise NotImplementedError
	
	def transform(self, X):
		#TODO: 2%
		with torch.no_grad():
			return self.encoder(torch.tensor(X, dtype=torch.float32)).numpy()
		# raise NotImplementedError
	
	def reconstruct(self, X):
		#TODO: 2%
		global cnt
		with torch.no_grad():
			res=self.forward(X).numpy()
		i0=X.reshape((61, 80))
		i1=res.reshape((61, 80))
		plt.figure(figsize=(10, 5))
		plt.subplot(1, 2, 1)
		name='Denoising_' if cnt else ''
		cnt+=1
		plt.title(name+'Autoencoder Original')
		plt.imshow(i0, cmap='gray')
		plt.subplot(1, 2, 2)
		plt.title(name+'Autoencoder Reconstructed')
		plt.imshow(i1, cmap='gray')
		plt.savefig(name+'Autoencoder_Compare.png')
		plt.close()
		# plt.show()
		return res
		# raise NotImplementedError


"""
Implementation of DenoisingAutoencoder
"""
class DenoisingAutoencoder(Autoencoder):
	def __init__(self, input_dim, encoding_dim, noise_factor=0.2):
		super(DenoisingAutoencoder, self).__init__(input_dim,encoding_dim)
		self.noise_factor = noise_factor
	
	def add_noise(self, x):
		#TODO: 3%
		return x+self.noise_factor*torch.randn_like(x)
		# raise NotImplementedError
	
	def fit(self, X, epochs=10, batch_size=32):
		#TODO: 4%
		cri=nn.MSELoss()
		opt=optim.Adam(self.parameters())
		dset=torch.utils.data.TensorDataset(torch.tensor(X, dtype=torch.float32))
		dload=torch.utils.data.DataLoader(dset, batch_size=batch_size, shuffle=True)
		losses=[]
		for i in range(epochs):
			tt=0
			for data in dload:
				ins=self.add_noise(data[0])
				opt.zero_grad()
				outs=self(ins)
				loss=cri(outs, ins)
				loss.backward()
				opt.step()
				tt+=loss.item()
			losses.append(tt/len(dload))
		plt.plot(losses)
		plt.xlabel('Epoch')
		plt.ylabel('Averaged Squared Error')
		plt.title('Denoising Autoencoder')
		plt.savefig('Denoising_Autoencoder_Error.png')
		plt.close()
		# plt.show()
		# raise NotImplementedError
