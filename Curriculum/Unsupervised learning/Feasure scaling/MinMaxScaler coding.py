from sklearn.preprocessing import MinMaxScaler
import numpy
weights = numpy.array([[115.],[140.],[175.]]) # MinMaxScaler need float data instead of int
scaler = MinMaxScaler()
rescaled_weight = scaler.fit_transform(weights)
print(rescaled_weight)
