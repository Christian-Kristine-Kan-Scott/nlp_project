import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

def lr_stemm(y_train_stemmed, y_test_stemmed, X_train_stemmed, X_test_stemmed):
    '''
    This function takes stemm data and creates dataframes for y_test and y_train.
    It takes the data frames and fits logistic regression and makes a prediction
    '''
    # create dataframe for stemm train / test
    y_train_stemmed = pd.DataFrame(dict(actual=y_train_stemmed))
    y_test_stemmed = pd.DataFrame(dict(actual=y_test_stemmed))
    
    # create logistics regesson object by fitting to X_trian and y_train
    lm_stemm = LogisticRegression().fit(X_train_stemmed, y_train_stemmed)
    
    # make prediction on train and test for stemm data
    y_train_stemmed['predicted'] = lm_stemm.predict(X_train_stemmed)
    y_test_stemmed['predicted'] = lm_stemm.predict(X_test_stemmed)
    
    return y_train_stemmed, y_test_stemmed


def lr_lemm(y_train_lemmed, y_test_lemmed, X_train_lemmed, X_test_lemmed):
    '''
    This function takes lemm data and creates dataframes for y_test and y_train.
    It takes the data frames and fits logistic regression and makes a prediction
    '''
    # create dataframe for lemm train / test 
    y_train_lemmed = pd.DataFrame(dict(actual=y_train_lemmed))
    y_test_lemmed = pd.DataFrame(dict(actual=y_test_lemmed))
    
    # create logistics regesson object by fitting to X_trian and y_train
    lm_lemm = LogisticRegression().fit(X_train_lemmed, y_train_lemmed)
    
    # make prediction on train and test for Lemmatize data
    y_train_lemmed['predicted'] = lm_lemm.predict(X_train_lemmed)
    y_test_lemmed['predicted'] = lm_lemm.predict(X_test_lemmed)
    
    return y_train_lemmed, y_test_lemmed
    
    
def lr_print(y_train_lemmed, y_test_lemmed, y_train_stemmed, y_test_stemmed):
    '''
    This function prints the accuracy score for for stemm and lemm data using logistics regression
    '''
    print(f"TRAIN\nLogistics Regression Stemmed Accuracy: {round(accuracy_score(y_train_stemmed.actual, y_train_stemmed.predicted), 2)}")
    print(f"Logistics Regression Lemmed Accuracy: {round(accuracy_score(y_train_lemmed.actual, y_train_lemmed.predicted), 2)}")


    print(f"\nTEST\nLogistics Regression Stemmed Accuracy Test: {round(accuracy_score(y_test_stemmed.actual, y_test_stemmed.predicted), 2)}")
    print(f"Logistics Regression Lemmed Accuracy Test: {round(accuracy_score(y_test_lemmed.actual, y_test_lemmed.predicted), 2)}")
    



    
    