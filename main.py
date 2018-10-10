
import pandas as pd
from sklearn.datasets import load_digits
from sklearn.linear_model import Perceptron
from StopWatch import StopWatch
X, y = load_digits(return_X_y=True)
ST= StopWatch()
clf = Perceptron(tol=1e-3, random_state=0)
ST.Reset()
clf.fit(X, y)
ST.RP()
clf.score(X, y)
ST.Print()
print(' Perceptron Accuarcy for Digits : '+ str(clf.score(X, y)*100))

from sklearn import svm

clf_SVM = svm.SVC(gamma=0.001)
ST.Reset()
clf_SVM.fit(X, y)
ST.RP()
clf_SVM.score(X, y)
ST.Print()
print(" SVC Accuarcy for Digits : "+ str(clf_SVM.score(X, y)*100))

from sklearn.svm import LinearSVC

clf_SVML = LinearSVC(random_state=0, tol=1e-5)
ST.Reset()
clf_SVML.fit(X, y)
ST.RP()
clf_SVML.score(X, y)
ST.Print()
print(" Linear SVM Accuarcy for Digits : "+ str(clf_SVML.score(X, y)*100))

from sklearn.svm import NuSVC

clf_SVMN =  NuSVC(gamma=0.001)
ST.Reset()
clf_SVMN.fit(X, y)
ST.RP()
clf_SVMN.score(X, y)
ST.Print()
print(" RBF Accuarcy for Digits : "+ str(clf_SVMN.score(X, y)*100))


from sklearn import tree
clf_T = tree.DecisionTreeClassifier()
ST.Reset()
clf_T.fit(X, y)
ST.RP()
clf_T.score(X, y)
ST.Print()
print(" Decision Tree Accuarcy for Digits : "+ str(clf_T.score(X, y)*100))

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=1)
ST.Reset()
neigh.fit(X, y) 
ST.RP()
neigh.score(X, y)
ST.Print()
print(" K Nearest Neighbors Accuarcy for Digits : "+ str(neigh.score(X, y)*100))

from sklearn.linear_model import LogisticRegression

LR = LogisticRegression(random_state=0, solver='lbfgs',
                         multi_class='multinomial')
ST.Reset()
LR.fit(X,y)
ST.RP()
LR.score(X, y)
ST.Print()
print(" Logistic Regression Accuarcy for Digits : "+ str(LR.score(X, y)*100))

print(" ************************************************* ")

df = pd.read_csv('subject1_ideal.csv', header=None)
df.tail()

y = df.iloc[0:17900, 119].values
X = df.iloc[0:17900, [0, 118]].values

ST= StopWatch()
clf = Perceptron(tol=1e-3, random_state=0)
ST.Reset()
clf.fit(X, y)
ST.RP()
clf.score(X, y)
ST.Print()
print(' Perceptron Accuarcy for time-series instances : '+ str(clf.score(X, y)*100))


clf_SVM = svm.SVC(gamma=0.001)
ST.Reset()
clf_SVM.fit(X, y)
ST.RP()
clf_SVM.score(X, y)
ST.Print()
print(" SVC Accuarcy for time-series instances : "+ str(clf_SVM.score(X, y)*100))


clf_SVML = LinearSVC(random_state=0, tol=1e-5)
ST.Reset()
clf_SVML.fit(X, y)
ST.RP()
clf_SVML.score(X, y)
ST.Print()
print(" Linear SVM Accuarcy for time-series instances : "+ str(clf_SVML.score(X, y)*100))

'''
clf_SVMN =  NuSVC(random_state=0, tol=1e-5)
ST.Reset()
clf_SVMN.fit(X, y)
ST.RP()
clf_SVMN.score(X, y)
ST.Print()
print(" RBF Accuarcy for time-series instances : "+ str(clf_SVMN.score(X, y)*100))
'''

clf_T = tree.DecisionTreeClassifier()
ST.Reset()
clf_T.fit(X, y)
ST.RP()
clf_T.score(X, y)
ST.Print()
print(" Decision Tree Accuarcy for time-series instances : "+ str(clf_T.score(X, y)*100))

neigh = KNeighborsClassifier(n_neighbors=1)
ST.Reset()
neigh.fit(X, y) 
ST.RP()
neigh.score(X, y)
ST.Print()
print(" K Nearest Neighbors Accuarcy for time-series instances : "+ str(neigh.score(X, y)*100))


LR = LogisticRegression(random_state=0, solver='lbfgs',
                         multi_class='multinomial')
ST.Reset()
LR.fit(X,y)
ST.RP()
LR.score(X, y)
ST.Print()
print(" Logistic Regression Accuarcy for time-series instances : "+ str(LR.score(X, y)*100))