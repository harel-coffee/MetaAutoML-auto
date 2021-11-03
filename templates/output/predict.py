import pickle
import pandas as pd

from flaml import AutoML

if __name__ == '__main__':
	X = pd.read_csv(#REPLAVE WITH PATH TO PREDICTION CSV, quotechar='"', skipinitialspace=True)
	with open('flaml-model', 'rb') as file:
		automl2 = pickle.load(file)

	predicted_y = automl2.predict(X)
	print(predicted_y)