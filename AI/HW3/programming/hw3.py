from collections import Counter

import numpy as np
import pandas as pd
from math import *

oo=1e18
def sigma(a):
	return 1/(1+exp(-a))

def mode(a):
	return np.argmax(np.bincount(a))


# set random seed
np.random.seed(0)

"""
Tips for debugging:
- Use `print` to check the shape of your data. Shape mismatch is a common error.
- Use `ipdb` to debug your code
	- `ipdb.set_trace()` to set breakpoints and check the values of your variables in interactive mode
	- `python -m ipdb -c continue hw3.py` to run the entire script in debug mode. Once the script is paused, you can use `n` to step through the code line by line.
"""


# 1. Load datasets
def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
	"""
	DO NOT MODIFY THIS FUNCTION.
	"""
	# Load iris dataset
	iris = pd.read_csv(
		"https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
		header=None,
	)
	iris.columns = [
		"sepal_length",
		"sepal_width",
		"petal_length",
		"petal_width",
		"class",
	]

	# Load Boston housing dataset
	boston = pd.read_csv(
		"https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
	)

	return iris, boston


# 2. Preprocessing functions
def train_test_split(
	df: pd.DataFrame, target: str, test_size: float = 0.3
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
	# Shuffle and split dataset into train and test sets
	df = df.sample(frac=1, random_state=42).reset_index(drop=True)
	split_idx = int(len(df) * (1 - test_size))
	train = df.iloc[:split_idx]
	test = df.iloc[split_idx:]

	# Split target and features
	X_train = train.drop(target, axis=1).values
	y_train = train[target].values
	X_test = test.drop(target, axis=1).values
	y_test = test[target].values

	return X_train, X_test, y_train, y_test

mnx=oo
mxx=-oo
mu=oo
var=oo

def init():
	global mnx, mxx, mu, var
	mnx, mxx=oo, -oo
	mu, var=oo, oo

def normalize(X: np.ndarray) -> np.ndarray:
	# Normalize features to [0, 1]
	# You can try other normalization methods, e.g., z-score, etc.
	# TODO: 1%
	m=len(X[0])
	global mnx, mxx
	if mnx==oo:
		mnx=[oo for i in range(m)]
		mxx=[-oo for i in range(m)]
		for i in X:
			for j in range(m):
				mnx[j], mxx[j]=min(mnx[j], i[j]), max(mxx[j], i[j])
	return np.array([[(i[j]-mnx[j])/(mxx[j]-mnx[j]) for j in range(m)] for i in X])
	# raise NotImplementedError

def standardize(X: np.ndarray) -> np.ndarray:
	m=len(X[0])
	global mu, var
	if mu==oo:
		mu=[np.mean(X[:, i]) for i in range(m)]
		#print([(j-mu[0])**2 for j in X[:, 0]])
		var=[sqrt(np.mean([(j-mu[i])**2 for j in X[:, i]])) for i in range(m)]
	return np.array([[(i[j]-mu[j])/var[j] for j in range(m)] for i in X])


typ={}

def encode_labels(y: np.ndarray) -> np.ndarray:
	"""
	Encode labels to integers.
	"""
	# TODO: 1%
	global typ
	if len(typ)==0:
		for i in y:
			if i not in typ:
				typ[i]=len(typ)
	return np.array([typ[i] for i in y])
	# raise NotImplementedError


# 3. Models
class LinearModel:
	def __init__(
		self, learning_rate=0.01, iterations=1000, model_type="linear"
	) -> None:
		self.learning_rate = learning_rate
		self.iterations = iterations
		# You can try different learning rate and iterations
		self.model_type = model_type

		assert model_type in [
			"linear",
			"logistic",
		], "model_type must be either 'linear' or 'logistic'"

	def fit(self, X: np.ndarray, y: np.ndarray) -> None:
		X = np.insert(X, 0, 1, axis=1)
		n_classes = len(np.unique(y))
		n_features = X.shape[1]

		n_classes=max(y)+1
		if self.model_type == "logistic":
			self.W=np.array([[0.0 for j in range(n_features)] for i in range(n_classes)])
			for i in range(self.iterations):
				self.W=self.W-self._compute_gradients(X, y)*self.learning_rate
			# pass
		else:
			# self.w=np.dot(np.linalg.pinv(X), y)
			self.w=np.array([0.0 for i in range(n_features)])
			for i in range(self.iterations):
				self.w=self.w-self._compute_gradients(X, y)*self.learning_rate
			# pass
		# TODO: 2%
		# raise NotImplementedError

	def predict(self, X: np.ndarray) -> np.ndarray:
		X = np.insert(X, 0, 1, axis=1)
		if self.model_type == "linear":
			# TODO: 2%
			return np.dot(X, self.w)
			# raise NotImplementedError
		elif self.model_type == "logistic":
			# TODO: 2%
			#p=np.dot(X, np.transpose(self.W))
			p=self._softmax(np.dot(X, np.transpose(self.W)))
			return np.array([np.argmax(i) for i in p])
			# raise NotImplementedError

	def _compute_gradients(self, X: np.ndarray, y: np.ndarray) -> np.ndarray:
		if self.model_type == "linear":
			# TODO: 3%
			return sum([2*(np.dot(self.w, X[i])-y[i])*X[i] for i in range(len(X))])/len(X)
			# raise NotImplementedError
		elif self.model_type == "logistic":
			# TODO: 3%
			res=[]
			for i in range(len(self.W)):
				yt=[1 if j==i else -1 for j in y]
				res.append(sum([sigma(-yt[j]*np.dot(self.W[i], X[j]))*(-yt[j]*X[j]) for j in range(len(X))])/len(X))
			return np.array(res)
			# raise NotImplementedError

	def _softmax(self, z: np.ndarray) -> np.ndarray:
		exp = np.exp(z)
		return exp / np.sum(exp, axis=1, keepdims=True)


class DecisionTree:
	def __init__(self, max_depth: int = 5, model_type: str = "classifier"):
		self.max_depth = max_depth
		self.model_type = model_type

		assert model_type in [
			"classifier",
			"regressor",
		], "model_type must be either 'classifier' or 'regressor'"

	def fit(self, X: np.ndarray, y: np.ndarray) -> None:
		self.tree = self._build_tree(X, y, 0)

	def predict(self, X: np.ndarray) -> np.ndarray:
		return np.array([self._traverse_tree(x, self.tree) for x in X])

	def _build_tree(self, X: np.ndarray, y: np.ndarray, depth: int) -> dict:
		if depth >= self.max_depth or self._is_pure(y):
			return self._create_leaf(y)

		feature, threshold = self._find_best_split(X, y)
		# TODO: 4%
		Xl, Xr=[], []
		yl, yr=[], []
		for i in range(len(X)):
			if X[i][feature]<=threshold:
				Xl.append(X[i])
				yl.append(y[i])
			else:
				Xr.append(X[i])
				yr.append(y[i])
		left_child=self._build_tree(np.array(Xl), np.array(yl), depth+1)
		right_child=self._build_tree(np.array(Xr), np.array(yr), depth+1)
		# raise NotImplementedError


		return {
			"feature": feature,
			"threshold": threshold,
			"left": left_child,
			"right": right_child,
		}

	def _is_pure(self, y: np.ndarray) -> bool:
		return len(set(y)) == 1

	def _create_leaf(self, y: np.ndarray):
		if self.model_type == "classifier":
			# TODO: 1%
			return mode(y)
			# raise NotImplementedError
		else:
			# TODO: 1%
			return np.mean(y)
			# raise NotImplementedError

	def _find_best_split(self, X: np.ndarray, y: np.ndarray) -> tuple[int, float]:
		best_gini = float("inf")
		best_mse = float("inf")
		best_feature = None
		best_threshold = None

		for feature in range(X.shape[1]):
			sorted_indices = np.argsort(X[:, feature])
			for i in range(1, len(X)):
				if X[sorted_indices[i - 1], feature] != X[sorted_indices[i], feature]:
					threshold = (
						X[sorted_indices[i - 1], feature]
						+ X[sorted_indices[i], feature]
					) / 2
					mask = X[:, feature] <= threshold
					left_y, right_y = y[mask], y[~mask]

					if self.model_type == "classifier":
						gini = self._gini_index(left_y, right_y)
						if gini < best_gini:
							best_gini = gini
							best_feature = feature
							best_threshold = threshold
					else:
						mse = self._mse(left_y, right_y)
						if mse < best_mse:
							best_mse = mse
							best_feature = feature
							best_threshold = threshold

		return best_feature, best_threshold

	def _gini_index(self, left_y: np.ndarray, right_y: np.ndarray) -> float:
		# TODO: 4%
		cntl=np.bincount(left_y)
		cntr=np.bincount(right_y)
		cntl=[(i/len(left_y))**2 for i in cntl]
		cntr=[(i/len(right_y))**2 for i in cntr]
		return (len(left_y)*(1-sum(cntl))+len(right_y)*(1-sum(cntr)))/(len(left_y)+len(right_y))
		# raise NotImplementedError


	def _mse(self, left_y: np.ndarray, right_y: np.ndarray) -> float:
		# TODO: 4%
		ly, ry=np.mean(left_y), np.mean(right_y)
		return (sum([(i-ly)**2 for i in left_y])+sum([(i-ry)**2 for i in right_y]))/(len(left_y)+len(right_y))
		# raise NotImplementedError

	def _traverse_tree(self, x: np.ndarray, node: dict):
		if isinstance(node, dict):
			feature, threshold = node["feature"], node["threshold"]
			if x[feature] <= threshold:
				return self._traverse_tree(x, node["left"])
			else:
				return self._traverse_tree(x, node["right"])
		else:
			return node


class RandomForest:
	def __init__(
		self,
		n_estimators: int = 100,
		max_depth: int = 5,
		model_type: str = "classifier",
	):
		# TODO: 1%
		self.model_type=model_type
		self.trees=[DecisionTree(max_depth=max_depth, model_type=model_type) for i in range(n_estimators)]
		# raise NotImplementedError

	def fit(self, X: np.ndarray, y: np.ndarray) -> None:
		for tree in self.trees:
			# TODO: 2%
			bootstrap_indices = np.random.choice(len(X), round(len(X)*0.7))
			Xt=np.array([X[i] for i in bootstrap_indices])
			yt=np.array([y[i] for i in bootstrap_indices])
			tree.fit(Xt, yt)
			# raise NotImplementedError

	def predict(self, X: np.ndarray) -> np.ndarray:
		# TODO: 2%
		y=[i.predict(X) for i in self.trees]
		return np.array([mode([j[i] for j in y]) if self.model_type=='classifier' else np.mean([j[i] for j in y]) for i in range(len(X))])
		# raise NotImplementedError


# 4. Evaluation metrics
def accuracy(y_true, y_pred):
	# TODO: 1%
	ac=0
	for i in range(len(y_true)):
		if y_true[i]==y_pred[i]:
			ac+=1
	return ac/len(y_true)
	# raise NotImplementedError


def mean_squared_error(y_true, y_pred):
	# TODO: 1%
	return np.mean([(y_true[i]-y_pred[i])**2 for i in range(len(y_true))])
	# raise NotImplementedError


# 5. Main function
def main():
	init()
	iris, boston = load_data()

	# Iris dataset - Classification
	X_train, X_test, y_train, y_test = train_test_split(iris, "class")
	X_train, X_test = normalize(X_train), normalize(X_test)
	y_train, y_test = encode_labels(y_train), encode_labels(y_test)

	logistic_regression = LinearModel(model_type="logistic")
	logistic_regression.fit(X_train, y_train)
	y_pred = logistic_regression.predict(X_test)
	#print("Logistic Regression Ein:", accuracy(y_train, logistic_regression.predict(X_train)))
	print("Logistic Regression Accuracy:", accuracy(y_test, y_pred))

	X_train, X_test=standardize(X_train), standardize(X_test)
	logistic_regression = LinearModel(model_type="logistic")
	logistic_regression.fit(X_train, y_train)
	y_pred = logistic_regression.predict(X_test)
	print("Logistic Regression Accuracy:", accuracy(y_test, y_pred))

	logistic_regression = LinearModel(model_type="logistic", iterations=10000)
	logistic_regression.fit(X_train, y_train)
	y_pred = logistic_regression.predict(X_test)
	print("Logistic Regression Accuracy:", accuracy(y_test, y_pred))
	logistic_regression = LinearModel(model_type="logistic", learning_rate=0.1)
	logistic_regression.fit(X_train, y_train)
	y_pred = logistic_regression.predict(X_test)
	print("Logistic Regression Accuracy:", accuracy(y_test, y_pred))

	decision_tree_classifier = DecisionTree(model_type="classifier")
	decision_tree_classifier.fit(X_train, y_train)
	#print("Decision Tree Classifier Ein:", accuracy(y_train, decision_tree_classifier.predict(X_train)))
	y_pred = decision_tree_classifier.predict(X_test)
	print("Decision Tree Classifier Accuracy:", accuracy(y_test, y_pred))

	random_forest_classifier = RandomForest(model_type="classifier")
	random_forest_classifier.fit(X_train, y_train)
	#print("Random Forest Classifier Ein:", accuracy(y_train, random_forest_classifier.predict(X_train)))
	y_pred = random_forest_classifier.predict(X_test)
	print("Random Forest Classifier Accuracy:", accuracy(y_test, y_pred))
	
	# random_forest_classifier = RandomForest(model_type="classifier", n_estimators=500)
	# random_forest_classifier.fit(X_train, y_train)
	# y_pred = random_forest_classifier.predict(X_test)
	# print("Random Forest Classifier Accuracy:", accuracy(y_test, y_pred))
	# random_forest_classifier = RandomForest(model_type="classifier", max_depth=10)
	# random_forest_classifier.fit(X_train, y_train)
	# y_pred = random_forest_classifier.predict(X_test)
	# print("Random Forest Classifier Accuracy:", accuracy(y_test, y_pred))
	random_forest_classifier = RandomForest(model_type="classifier", n_estimators=10)
	random_forest_classifier.fit(X_train, y_train)
	y_pred = random_forest_classifier.predict(X_test)
	print("Random Forest Classifier Accuracy:", accuracy(y_test, y_pred))
	random_forest_classifier = RandomForest(model_type="classifier", max_depth=2)
	random_forest_classifier.fit(X_train, y_train)
	y_pred = random_forest_classifier.predict(X_test)
	print("Random Forest Classifier Accuracy:", accuracy(y_test, y_pred))

	# Boston dataset - Regression
	init()

	X_train, X_test, y_train, y_test = train_test_split(boston, "medv")
	X_train, X_test = normalize(X_train), normalize(X_test)

	linear_regression = LinearModel(model_type="linear")
	linear_regression.fit(X_train, y_train)
	y_pred = linear_regression.predict(X_test)
	print("Linear Regression MSE:", mean_squared_error(y_test, y_pred))

	X_train, X_test = standardize(X_train), standardize(X_test)

	linear_regression = LinearModel(model_type="linear")
	linear_regression.fit(X_train, y_train)
	y_pred = linear_regression.predict(X_test)
	print("Linear Regression MSE:", mean_squared_error(y_test, y_pred))

	linear_regression = LinearModel(model_type="linear", iterations=10000)
	linear_regression.fit(X_train, y_train)
	y_pred = linear_regression.predict(X_test)
	print("Linear Regression MSE:", mean_squared_error(y_test, y_pred))
	linear_regression = LinearModel(model_type="linear", learning_rate=0.1)
	linear_regression.fit(X_train, y_train)
	y_pred = linear_regression.predict(X_test)
	print("Linear Regression MSE:", mean_squared_error(y_test, y_pred))

	decision_tree_regressor = DecisionTree(model_type="regressor")
	decision_tree_regressor.fit(X_train, y_train)
	y_pred = decision_tree_regressor.predict(X_test)
	print("Decision Tree Regressor MSE:", mean_squared_error(y_test, y_pred))

	random_forest_regressor = RandomForest(model_type="regressor")
	random_forest_regressor.fit(X_train, y_train)
	y_pred = random_forest_regressor.predict(X_test)
	print("Random Forest Regressor MSE:", mean_squared_error(y_test, y_pred))
	random_forest_regressor = RandomForest(model_type="regressor", n_estimators=500)
	random_forest_regressor.fit(X_train, y_train)
	y_pred = random_forest_regressor.predict(X_test)
	print("Random Forest Regressor MSE:", mean_squared_error(y_test, y_pred))
	random_forest_regressor = RandomForest(model_type="regressor", max_depth=10)
	random_forest_regressor.fit(X_train, y_train)
	y_pred = random_forest_regressor.predict(X_test)
	print("Random Forest Regressor MSE:", mean_squared_error(y_test, y_pred))

if __name__ == "__main__":
	main()
