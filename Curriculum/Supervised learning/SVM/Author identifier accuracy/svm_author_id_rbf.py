#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#let the training sample be smaller
#features_train = features_train[:int(len(features_train)/100)]
#labels_train = labels_train[:int(len(labels_train)/100)]


#########################################################
### your code goes here ###

#########################################################
from sklearn import svm
clf = svm.SVC(kernel="rbf",C=10000)
t0 = time() #time calulator for training
clf.fit(features_train, labels_train)
print ("training time:",round(time()-t0,3),"s")
t0 = time()#time calulator for predict
pred = clf.predict(features_test)
print ("predict time:",round(time()-t0,3),"s")
from sklearn.metrics import accuracy_score
print (accuracy_score(pred, labels_test))
print (pred[10]) #To see the prediction result at the index
print (pred[26]) #To see the prediction result at the index
print (pred[50]) #To see the prediction result at the index
### To count the num of predict lable equels to Chris(1) in pred / There are over 1700 test sample
count = 0
for x in pred:
    if(x == 1):
        count=count+1
print (count)
