import random
import pylab as pl
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.lda import LDA
from sklearn.qda import QDA

#test mode
mode = 3

if mode == 1:
    test = pd.read_csv("test.csv")
    data = pd.read_csv("train.csv")
elif mode == 2:
    test = pd.read_csv("train.csv")
    data = pd.read_csv("train2.csv")
else:
    test = pd.read_csv("train2.csv")
    data = pd.read_csv("train3.csv")
    


#tr_features = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f20', 'f21', 'f22', 'f23', 'f24', 'f25', 'f26', 'f27', 'f28', 'f29', 'f30', 'f31', 'f32', 'f33', 'f34', 'f35', 'f36', 'f37', 'f38', 'f39', 'f40', 'f41', 'f42', 'f43', 'f44', 'f45', 'f46', 'f47', 'f48', 'f49', 'f50', 'f51', 'f52', 'f53', 'f54']
#tr_features = ['f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f20', 'f21', 'f22', 'f23', 'f24', 'f25', 'f26', 'f27', 'f28', 'f29', 'f30', 'f31', 'f32', 'f33', 'f34', 'f35', 'f36', 'f37', 'f38', 'f39', 'f40', 'f41', 'f42', 'f43', 'f44', 'f45', 'f46', 'f47', 'f48', 'f49', 'f50', 'f51', 'f52', 'f53', 'f54']
tr_features = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10']
ts_features = 'class'

classifiers = [
    KNeighborsClassifier(1),                                                    #  0
    KNeighborsClassifier(3),                                                    #  1
    KNeighborsClassifier(6),                                                    #  2
    SVC(kernel="linear", C=0.025),                                              #  3
    SVC(kernel="linear", C=1),                                                  #  4
    SVC(kernel="linear", C=100),                                                #  5
    SVC(gamma=0.5, C=0.1),                                                      #  6
    SVC(gamma=2, C=1),                                                          #  7
    SVC(gamma=50, C=100),                                                       #  8
    DecisionTreeClassifier(max_depth=5),                                        #  9
    DecisionTreeClassifier(max_depth=10),                                       # 10
    SVC(gamma=2, C=1000),                                                       # 11
    SVC(gamma=2, C=100),                                                        # 12
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),       # 13
    RandomForestClassifier(max_depth=10, n_estimators=10, max_features=1),      # 14
    RandomForestClassifier(max_depth=10, n_estimators=50, max_features=5),      # 15
    AdaBoostClassifier(),                                                       # 16
    GaussianNB(),                                                               # 17
    MultinomialNB(),                                                            # 18
    BernoulliNB(),                                                              # 19
    LDA(),                                                                      # 20
    QDA()                                                                       # 21
    ]
              #0  #1  #2  #3  #4  #5  #6  #7  #8  #9 #10 #11 #12 #13 #14 #15 #16 #17 #18 #19 #20 #21
needtocheck = [1,  1,  1,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  0,  1,  1,  0]

i = -1;

for fier in classifiers:
    i += 1
    if needtocheck[i] == 1:

        clf = fier
        
        clf.fit(data[tr_features], data[ts_features])
        preds = clf.predict(data[tr_features])
    
        if mode != 1:
            print i
            accuracy = np.where(preds==data[ts_features], 1, 0).sum() / float(len(data))    
            print accuracy

        if mode == 1:
            print 'class'

            for i in preds:
                print i
    
