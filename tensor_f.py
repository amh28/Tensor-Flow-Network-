from __future__ import print_function

import numpy as np
import tflearn

# Download the Titanic dataset
	#from tflearn.datasets import titanic
	#titanic.download_dataset('titanic_dataset.csv')


# Load CSV file, indicate that the first column represents labels
from tflearn.data_utils import load_csv
data, labels = load_csv('car_replaced.csv', target_column=6,
                        categorical_labels=True, n_classes=4)


# Preprocessing function
def preprocess(data):
    
	for i in range(len(data)):
				
		if data[i][0] == 'vhigh':
			data[i][0] = 0

		elif data[i][0] == 'high':
			data[i][0] = 1	  	

		elif data[i][0] == 'med':
			data[i][0] = 2

		elif data[i][0] == 'low':
			data[i][0] = 3	  	


		if data[i][1] == 'vhigh':
			data[i][1] = 0

		elif data[i][1] == 'high':
			data[i][1] = 1	  	

		elif data[i][1] == 'med':
			data[i][1] = 2

		elif data[i][1] == 'low':
			data[i][1] = 3	  


		if data[i][2] == '2':
			data[i][2] = 0

		elif data[i][2] == '3':
			data[i][2] = 1	  	

		elif data[i][2] == '4':
			data[i][2] = 2

		elif data[i][2] == '5more':
			data[i][2] = 3	  



		if data[i][3] == '2':
			data[i][3] = 0

		elif data[i][3] == '4':
			data[i][3] = 1	  	

		elif data[i][3] == 'more':
			data[i][3] = 2


		if data[i][4] == 'small':
			data[i][4] = 0

		elif data[i][4] == 'med':
			data[i][4] = 1	  	

		elif data[i][4] == 'big':
			data[i][4] = 2



		if data[i][5] == 'low':
			data[i][5] = 0

		elif data[i][5] == 'med':
			data[i][5] = 1	  	

		elif data[i][5] == 'high':
			data[i][5] = 2	
							
	return np.array(data, dtype=np.float32)


# Preprocess data
data = preprocess(data)  


# Build neural network
net = tflearn.input_data(shape=[None, 6])
net = tflearn.fully_connected(net, 30, activation = 'sigmoid')
net = tflearn.fully_connected(net, 32, activation = 'softplus')
net = tflearn.fully_connected(net, 4, activation='softmax')
net = tflearn.regression(net)

# Define model
model = tflearn.DNN(net)
# Start training (apply gradient descent algorithm)

model.fit(data, labels, n_epoch=20, batch_size=1, show_metric=True)

# Preprocess data

#test1 = ['low','low',4,2,'big','high']
test1 = [3,3,2,0,2,2]
test2 = [3,3,3,1,1,1]
test3 = [3,3,3,2,2,0]
test4 = [1,0,1,1,2,1]


pred = model.predict([test1,test2,test3,test4])

print("test1:\n", "unacc: ", pred[0][0],"\n acc: ", pred[0][1], "\n good: ", pred[0][2], "\n vgood: ", pred[0][3] )
print("test2:\n", "unacc: ", pred[1][0],"\n acc: ", pred[1][1], "\n good: ", pred[1][2], "\n vgood: ", pred[1][3] )
print("test3:\n", "unacc: ", pred[2][0],"\n acc: ", pred[2][1], "\n good: ", pred[2][2], "\n vgood: ", pred[2][3] )
print("test4:\n", "unacc: ", pred[3][0],"\n acc: ", pred[3][1], "\n good: ", pred[3][2], "\n vgood: ", pred[3][3] )

