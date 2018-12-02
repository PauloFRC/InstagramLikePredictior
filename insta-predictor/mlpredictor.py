import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import datasets, linear_model, svm, naive_bayes, tree
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import math

def predict_next_like(x, y, to_predict, evaluate=False):

	if evaluate:
		test_size = 0.1
	else:
		test_size = 0

	post = x
	likes = y
	post_train, post_test, likes_train, likes_test = train_test_split(post, likes, test_size=test_size)
	regr = linear_model.ElasticNet()
	regr.fit(post_train, likes_train)

	total = 0

	for i in range(len(post_test)):
		prediction = regr.predict([post_test[i]])
		total += math.sqrt((prediction-likes_test[i])**2)

	preds = []
	for h in range(len(post)):
		preds.append(regr.predict([post[h]]))
	preds.append(regr.predict([[130,33]]))
	plt.plot(preds)
	plt.legend(['prediction'])
	plt.show()

	error_rate = total/len(post_test)
	final_prediction = regr.predict([to_predict])
	print("Prediction likes next post:",regr.predict([to_predict]))
	print('Error rate', error_rate)

	return final_prediction
